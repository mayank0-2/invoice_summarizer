import loguru

from src.common import InvoiceSummary
from src.email.config import config
from src.email.gmail import GmailClient


def main():
    logger = loguru.logger
    client_engine = GmailClient.__build_client(config, logger)
    summary = InvoiceSummary.__build_summarizer(client_engine)
    summary.__run()
    GmailClient.__logout(client_engine)


if __name__ == "__main__":
    main()
