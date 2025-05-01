import os
import json
from config import MAX_SKIP
from visualizations import plot_os_distribution, plot_age_distribution
from utils import (
    fetch_and_normalize,
    fetch_and_normalize_qualys,
    fetch_and_normalize_crowdstrike,
    deduplicate_hosts
)
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Fetch
qualys_hosts = fetch_and_normalize(fetch_and_normalize_qualys, MAX_SKIP)
crowdstrike_hosts = fetch_and_normalize(fetch_and_normalize_crowdstrike, MAX_SKIP)
all_hosts = qualys_hosts + crowdstrike_hosts

# Dedup
deduped = deduplicate_hosts(all_hosts)
print(f"Total deduped hosts: {len(deduped)}")

# Save
with open(os.path.join(OUTPUT_DIR, "deduped_hosts.json"), "w") as f:
    json.dump([h.__dict__ for h in deduped], f, indent=2, default=str)

# Visualize
plot_os_distribution(deduped)
plot_age_distribution(deduped)

# Database
MONGO_DB_URI = os.getenv("MONGO_DB_URI")
client = MongoClient(MONGO_DB_URI)

db = client["silk_demo"]
collection = db["deduped_hosts"]

collection.delete_many({})
collection.insert_many([host.__dict__ for host in deduped])

print(f"Inserted {len(deduped)} records into MongoDB.")

client.close()