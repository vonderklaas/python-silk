import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("SILK_API_KEY")
if not TOKEN:
    raise ValueError("SILK_API_KEY environment variable is not set.")

HEADERS = {
    "accept": "application/json",
    "token": TOKEN
}

SILK_API_URL = "https://api.recruiting.app.silk.security"
MAX_SKIP = 10
LIMIT_PER_PAGE = 2
MAX_ALLOWED_SKIP = 7
