import logging
from typing import Any

import feedparser

logger = logging.getLogger(__name__)


def fetch_rss_feed(url: str, limit: int = 5) -> list[dict[str, Any]]:
    feed = feedparser.parse(url)

    if feed.bozo:
        logger.warning("RSS parsing issue for feed %s", url)

    entries = []

    for entry in feed.entries[:limit]:
        entries.append(
            {
                "title": entry.get("title"),
                "link": entry.get("link"),
                "published": entry.get("published"),
                "summary": entry.get("summary"),
            }
        )

    return entries