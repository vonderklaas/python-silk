import requests
from config import HEADERS

def safe_post(url: str):
    response = requests.post(url, headers=HEADERS, data={})
    if response.status_code != 200:
        print(f"Request to {url} failed ({response.status_code})")
        return []
    try:
        return response.json()
    except Exception:
        print(f"Failed to parse JSON from {url}")
        return []
