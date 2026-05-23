from loguru import logger
import email.encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import imaplib
from email.mime.multipart import MIMEMultipart
from multiprocessing import AuthenticationError
from time import time
from src.email.metadata import MetaData

from src.email.config import Config


class GmailClient:
    client: imaplib.IMAP4_SSL

    def __init__(self, conn: imaplib.IMAP4_SSL):
        self.client = conn

    def logout(self):
        self.client.logout()

    @classmethod
    def build_client(cls, config: Config, logger: logger):
        logger.info("Setting up connection to email server...")
        conn = imaplib.IMAP4_SSL("imap.gmail.com", port=993)
        try:
            conn.login(config.email, config.app_password)
        except imaplib.IMAP4_SSL.error as e:
            logger.error("Authentication failed. Check email and app password.", e)
            raise AuthenticationError(
                "Authentication failed. Check email and app password."
            )
        return cls(conn)


    def draft_mail(self, metadata: MetaData):
        client = self.client
        msg = MIMEMultipart()
        msg["To"] = metadata.to
        msg["Subject"] = metadata.subject 
        body = metadata.body 

        msg.attach(MIMEText(body, "plain"))

        filename = "final.pdf"
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        email.encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        msg.attach(part)
        text = msg.as_string()
        client.select("[Gmail]/Drafts")
        client.append(
            "[Gmail]/Drafts",
            "",
            imaplib.Time2Internaldate(time()),
            text.encode("utf-8"),
        )
