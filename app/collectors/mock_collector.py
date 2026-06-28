from datetime import date
from app.graph.state import InstitutionalBriefState


def collect_mock_data(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Temporary mock collector for Sprint 1.
    No external API call here.
    """

    state["run_date"] = date.today().isoformat()

    state["market_data"] = {
        "equities": {
            "S&P 500": {"level": 5450.0, "daily_change_pct": 0.42},
            "Nasdaq": {"level": 17800.0, "daily_change_pct": 0.65},
            "Euro Stoxx 50": {"level": 4950.0, "daily_change_pct": -0.18},
            "CAC 40": {"level": 7650.0, "daily_change_pct": -0.22},
        },
        "commodities": {
            "Brent": {"price": 84.2, "daily_change_pct": 0.31},
            "Gold": {"price": 2335.0, "daily_change_pct": -0.12},
        },
    }

    state["rates_data"] = {
        "US 2Y": {"yield_pct": 4.72, "daily_change_bps": 3},
        "US 10Y": {"yield_pct": 4.28, "daily_change_bps": 1},
        "EUR 10Y Bund": {"yield_pct": 2.45, "daily_change_bps": -2},
    }

    state["macro_data"] = {
        "today_calendar": [
            "US durable goods orders",
            "Eurozone consumer confidence",
        ]
    }

    state["central_bank_data"] = {
        "fed": "No major Fed decision in the mock dataset.",
        "ecb": "No major ECB decision in the mock dataset.",
    }

    state["news_data"] = {
        "headlines": [
            "Markets remain focused on central bank guidance.",
            "Energy prices edge higher amid supply concerns.",
        ]
    }

    state["sources"] = [
        {
            "name": "Mock market dataset",
            "url": "local://mock-market-data",
        }
    ]

    return state