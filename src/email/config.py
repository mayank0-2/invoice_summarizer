from dataclasses import dataclass, field
import os
from typing import List


def _parse_emails(raw: str) -> List[str]:
    return [part.strip() for part in raw.split(",") if part.strip()]


@dataclass
class Config:
    env: str = os.getenv("ENV", "dev")
    email: str = os.getenv("EMAIL", "")
    app_password: str = os.getenv("APP_PASSWORD", "")
    recipients: List[str] = field(
        default_factory=lambda: _parse_emails(os.getenv("RECIPIENTS", ""))
    )
    bcc: List[str] = field(
        default_factory=lambda: _parse_emails(os.getenv("BCC", ""))
    )


config = Config()
