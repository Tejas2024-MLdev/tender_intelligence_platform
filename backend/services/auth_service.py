from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from backend.core.security import (
    verify_password,
)

from backend.models.organization import Organization
from backend.models.user import User
from backend.core.security import (
    hash_password,
    create_access_token,
)


class AuthService:

    @staticmethod
    async def register_user(
        db: AsyncSession,
        organization_name: str,
        email: str,
        password: str,
    ):

        existing_user = await db.execute(
            select(User).where(
                User.email == email
            )
        )

        if existing_user.scalar_one_or_none():
            raise ValueError(
                "Email already registered"
            )

        organization = Organization(
            name=organization_name
        )

        db.add(organization)

        await db.flush()

        user = User(
            organization_id=organization.id,
            email=email,
            hashed_password=hash_password(password),
        )

        db.add(user)

        await db.commit()

        await db.refresh(user)

        token = create_access_token(
            user_id=str(user.id),
            organization_id=str(
                organization.id
            ),
        )

        return token
    @staticmethod
    async def login_user(
    db: AsyncSession,
    email: str,
    password: str,
    ):

        result = await db.execute(
            select(User).where(
            User.email == email
            )
        )

        user = result.scalar_one_or_none()

        if not user:
            raise ValueError(
                "Invalid credentials"
            )

        if not verify_password(
            password,
            user.hashed_password
        ):
            raise ValueError(
                "Invalid credentials"
            )

        token = create_access_token(
            user_id=str(user.id),
            organization_id=str(
                user.organization_id
            )
        )

        return token