from dataclasses import dataclass
from datetime import datetime
from typing import Literal
from parsers import safe_parse_date

@dataclass
class NormalizedHost:
    id: str
    ip: str
    hostname: str
    os: str
    platform: str
    last_seen: datetime
    source: Literal["qualys", "crowdstrike"]

def normalize_qualys(host: dict) -> NormalizedHost:
    return NormalizedHost(
        id=str(host["_id"]),
        ip=host.get("address", ""),
        hostname=host.get("dnsHostName", ""),
        os=host.get("agentInfo", {}).get("platform", ""),
        platform="Qualys",
        last_seen=safe_parse_date(
            host.get("agentInfo", {}).get("lastCheckedIn", {}).get("$date", "")
        ),
        source="qualys"
    )

def normalize_crowdstrike(host: dict) -> NormalizedHost:
    return NormalizedHost(
        id=host.get("device_id", ""),
        ip=host.get("local_ip", ""),
        hostname=host.get("hostname", ""),
        os=host.get("os_version", ""),
        platform=host.get("platform_name", ""),
        last_seen=safe_parse_date(host.get("last_seen", "")),
        source="crowdstrike"
    )
