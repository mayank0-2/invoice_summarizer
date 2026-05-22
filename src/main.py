import loguru

from src.common import InvoiceSummary
from src.email.config import config
from src.email.gmail import GmailClient


def main():
    logger = loguru.logger
    client_engine = GmailClient.build_client(config, logger)
    summary = InvoiceSummary.build_summarizer(client_engine)
    summary.run()
    client_engine.draft_mail()
    client_engine.logout()



if __name__ == "__main__":
    main()
