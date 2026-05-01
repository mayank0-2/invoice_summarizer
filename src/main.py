import argparse

import loguru

from src.common import Args
from src.email.reader import setup_connection


def main():
    logger = loguru.logger
    args = parse_args()
    setup_connection()


def parse_args() -> Args:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--email",
        type=str,
        help="Enter Email Address.",
        required=True,
    )
    parser.add_argument(
        "--password",
        type=str,
        help="Enter password for email",
        required=True,
    )

    args = parser.parse_args()
    return Args(**vars(args))


#    reader = PdfReader("test.pdf")
#    page = reader.pages[0]
#    text = page.extract_text()
#    index = text.find("Total")
#    temp = text[index:]
#    indexnew = temp.find("\n")
#    print(temp[:indexnew])


if __name__ == "__main__":
    main()
