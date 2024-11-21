import re
from datetime import datetime

from sqlalchemy import func
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
    AsyncAttrs,
)
from sqlalchemy.orm import DeclarativeBase, declared_attr, Mapped, mapped_column

from core.settings import settings


class Base(AsyncAttrs, DeclarativeBase):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        return re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()


class CreatedModifiedMixin:
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    modified_at: Mapped[datetime] = mapped_column(
        server_default=func.now(), server_onupdate=func.now()
    )


class CommonMixin:
    id: Mapped[int] = mapped_column(primary_key=True)


engine = create_async_engine(settings.database_uri, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session() -> AsyncSession:
    async with AsyncSessionLocal() as async_session:
        yield async_session
