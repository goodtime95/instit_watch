from datetime import date
from app.graph.state import InstitutionalBriefState
from app.collectors.market_collector import collect_market_data



def collect_mock_data(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Temporary mock collector for Sprint 1.
    No external API call here.
    """

    state["run_date"] = date.today().isoformat()

    state["market_data"] = state["market_data"] = collect_market_data()
    
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
            "name": "Yahoo Finance",
            "url": "https://finance.yahoo.com/",
        },
        {
            "name": "Mock rates and macro dataset",
            "url": "local://mock-rates-macro-data",
        },
    ]

    return state