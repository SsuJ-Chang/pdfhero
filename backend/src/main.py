from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.adapters.api import router as api_router

app = FastAPI(title="PDF Hero Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["Content-Disposition"],
)

app.include_router(api_router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "PDF Hero Backend is running"}
