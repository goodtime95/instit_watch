from langgraph.graph import END, StateGraph

from app.agents.brief_reviewer import review_brief
from app.agents.brief_writer import write_brief
from app.graph.nodes import (
    collect_central_bank_node,
    collect_macro_node,
    collect_market_node,
    collect_news_node,
    collect_rates_node,
    initialize_run,
)
from app.graph.state import InstitutionalBriefState
from app.services.validator import validate_data


def build_graph():
    graph = StateGraph(InstitutionalBriefState)

    graph.add_node("initialize_run", initialize_run)
    graph.add_node("collect_market", collect_market_node)
    graph.add_node("collect_rates", collect_rates_node)
    graph.add_node("collect_macro", collect_macro_node)
    graph.add_node("collect_central_bank", collect_central_bank_node)
    graph.add_node("collect_news", collect_news_node)
    graph.add_node("validate_data", validate_data)
    graph.add_node("write_brief", write_brief)
    graph.add_node("review_brief", review_brief)

    graph.set_entry_point("initialize_run")

    graph.add_edge("initialize_run", "collect_market")
    graph.add_edge("collect_market", "collect_rates")
    graph.add_edge("collect_rates", "collect_macro")
    graph.add_edge("collect_macro", "collect_central_bank")
    graph.add_edge("collect_central_bank", "collect_news")
    graph.add_edge("collect_news", "validate_data")
    graph.add_edge("validate_data", "write_brief")
    graph.add_edge("write_brief", "review_brief")
    graph.add_edge("review_brief", END)

    return graph.compile()