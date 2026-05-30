from fastapi import APIRouter

from backend.schemas.search import (
    SearchRequest,
)

from backend.services.rag.search_service import (
    SearchService,
)

router = APIRouter(
    prefix="/search",
    tags=["Search"],
)


@router.post("")
async def search(
    payload: SearchRequest,
):

    return SearchService.search(
        payload.query
    )