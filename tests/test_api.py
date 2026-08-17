from fastapi.testclient import TestClient

from app.main import create_app, match_skills


def test_skill_matching_is_explainable() -> None:
    assert match_skills("Python FastAPI and Docker", {"python", "fastapi"}) == ["python", "fastapi"]


def test_job_lifecycle() -> None:
    with TestClient(create_app()) as client:
        created = client.post(
            "/api/v1/jobs",
            json={
                "title": "Backend Engineer",
                "company": "Acme",
                "url": "https://example.com/jobs/1",
                "description": "Build Python FastAPI services with PostgreSQL and Docker.",
            },
        )
        assert created.status_code == 201
        job_id = created.json()["id"]
        updated = client.patch(f"/api/v1/jobs/{job_id}/status?status=applied")
    assert updated.json()["status"] == "applied"
