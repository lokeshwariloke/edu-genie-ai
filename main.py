from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations


BASE_DIR = Path(__file__).resolve().parent


app = FastAPI(
    title="EduGenie - Google Gemini Powered Learning Assistant",
    version="1.0.0",
    description="AI-powered educational assistant built with FastAPI and Gemini."
)


# Static files
app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


# HTML templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# -----------------------------
# Request Models
# -----------------------------

class TextRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        max_length=20000
    )


class TopicRequest(BaseModel):
    topic: str = Field(
        ...,
        min_length=1,
        max_length=500
    )


# -----------------------------
# Home Page
# -----------------------------

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "title": "EduGenie"
        }
    )


# -----------------------------
# Health Check
# -----------------------------

@app.get("/health")
async def health():

    return {
        "status": "ok",
        "service": "EduGenie"
    }


# -----------------------------
# Question Answering
# -----------------------------

@app.post("/qa")
async def qa(payload: TextRequest):
    try:
        answer = answer_question(payload.text)
        return {"answer": answer}
    except Exception as e:
        return {"answer": f"Gemini Error: {str(e)}"}


# -----------------------------
# Explain Topic
# -----------------------------

@app.post("/explain")
async def explain(payload: TopicRequest):
    try:
        explanation = explain_topic(payload.topic)
        return {"explanation": explanation}
    except Exception as e:
        return {"explanation": f"Gemini Error: {str(e)}"}
    


# -----------------------------
# Generate Quiz
# -----------------------------

@app.post("/quiz")
async def quiz(payload: TextRequest):

    quiz_data = generate_quiz(payload.text)

    return {
        "quiz": quiz_data
    }


# -----------------------------
# Summarization
# -----------------------------

@app.post("/summarize")
async def summarize(payload: TextRequest):
    try:
        summary = summarize_text(payload.text)
        return {"summary": summary}
    except Exception as e:
        return {"summary": f"Gemini Error: {str(e)}"}


# -----------------------------
# Learning Recommendations
# -----------------------------

@app.post("/learn/recommendations")
async def learning_recommendations(payload: TopicRequest):

    recommendations = get_learning_recommendations(
        payload.topic
    )

    return {
        "recommendations": recommendations
    }