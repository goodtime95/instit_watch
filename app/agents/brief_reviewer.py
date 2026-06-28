from app.graph.state import InstitutionalBriefState


def review_brief(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    Basic deterministic reviewer for Sprint 1.
    No LLM call yet.
    """

    brief = state.get("final_brief", "")
    warnings = state.get("warnings", [])

    forbidden_terms = [
        "acheter absolument",
        "vendre absolument",
        "sans risque",
    ]

    for term in forbidden_terms:
        if term.lower() in brief.lower():
            warnings.append(f"Potential compliance issue: '{term}'")

    if "Sources" not in brief:
        warnings.append("Brief does not contain a sources section.")

    if warnings:
        warning_block = "\n\nAvertissements de validation :\n"
        warning_block += "\n".join(f"- {warning}" for warning in warnings)
        state["final_brief"] = brief + warning_block

    state["warnings"] = warnings

    return state