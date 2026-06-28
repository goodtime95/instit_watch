import logging
from typing import Any

from app.collectors.providers.fred_provider import fetch_latest_series_value
from config.constants import FRED_RATES_SERIES

logger = logging.getLogger(__name__)


def collect_rates_data() -> dict[str, Any]:
    rates_data: dict[str, Any] = {}

    for name, series_id in FRED_RATES_SERIES.items():
        rates_data[name] = fetch_latest_series_value(series_id)

    logger.info("Rates data collected successfully")

    return rates_data