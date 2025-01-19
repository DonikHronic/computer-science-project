import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

COLOR_MAPPING = {
    "AVAILABLE": "skyblue",
    "IMPACTED": "yellow",
    "BLOCKED": "red",
    "NEW": "green",
    "REMEDIATED": "lightgreen",
}
