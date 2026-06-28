from typing import Any


def collect_macro_data() -> dict[str, Any]:
    """
    Temporary mock macro collector.
    Will be replaced later by real macro/calendar sources.
    """

    return {
        "today_calendar": [
            "US durable goods orders",
            "Eurozone consumer confidence",
        ],
        "is_mock": True,
    }