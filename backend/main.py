from fastapi import FastAPI

from backend.core.config import settings

from backend.api.auth.routes import router as auth_router

from backend.services.storage.minio_service import (
    MinioService,
)

from backend.services.rag.qdrant_service import (
    QdrantService,
)


from backend.api.documents.routes import (
    router as documents_router
)


from backend.api.search.routes import (
    router as search_router
)


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(auth_router)

app.include_router(documents_router)

QdrantService.create_collection()

app.include_router(
    search_router
)

@app.get("/")
async def root():
    return {
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }



@app.on_event("startup")
async def startup():

    MinioService.ensure_bucket()