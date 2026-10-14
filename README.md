# Invoice Summarizer

## Overview

A Python automation tool that streamlines your accounting workflow by automatically fetching PDF invoices from your Gmail account and merging them into a single, consolidated PDF document.

## Features

- **Automated Extraction:** Connects to Gmail securely via IMAP and extracts PDF attachments from the "Invoices" folder.
- **PDF Consolidation:** Uses `PyPDF2` to seamlessly merge all extracted invoices into a single `final.pdf` document.
- **Direct Email Sending:** Automatically sends the consolidated invoice as an email attachment without manual drafting.
- **Logging:** Integrated `loguru` for detailed runtime logging.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mayank0-2/invoice_summarizer.git
   cd invoice_summarizer
   ```

2. **Install Dependencies:**
   ```bash
   make build
   ```

3. **Set Environment Variables:**
   - `EMAIL`: Your Gmail address (e.g., `youremail@gmail.com`)
   - `APP_PASSWORD`: Your 16-character Gmail App Password

   *Note: Ensure your `.vscode/launch.json` or `.env` files are added to `.gitignore`*

## Usage

Run the main script:
```bash
make run
```

The consolidated invoice will be saved as `final.pdf` in the root directory.
