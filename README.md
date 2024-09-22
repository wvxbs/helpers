# helpers

# PDF e PPTX Text Extractor

Este projeto contém scripts para extrair texto de arquivos PDF e PPTX, convertendo o conteúdo em arquivos de texto simples. Os scripts utilizam as bibliotecas `pdfplumber` e `python-pptx`, e a configuração é feita via variáveis de ambiente.

## Requisitos

As dependências do projeto estão listadas no arquivo `requirements.txt`. Para instalar as bibliotecas necessárias, execute:

```bash
pip install -r requirements.txt
```

Variáveis de ambiente:
```bash
PDF_FILE=path/to/your/input.pdf
PDF_OUTPUT_FILE=path/to/your/output.txt
PPTX_FILE=path/to/your/input.pptx
PPTX_OUTPUT_FILE=path/to/your/output.txt
```