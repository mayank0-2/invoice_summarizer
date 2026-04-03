# invoice_summarizer
# Invoice Summarizer

A command-line tool to summarize invoices from PDF files. This tool extracts text from PDF documents, including scanned images within PDFs using Optical Character Recognition (OCR), and then uses a pre-trained language model to generate a summary.

## Prerequisites

Before you can use this tool, you need to have the following installed on your system:

*   **Python 3.14+**
*   **Tesseract OCR Engine**: This is required by the `pytesseract` library for extracting text from images.

### Tesseract Installation

You need to install the Tesseract OCR engine on your system.

*   **macOS**:
    ```bash
    brew install tesseract
    ```

*   **Debian/Ubuntu**:
    ```bash
    sudo apt install tesseract-ocr
    ```

*   **Windows**:
    Download and run the installer from the Tesseract at UB Mannheim page. During installation, make sure to include the language data for the languages you want to recognize.

For other systems, please refer to the official Tesseract installation documentation. [2]

## Installation

1.  Clone this repository to your local machine:
    ```bash
    git clone <your-repository-url>
    cd invoice-summarizer
    ```

2.  Install the project and its dependencies:
    ```bash
    pip install .
    ```
    This will install all the necessary Python packages listed in `pyproject.toml`.

## Usage

Once installed, you can use the `invoice-summarizer` command-line tool to summarize an invoice:

```bash
invoice-summarizer /path/to/your/invoice.pdf
```

Replace `/path/to/your/invoice.pdf` with the actual path to your PDF file.