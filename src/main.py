import loguru

from src.common import InvoiceSummary
from src.email.config import config
from src.email.gmail import GmailClient
from src.email.metadata import MetaData

def main():
    logger = loguru.logger
    client_engine = GmailClient.build_client(config, logger)
    summary = InvoiceSummary.build_summarizer(client_engine)
    summary.run()
    metadata = MetaData.build()
    client_engine.draft_mail(metadata)
    client_engine.logout()



if __name__ == "__main__":
    main()
