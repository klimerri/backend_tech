from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src import database, models
from src.api import user, client, engineer, engineering_skill, location, request, skill, task, task_type

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)
app.include_router(client.router)
app.include_router(engineer.router)
app.include_router(engineering_skill.router)
app.include_router(location.router)
app.include_router(request.router)
app.include_router(skill.router)
app.include_router(task.router)
app.include_router(task_type.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
