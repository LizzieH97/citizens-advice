from pydantic import BaseModel

class Source(BaseModel):
    id: str
    title: str
    source: str
    favicon: str

class Data(BaseModel):
    category: str
    sources: list[Source]
    content: str