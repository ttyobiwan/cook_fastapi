from fastapi import APIRouter

router = APIRouter(tags=["internal"])


@router.get("/health")
def check_health() -> dict:
    """Check health of the app."""
    return {"status": "ok"}
