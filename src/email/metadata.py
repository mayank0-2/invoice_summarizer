from datetime import datetime
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class MetaData:
    to: List[str]
    bcc: List[str] = field(default_factory=list)
    subject: str = "HungerBox Invoice Summary for {}."
    body: str = (
        "Hi, \n\nPlease find the attached PDF containing the invoice summary "
        "of 2000 rupees for this month.\n\nBest regards,\nMayank Kumar"
    )

    @classmethod
    def build(cls, to: List[str], bcc: Optional[List[str]] = None):
        formated_date = datetime.now().strftime("%b %Y")
        return cls(
            to=to,
            bcc=bcc or [],
            subject=cls.subject.format(formated_date),
        )
