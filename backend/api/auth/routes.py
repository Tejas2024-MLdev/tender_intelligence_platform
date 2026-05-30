# from fastapi import APIRouter

# router = APIRouter(
#     prefix="/auth",
#     tags=["Authentication"]
# )


# @router.get("/ping")
# async def ping():
#     return {
#         "message": "auth service running"
#     }

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException


from sqlalchemy.ext.asyncio import AsyncSession

from backend.db.session import get_db
from backend.schemas.user import (
    RegisterUserRequest,
    TokenResponse,
)
from backend.services.auth_service import (
    AuthService,
)

from backend.schemas.user import (
    LoginRequest,
)


from backend.core.dependencies import (
    get_current_user,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=TokenResponse
)
async def register(
    payload: RegisterUserRequest,
    db: AsyncSession = Depends(get_db),
):

    try:

        token = await (
            AuthService.register_user(
                db=db,
                organization_name=payload.organization_name,
                email=payload.email,
                password=payload.password,
            )
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    
@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    payload: LoginRequest,
    db: AsyncSession = Depends(get_db),
):

    try:

        token = await (
            AuthService.login_user(
                db=db,
                email=payload.email,
                password=payload.password,
            )
        )

        return TokenResponse(
            access_token=token
        )

    except ValueError as e:

        raise HTTPException(
            status_code=401,
            detail=str(e)
        )    

@router.get("/me")
async def me(
    current_user=Depends(
        get_current_user
    )
):

    return {
        "user_id": current_user["sub"],
        "organization_id": current_user[
            "organization_id"
        ]
    }    



