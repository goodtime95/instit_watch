import logging
from typing import Any

from app.collectors.providers.rss_provider import fetch_rss_feed
from config.constants import CENTRAL_BANK_RSS_FEEDS

logger = logging.getLogger(__name__)


def collect_central_bank_data() -> dict[str, Any]:
    central_bank_data: dict[str, Any] = {}

    for name, url in CENTRAL_BANK_RSS_FEEDS.items():
        central_bank_data[name] = fetch_rss_feed(url, limit=5)

    logger.info("Central bank RSS data collected successfully")

    return central_bank_data