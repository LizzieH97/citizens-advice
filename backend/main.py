import json
import re
from fastapi import FastAPI
from pathlib import Path
from utils import extract_favicon_url
from models import Data
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "And we're up and running! Go to /data for the content."}


@app.get("/data", response_model=list[Data])
def get_data() -> list[Data]:
    raw = Path("data/mock.json").read_text()
    raw_data = json.loads(raw)

    output = []
    for item in raw_data:
        content = item["content"]
        cited_ids = re.findall(r"<ref>(.*?)</ref>", content)

        cited_sources = []
        id_to_url = {}

        for source in item["sources"]:
            if source["id"] in cited_ids:
                favicon = extract_favicon_url(source["source"])
                cited_sources.append({
                    "id": source["id"],
                    "title": source["title"],
                    "source": source["source"],
                    "favicon": favicon
                })
                id_to_url[source["id"]] = source["source"]

        def replace_ref(match):
            ref_id = match.group(1)
            link = id_to_url.get(ref_id)
            if link:
                return f"<a href='{link}'>[source]</a>"
            return ""  

        clean_content = re.sub(r"<ref>(.*?)</ref>", replace_ref, content)

        output.append({
            "category": item["category"],
            "content": clean_content,
            "sources": cited_sources,
        })

    return output
