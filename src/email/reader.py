import imaplib
import os
import email

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
            date = email_message['Date']

            imap.logout()

        


if __name__ == "__main__":
    setup_connection()
