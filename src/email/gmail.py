from loguru import logger
import email.encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import imaplib
import smtplib
from email.mime.multipart import MIMEMultipart
from multiprocessing import AuthenticationError
from src.email.metadata import MetaData

from src.email.config import Config


class GmailClient:
    client: imaplib.IMAP4_SSL

    def __init__(self, conn: imaplib.IMAP4_SSL, config: Config):
        self.client = conn
        self._config = config

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
        return cls(conn, config)

    def _build_message(self, metadata: MetaData) -> MIMEMultipart:
        if not metadata.to:
            raise ValueError("RECIPIENTS is required (comma-separated emails).")
        msg = MIMEMultipart()
        msg["From"] = self._config.email
        msg["To"] = ", ".join(metadata.to)
        msg["Subject"] = metadata.subject
        msg.attach(MIMEText(metadata.body, "plain"))

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
        return msg

    def send_mail(self, metadata: MetaData):
        msg = self._build_message(metadata)
        envelope = metadata.to + metadata.bcc
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
                smtp.starttls()
                smtp.login(self._config.email, self._config.app_password)
                smtp.send_message(
                    msg, from_addr=self._config.email, to_addrs=envelope
                )
        except smtplib.SMTPAuthenticationError as e:
            logger.error("SMTP authentication failed. Check email and app password.", e)
            raise AuthenticationError(
                "Authentication failed. Check email and app password."
            )
        logger.info("Sent invoice summary to {}", ", ".join(metadata.to))
