import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.learning_path import router as learning_path_router

app = FastAPI(title="Course Forge Backend API", version="1.0")

# =========================================================================
# Configure CORS Middleware so your React frontend can communicate safely
# =========================================================================
allowed_origins = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:5173,http://127.0.0.1:5173"
).split(",")

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount your learning path router to the app workspace, prepending "/api" to all its endpoints.
app.include_router(learning_path_router, prefix="/api")

# Define a baseline GET endpoint at the absolute root URL to handle simple connectivity health checks.
@app.get("/")
def health_check():
    return {"status": "healthy", "message": "Course Forge API is running smoothly!"}