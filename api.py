from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from analysis import analyze_complaint

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ComplaintRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "API is running 🚀"}

@app.post("/analyze")
def analyze(request: ComplaintRequest):
    return analyze_complaint(request.text)