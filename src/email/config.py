from dataclasses import dataclass
import os


@dataclass
class Config:
    env: str = os.getenv("ENV", "dev")
    email: str = os.getenv("EMAIL", "")
    app_password: str = os.getenv("APP_PASSWORD", "")


config = Config()
