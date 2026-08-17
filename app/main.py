from datetime import UTC, datetime
from enum import StrEnum
from uuid import uuid4

from fastapi import FastAPI
from pydantic import BaseModel, Field, HttpUrl


class Status(StrEnum):
    SAVED = "saved"
    APPLIED = "applied"
    INTERVIEW = "interview"
    REJECTED = "rejected"


class JobCreate(BaseModel):
    title: str = Field(min_length=2, max_length=200)
    company: str = Field(min_length=2, max_length=200)
    url: HttpUrl
    description: str = Field(min_length=20, max_length=30_000)
    source: str = Field(default="manual", max_length=50)


class Job(JobCreate):
    id: str
    status: Status = Status.SAVED
    matched_skills: list[str]
    created_at: datetime


SKILLS = (
    "python",
    "fastapi",
    "flask",
    "django",
    "sql",
    "postgresql",
    "docker",
    "aws",
    "react",
    "typescript",
    "pytorch",
    "tensorflow",
    "nlp",
    "llm",
    "rag",
    "playwright",
)
jobs: dict[str, Job] = {}


def match_skills(description: str, profile: set[str]) -> list[str]:
    lowered = description.lower()
    return [skill for skill in SKILLS if skill in profile and skill in lowered]


def create_app() -> FastAPI:
    app = FastAPI(title="Job Tracker Automation", version="0.1.0")

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok", "service": "job-tracker-automation"}

    @app.post("/api/v1/jobs", response_model=Job, status_code=201)
    async def add_job(payload: JobCreate) -> Job:
        profile = {
            "python",
            "fastapi",
            "sql",
            "docker",
            "aws",
            "react",
            "typescript",
            "llm",
            "rag",
            "playwright",
        }
        job = Job(
            id=str(uuid4()),
            matched_skills=match_skills(payload.description, profile),
            created_at=datetime.now(UTC),
            **payload.model_dump(),
        )
        jobs[job.id] = job
        return job

    @app.patch("/api/v1/jobs/{job_id}/status", response_model=Job)
    async def update_status(job_id: str, status: Status) -> Job:
        job = jobs[job_id]
        updated = job.model_copy(update={"status": status})
        jobs[job_id] = updated
        return updated

    @app.get("/api/v1/jobs", response_model=list[Job])
    async def list_jobs() -> list[Job]:
        return list(jobs.values())

    return app


app = create_app()
