from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
from summarizer import fetch_article_text, summarize_text 

app = FastAPI()

class URLRequest(BaseModel):
    url: str
    
@app.post("/summarize")
async def summarize (request: URLRequest):
    try:
        article_text = fetch_article_text(request.url)
        summary = summarize_text(article_text)
        return {"summary":summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))