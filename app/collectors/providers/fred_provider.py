import logging
from datetime import date, timedelta

from fredapi import Fred

from config.settings import settings

logger = logging.getLogger(__name__)


def fetch_latest_series_value(series_id: str) -> dict[str, float | str | None]:
    if not settings.fred_api_key:
        logger.warning("FRED_API_KEY is missing")
        return {"value": None, "date": None}

    fred = Fred(api_key=settings.fred_api_key)

    start_date = date.today() - timedelta(days=90)
    data = fred.get_series(series_id, observation_start=start_date.isoformat())

    if data.empty:
        logger.warning("No FRED data found for series %s", series_id)
        return {"value": None, "date": None}

    clean_data = data.dropna()

    if clean_data.empty:
        logger.warning("Only empty FRED data found for series %s", series_id)
        return {"value": None, "date": None}

    latest_date = clean_data.index[-1].date().isoformat()
    latest_value = float(clean_data.iloc[-1])

    return {
        "value": round(latest_value, 4),
        "date": latest_date,
    }