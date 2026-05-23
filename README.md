# Invoice Summarizer

A Python automation tool that streamlines your accounting workflow by automatically fetching PDF invoices from your Gmail account and merging them into a single, consolidated PDF document.

## Features

- **Automated Extraction:** Connects to Gmail securely via IMAP and extracts PDF attachments from the "Invoices" folder.
- **PDF Consolidation:** Uses `PyPDF2` to seamlessly merge all extracted invoices into a single `final.pdf` document.
- **Email Drafting:** Contains functionality to automatically draft a summary email with the consolidated invoice report attached.

## Prerequisites

- Python 3.8+
- [uv](https://docs.astral.sh/uv/) installed on your system.
- A Gmail account with 2-Step Verification enabled.
- A generated **Gmail App Password** (regular passwords will not work for IMAP).

## Setup & Configuration

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd invoice_summarizer
   ```

2. **Install Dependencies:**
   Use `uv` to set up your virtual environment and install dependencies:
   ```bash
   make build
   ```

3. **Environment Variables:**
   The application requires your Gmail credentials to be set as environment variables to authenticate securely.
   - `EMAIL`: Your Gmail address (e.g., `youremail@gmail.com`).
   - `APP_PASSWORD`: Your 16-character Gmail App Password.
   
   *Note: Ensure your `.vscode/launch.json` or `.env` files are added to `.gitignore` so you do not accidentally commit your app password to a public repository!*

## Usage

Run the main script using `uv` to start the extraction and merging process:

```bash
make run
```

The individual invoice files will be temporarily saved in `src/email/invoice/`, and the successfully merged output will be saved as `final.pdf` in the root directory.
