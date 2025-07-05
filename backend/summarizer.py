import os
from dotenv import load_dotenv
from openai import OpenAI
from newspaper import Article 

# Load environment variables from .env file
load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Function to summarize an article given its URL
def fetch_article_text(url : str) -> str:
    article = Article(url)
    
    article.download()
    article.parse()
    return article.text

def summarize_text(text:str) ->str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes articles."},
            {"role": "user", "content": f"Please summarize the following article content:\n{text}"}
        ],
        max_tokens=300,  # Adjust as needed
        temperature=0.7  # Adjust as needed
    )
    return response.choices[0].message.content.strip() 

