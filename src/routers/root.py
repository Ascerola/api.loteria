from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from sqlalchemy import text

from db.conn import get_session

router = APIRouter()


@router.get("/")
async def root():
    try:
        with get_session() as session:
            session.execute(text("SELECT 1"))
        return {"message": "DB connection successful"}
    except Exception as exc:  # noqa: BLE001
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={"message": "DB connection failed", "detail": str(exc)},
        )
