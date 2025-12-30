from fastapi import FastAPI
from app.routes.auth import router as auth_router
from app.routes.tasks import router as tasks_router

app = FastAPI(title="Task Management API", version="1.0.0")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tasks_router, tags=["tasks"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Management API"}