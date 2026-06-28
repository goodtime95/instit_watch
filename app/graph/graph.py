from langgraph.graph import END, StateGraph

from app.agents.brief_reviewer import review_brief
from app.agents.brief_writer import write_brief
from app.collectors.mock_collector import collect_mock_data
from app.graph.state import InstitutionalBriefState
from app.services.validator import validate_data


def build_graph():
    graph = StateGraph(InstitutionalBriefState)

    graph.add_node("collect_data", collect_mock_data)
    graph.add_node("validate_data", validate_data)
    graph.add_node("write_brief", write_brief)
    graph.add_node("review_brief", review_brief)

    graph.set_entry_point("collect_data")

    graph.add_edge("collect_data", "validate_data")
    graph.add_edge("validate_data", "write_brief")
    graph.add_edge("write_brief", "review_brief")
    graph.add_edge("review_brief", END)

    return graph.compile()