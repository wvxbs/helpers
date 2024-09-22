import pdfplumber
from dotenv import load_dotenv
import os

def extractTextFromPdf(inputFile):
    with pdfplumber.open(inputFile) as pdf:
        textContent = []
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                textContent.append(text)
    return "\n".join(textContent)

load_dotenv()

pdfFile = os.getenv("PDF_FILE")
outputFile = os.getenv("PDF_OUTPUT_FILE")

plainText = extractTextFromPdf(pdfFile)

with open(outputFile, "w", encoding="utf-8") as f:
    f.write(plainText)

print("Exportação de PDF para texto concluída!")