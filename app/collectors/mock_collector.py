from datetime import date
from app.graph.state import InstitutionalBriefState
from app.collectors.market_collector import collect_market_data
from app.collectors.rates_collector import collect_rates_data


def collect_mock_data(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Temporary mock collector for Sprint 1.
    No external API call here.
    """

    state["run_date"] = date.today().isoformat()

    state["market_data"] = state["market_data"] = collect_market_data()
    
    state["rates_data"] = collect_rates_data()

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
        {"name": "Yahoo Finance", "url": "https://finance.yahoo.com/"},
        {"name": "FRED", "url": "https://fred.stlouisfed.org/"},
        {"name": "Mock macro and central bank dataset", "url": "local://mock-macro-cb-data"},
    ]

    return state