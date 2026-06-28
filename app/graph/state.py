from typing import Any, Dict, List, TypedDict


class InstitutionalBriefState(TypedDict):
    """
    Shared state across the LangGraph workflow.
    """

    run_date: str

    market_data: Dict[str, Any]
    rates_data: Dict[str, Any]
    macro_data: Dict[str, Any]
    central_bank_data: Dict[str, Any]
    news_data: Dict[str, Any]

    warnings: List[str]

    draft_brief: str
    final_brief: str

    sources: List[Dict[str, str]]