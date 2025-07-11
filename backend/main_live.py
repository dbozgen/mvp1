from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from summarizer import fetch_article_text, summarize_text

app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/summarize")
async def summarize(request:dict):
    """
    Endpoint to summarize an article given its URL.
    Expects a JSON body with a 'url' field.
    """
    url = request.get("url")
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")
    try:
        text = fetch_article_text(url)
        summary = summarize_text(text)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))