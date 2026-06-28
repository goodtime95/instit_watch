from app.core.models import BriefResult, Source
from app.graph.graph import build_graph


def create_initial_state() -> dict:
    return {
        "run_date": "",
        "market_data": {},
        "rates_data": {},
        "macro_data": {},
        "central_bank_data": {},
        "news_data": {},
        "warnings": [],
        "draft_brief": "",
        "final_brief": "",
        "sources": [],
    }


def generate_daily_brief() -> BriefResult:
    graph = build_graph()
    result = graph.invoke(create_initial_state())

    return BriefResult(
        subject=f"Point institutionnel quotidien — {result['run_date']}",
        markdown=result["final_brief"],
        sources=[Source(**source) for source in result["sources"]],
        warnings=result["warnings"],
    )