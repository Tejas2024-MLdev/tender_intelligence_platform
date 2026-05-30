from fastapi import APIRouter

from backend.schemas.chat import (
    ChatRequest,
)

from backend.services.rag.rag_service import (
    RAGService,
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post("")
async def chat(
    payload: ChatRequest,
):

    return RAGService.ask(
        payload.question
    )