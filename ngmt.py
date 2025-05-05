from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

API_KEY = os.getenv("API_KEY")

categories = ["Genetics", "Medical AI", "Neuroscience", "BioTech"]
filters = ["Breakthroughs", "Opportunities", "Explainers"]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("news.html", {
        "request": request,
        "categories": categories,
        "filters": filters,
        "selected_category": "",
        "selected_filter": "",
        "articles": []
    })

@app.post("/get_news", response_class=HTMLResponse)
async def get_news(request: Request, category: str = Form(...), filter_type: str = Form(...)):
    query = f"{category} {filter_type} biomedical innovation"
    url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    articles = data.get("articles", [])[:10]

    return templates.TemplateResponse("news.html", {
        "request": request,
        "categories": categories,
        "filters": filters,
        "selected_category": category,
        "selected_filter": filter_type,
        "articles": articles
    })
