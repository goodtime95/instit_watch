import logging
from datetime import date, timedelta

from fredapi import Fred

from config.settings import settings

logger = logging.getLogger(__name__)


def fetch_latest_series_value(series_id: str) -> dict[str, float | str | int | None]:
    if not settings.fred_api_key:
        logger.warning("FRED_API_KEY is missing")
        return _empty_result()

    fred = Fred(api_key=settings.fred_api_key)

    start_date = date.today() - timedelta(days=120)
    data = fred.get_series(series_id, observation_start=start_date.isoformat())

    if data.empty:
        logger.warning("No FRED data found for series %s", series_id)
        return _empty_result()

    clean_data = data.dropna()

    if len(clean_data) == 0:
        logger.warning("Only empty FRED data found for series %s", series_id)
        return _empty_result()

    latest_date = clean_data.index[-1].date()
    latest_value = float(clean_data.iloc[-1])

    previous_date = None
    previous_value = None
    change_bps = None

    if len(clean_data) >= 2:
        previous_date = clean_data.index[-2].date()
        previous_value = float(clean_data.iloc[-2])
        change_bps = round((latest_value - previous_value) * 100)

    staleness_days = (date.today() - latest_date).days

    return {
        "value": round(latest_value, 4),
        "date": latest_date.isoformat(),
        "previous_value": round(previous_value, 4) if previous_value is not None else None,
        "previous_date": previous_date.isoformat() if previous_date else None,
        "change_bps": change_bps,
        "staleness_days": staleness_days,
    }


def _empty_result() -> dict[str, float | str | int | None]:
    return {
        "value": None,
        "date": None,
        "previous_value": None,
        "previous_date": None,
        "change_bps": None,
        "staleness_days": None,
    }