import logging

from app.graph.graph import build_graph
from config.logging_config import setup_logging
from config.settings import settings

logger = logging.getLogger(__name__)


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


def main() -> None:
    setup_logging()

    logger.info("Starting %s", settings.app_name)

    app = build_graph()
    result = app.invoke(create_initial_state())

    logger.info("Brief generated successfully")

    print("\n" + "=" * 80)
    print(result["final_brief"])
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()