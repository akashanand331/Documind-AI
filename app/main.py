from fastapi import FastAPI

app = FastAPI(
    title="DocuMind AI",
    description="AI document chatbot using Retrieval-Augmented Generation",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "message": "Welcome to DocuMind AI",
        "status": "running",
    }


@app.get("/health")
def health():
    return {"status": "ok"}