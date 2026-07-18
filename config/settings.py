from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    APP_NAME = "AI Job Agent"
    APP_VERSION = "0.1"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

    DATABASE_URL = "sqlite:///jobs.db"

    DEBUG = True


settings = Settings()