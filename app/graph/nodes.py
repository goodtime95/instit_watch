from datetime import date

from app.collectors.central_bank_collector import collect_central_bank_data
from app.collectors.macro_collector import collect_macro_data
from app.collectors.market_collector import collect_market_data
from app.collectors.rates_collector import collect_rates_data
from app.graph.state import InstitutionalBriefState


def initialize_run(state: InstitutionalBriefState) -> InstitutionalBriefState:
    state["run_date"] = date.today().isoformat()
    state["warnings"] = state.get("warnings", [])
    state["sources"] = state.get("sources", [])
    return state


def collect_market_node(state: InstitutionalBriefState) -> InstitutionalBriefState:
    state["market_data"] = collect_market_data()
    state["sources"].append(
        {"name": "Yahoo Finance", "url": "https://finance.yahoo.com/"}
    )
    return state


def collect_rates_node(state: InstitutionalBriefState) -> InstitutionalBriefState:
    state["rates_data"] = collect_rates_data()
    state["sources"].append(
        {"name": "FRED", "url": "https://fred.stlouisfed.org/"}
    )
    return state


def collect_macro_node(state: InstitutionalBriefState) -> InstitutionalBriefState:
    state["macro_data"] = collect_macro_data()
    state["sources"].append(
        {
            "name": "Mock macro dataset",
            "url": "local://mock-macro-data",
        }
    )
    return state


def collect_central_bank_node(
    state: InstitutionalBriefState,
) -> InstitutionalBriefState:
    state["central_bank_data"] = collect_central_bank_data()
    state["sources"].append(
        {
            "name": "Mock central bank dataset",
            "url": "local://mock-central-bank-data",
        }
    )
    return state


def collect_news_node(state: InstitutionalBriefState) -> InstitutionalBriefState:
    state["news_data"] = {
        "headlines": [
            "Markets remain focused on central bank guidance.",
            "Energy prices edge higher amid supply concerns.",
        ],
        "is_mock": True,
    }
    state["sources"].append(
        {
            "name": "Mock news dataset",
            "url": "local://mock-news-data",
        }
    )
    return state