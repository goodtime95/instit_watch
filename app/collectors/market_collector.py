import logging
from typing import Any

from app.collectors.providers.yahoo_provider import fetch_latest_market_point
from config.constants import DEFAULT_COMMODITIES, DEFAULT_MARKET_INDEXES

logger = logging.getLogger(__name__)


def collect_market_data() -> dict[str, Any]:
    market_data: dict[str, Any] = {
        "equities": {},
        "commodities": {},
    }

    for name, ticker in DEFAULT_MARKET_INDEXES.items():
        market_data["equities"][name] = fetch_latest_market_point(ticker)

    for name, ticker in DEFAULT_COMMODITIES.items():
        market_data["commodities"][name] = fetch_latest_market_point(ticker)

    logger.info("Market data collected successfully")

    return market_data