from pydantic import BaseModel

from app.core.models import Source

class DailyBriefResponse(BaseModel):
    subject: str
    body: str
    sources: list[Source]
    warnings: list[str]