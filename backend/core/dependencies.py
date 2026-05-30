from fastapi import Depends
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security import HTTPBearer

from backend.core.security import decode_access_token

security = HTTPBearer()


# async def get_current_user(
#     credentials: HTTPAuthorizationCredentials = Depends(security)
# ):

#     token = credentials.credentials

#     payload = decode_access_token(token)

#     if not payload:

#         raise HTTPException(
#             status_code=401,
#             detail="Invalid token"
#         )

#     return payload



async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    print("CREDENTIALS:", credentials)

    token = credentials.credentials

    print("TOKEN:", token)

    payload = decode_access_token(token)

    print("PAYLOAD:", payload)

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload