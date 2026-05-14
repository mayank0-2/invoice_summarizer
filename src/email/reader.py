import imaplib
import os
import email
from PyPDF2 import PdfMerger
import pathlib

# Securely load credentials from environment variables
EMAIL = os.environ.get("GMAIL_ADDRESS", default="***")
APP_PASSWORD = os.environ.get("GMAIL_APP_PASSWORD", default="****")


def setup_connection():
    if not EMAIL or not APP_PASSWORD:
        raise ValueError(
            "Please set GMAIL_ADDRESS and GMAIL_APP_PASSWORD environment variables."
        )

    print("Setting up connection to email server...")
    with imaplib.IMAP4_SSL("imap.gmail.com", port=993) as imap:
        print("Logging in to email server...")
        a, b = imap.login(EMAIL, APP_PASSWORD)
        
        # selecting inbox
        status, messages = imap.select("Invoices", readonly=True)
        status, mail = imap.search(None, "ALL")
        for mail_id in mail[0].split():
            _, msg_data = imap.fetch(mail_id, "(RFC822)")
            email_message = email.message_from_bytes(msg_data[0][1])
            date = email_message["Date"]

            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    body_bytes = part.get_payload(decode=True)
                    charset = part.get_content_charset() or "utf-8"
                    body = (
                        body_bytes.decode(charset, errors="replace")
                        if body_bytes
                        else ""
                    )
                    print(f"Date: {date}")
                    print(f"Body: {body}")
                    print("-" * 50)
                    with open(f"email_{mail_id.decode()}.txt", "w") as f:
                        f.write(f"Date: {date}\n")
                        f.write(f"Body: {body}\n")
                        f.write("-" * 50 + "\n")
                        f.write(body)
                elif part.get_content_type() == "application/pdf":
                    filename = pathlib.Path(__file__).resolve().parent / "invoice" / part.get_filename()
                    filename.parent.mkdir(parents=True, exist_ok=True)
                    if filename:
                        with open(filename, "wb") as f:
                            f.write(part.get_payload(decode=True))
                        print(f"Saved attachment: {filename}")
                    print(f"Date: {date}")
                    print("No text/plain part found in this email.")
                    print("-" * 50)
        imap.logout()

    merger = PdfMerger()

    for filename in os.listdir("src/email/invoice"):
        pdf_path = os.path.join("src/email/invoice/", filename)
        merger.append(pdf_path)
    with open("final.pdf", "wb") as f :
        merger.write(f)


if __name__ == "__main__":
    setup_connection()
