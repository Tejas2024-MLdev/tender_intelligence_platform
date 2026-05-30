from fastapi import APIRouter
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from backend.db.session import get_db

router = APIRouter()


@router.get("/db-check")
async def db_check(
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(text("SELECT 1"))
    return {"result": result.scalar()}