import json
from pathlib import Path

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

from app.graph.state import InstitutionalBriefState
from config.settings import settings


def write_brief(state: InstitutionalBriefState) -> InstitutionalBriefState:
    """
    LLM-based institutional brief writer.
    """

    llm = ChatOpenAI(
        model=settings.openai_model,
        temperature=settings.openai_temperature,
        api_key=settings.openai_api_key,
    )

    system_prompt = Path("app/prompts/brief_writer.md").read_text(encoding="utf-8")

    user_payload = {
        "run_date": state["run_date"],
        "market_data": state["market_data"],
        "rates_data": state["rates_data"],
        "macro_data": state["macro_data"],
        "central_bank_data": state["central_bank_data"],
        "news_data": state["news_data"],
        "sources": state["sources"],
        "warnings": state["warnings"],
    }

    response = llm.invoke(
        [
            SystemMessage(content=system_prompt),
            HumanMessage(
                content=(
                    "Voici les données disponibles pour le brief institutionnel du jour. "
                    "Rédige le brief en respectant strictement les contraintes du prompt système.\n\n"
                    f"{json.dumps(user_payload, ensure_ascii=False, indent=2)}"
                )
            ),
        ]
    )

    state["draft_brief"] = response.content
    state["final_brief"] = response.content

    return state