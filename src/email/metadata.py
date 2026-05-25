from datetime import datetime
from dataclasses import dataclass



@dataclass
class MetaData:
    to = "" 
    subject = "HungerBox Invoice Summary for {}."
    body =  "Hi, \n\nPlease find the attached PDF containing the invoice summary of 2000 rupees for this month.\n\nBest regards,\nMayank Kumar"

    
    @classmethod
    def build(cls):
        formated_date = datetime.now().strftime("%b %Y")
        cls.subject = cls.subject.format(formated_date)
        return cls()
