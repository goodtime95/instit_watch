from pydantic import BaseModel


class Source(BaseModel):
    name: str
    url: str


class BriefResult(BaseModel):
    subject: str
    markdown: str
    sources: list[Source]
    warnings: list[str]