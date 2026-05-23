from datetime import datetime
from PyPDF2 import PdfMerger
import email
import imaplib
import os
import pathlib
from typing import Any, Final

PATH: Final = "src/email/invoice/"


class InvoiceSummary:
    __conn: imaplib.IMAP4_SSL

    def __init__(self, conn: Any):
        self.__conn = conn.client

    @classmethod
    def build_summarizer(cls, conn: Any):
        return cls(conn)

    def run(self):
        client = self.__conn
        client.select("Invoices", readonly=True)
        _, mail = client.search(None, "ALL")
        for mail_id in mail[0].split():
            _, msg_data = client.fetch(mail_id, "(RFC822)")
            email_message = email.message_from_bytes(msg_data[0][1])
            if self.__check_download_eligibility(email_message):
                self.__extractAttachment(email_message)
        self.__merge_pdfs()

    def __extractAttachment(self, email_message: Any):
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                # TODO: read the date and automate one month extraction.
                pass
            elif part.get_content_type() == "application/pdf":
                filename = pathlib.Path(PATH).resolve() / part.get_filename()
                filename.parent.mkdir(parents=True, exist_ok=True)
                if filename:
                    with open(filename, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    print(f"Saved attachment: {filename}")

    def __merge_pdfs(self):
        merger = PdfMerger()
        for filename in os.listdir(PATH):
            pdf_path = os.path.join(PATH, filename)
            merger.append(pdf_path)
        with open("final.pdf", "wb") as f:
            merger.write(f)

    def __check_download_eligibility(self, email_message):
        date = email_message['date']
        date_obj = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S %z").date()
        date_today = datetime.today().date()
        delta = date_today - date_obj
        if delta.days > 30:
            return False
        
        return True
