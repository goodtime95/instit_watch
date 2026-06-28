from app.graph.state import InstitutionalBriefState


def validate_data(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Basic deterministic validation for Sprint 1.
    """

    warnings = state.get("warnings", [])

    required_sections = [
        "market_data",
        "rates_data",
        "macro_data",
        "central_bank_data",
        "news_data",
    ]

    for section in required_sections:
        if not state.get(section):
            warnings.append(f"Missing section: {section}")

    if not state.get("sources"):
        warnings.append("No sources available.")

    state["warnings"] = warnings

    return state