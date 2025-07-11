# Smart Reading Inbox

Smart Reading Inbox is a web app that helps you summarize articles using AI: Paste a URL and get a summary.

---

## Components

* Frontend (vanilla JS)
* FastAPI backend (deployed on Render)
* Frontend deployed via GitHub Pages

## Project structure

smart-reading-inbox/
- frontend/ # HTML + JS frontend (static)
- backend/ # FastAPI backend
- .gitignore
- README.md
- requirements.txt

## Getting Started (Local Setup)

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/smart-reading-inbox.git
cd smart-reading-inbox
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` folder with your OpenAI key:

```env
OPENAI_API_KEY=your-key-here
```

Start the server:

```bash
uvicorn main:app --reload
```

### 3. Frontend Setup

Just open `frontend/index.html` in a browser.
Make sure your FastAPI server is running locally on `localhost:8000`.

---

## Deployment

### Backend (Render)

* Connect your repo to [Render](https://render.com/)
* Add environment variable: `OPENAI_API_KEY`
* Use `main:app` as the entry point
* Use a production-ready `main_live.py` if needed

### Frontend (GitHub Pages)

* Push frontend files to a separate branch (e.g. `gh-pages`) or use root for a simple setup
* Enable Pages in GitHub repo settings

---

## Notes

* `.env` is ignored via `.gitignore`
* Avoid exposing secrets in frontend JS

---

## License

MIT

