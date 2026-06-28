import logging

from fastapi import FastAPI

from app.models.schemas import DailyBriefResponse
from app.services.brief_service import generate_daily_brief
from config.logging_config import setup_logging
from config.settings import settings

setup_logging()

logger = logging.getLogger(__name__)

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/brief/daily", response_model=DailyBriefResponse)
def daily_brief() -> DailyBriefResponse:
    logger.info("Daily brief API called")
    result = generate_daily_brief()

    return DailyBriefResponse(
        subject=result.subject,
        body=result.markdown,
        sources=result.sources,
        warnings=result.warnings,
    )