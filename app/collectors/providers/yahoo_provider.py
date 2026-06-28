import logging
from typing import Any

import yfinance as yf

logger = logging.getLogger(__name__)


def fetch_latest_market_point(ticker: str) -> dict[str, float | None]:
    data = yf.Ticker(ticker).history(period="5d")

    if data.empty:
        logger.warning("No market data found for ticker %s", ticker)
        return {
            "level": None,
            "daily_change_pct": None,
        }

    close = data["Close"].dropna()

    if len(close) < 2:
        logger.warning("Not enough market data for ticker %s", ticker)
        return {
            "level": float(close.iloc[-1]),
            "daily_change_pct": None,
        }

    latest = float(close.iloc[-1])
    previous = float(close.iloc[-2])
    daily_change_pct = ((latest - previous) / previous) * 100

    return {
        "level": round(latest, 2),
        "daily_change_pct": round(daily_change_pct, 2),
    }