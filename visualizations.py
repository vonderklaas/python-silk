import os
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime, timezone
OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_os_distribution(hosts):
    oses = [host.os for host in hosts]
    if not oses:
        print("⚠️ No OS data to visualize.")
        return
    sns.countplot(x=oses)
    plt.title("OS Distribution")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "os_distribution.png"))
    plt.show()

def plot_age_distribution(hosts):
    now = datetime.now(timezone.utc)
    old_count = sum((now - h.last_seen).days > 30 for h in hosts)
    new_count = len(hosts) - old_count
    sns.barplot(x=["Old Hosts", "New Hosts"], y=[old_count, new_count])
    plt.title("Host Age Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, "host_age_distribution.png"))
    plt.show()
