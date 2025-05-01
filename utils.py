from datetime import datetime, timezone
from dateutil.parser import isoparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from api import safe_post
from config import SILK_API_URL, MAX_ALLOWED_SKIP, LIMIT_PER_PAGE
from models import normalize_qualys, normalize_crowdstrike

def safe_parse_date(date_str: str) -> datetime:
    try:
        return isoparse(date_str).astimezone(timezone.utc)
    except Exception:
        return datetime(1970, 1, 1, tzinfo=timezone.utc)

def fetch_and_normalize(fetch_fn, max_skip):
    hosts = []
    with ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(fetch_fn, skip, LIMIT_PER_PAGE)
            for skip in range(0, max_skip, LIMIT_PER_PAGE)
            if skip <= MAX_ALLOWED_SKIP
        ]
        for f in as_completed(futures):
            try:
                hosts.extend(f.result())
            except Exception as e:
                print(f"Error in thread: {e}")
    return hosts

def fetch_and_normalize_qualys(skip, limit=LIMIT_PER_PAGE):
    url = f"{SILK_API_URL}/api/qualys/hosts/get?skip={skip}&limit={limit}"
    return [normalize_qualys(h) for h in safe_post(url)]

def fetch_and_normalize_crowdstrike(skip, limit=LIMIT_PER_PAGE):
    url = f"{SILK_API_URL}/api/crowdstrike/hosts/get?skip={skip}&limit={limit}"
    return [normalize_crowdstrike(h) for h in safe_post(url)]

def deduplicate_hosts(hosts):
    deduped = {}
    for host in hosts:
        key = f"{host.ip}|{host.hostname}"
        if key not in deduped or host.last_seen > deduped[key].last_seen:
            deduped[key] = host
    return list(deduped.values())
