from fastapi import FastAPI

app = FastAPI(
    title="AI Citizen Services Agent",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "citizen-ai-agent",
    }