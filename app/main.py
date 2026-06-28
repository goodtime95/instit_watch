import logging

from app.services.brief_service import generate_daily_brief
from config.logging_config import setup_logging
from config.settings import settings

logger = logging.getLogger(__name__)


def main() -> None:
    setup_logging()
    logger.info("Starting %s", settings.app_name)

    result = generate_daily_brief()

    logger.info("Brief generated successfully")

    print("\n" + "=" * 80)
    print(result.markdown)
    print("=" * 80 + "\n")


if __name__ == "__main__":
    main()