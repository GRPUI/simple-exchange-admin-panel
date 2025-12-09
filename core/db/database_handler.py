from __future__ import annotations

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_sessionmaker,
)


class DatabaseHandler:
    """
    Async database handler for managing shop operations.
    """

    def __init__(self, url: str):
        self.url = url
        self.engine = create_async_engine(self.url, echo=False)
        self.sessionmaker = async_sessionmaker(
            self.engine, autoflush=False, autocommit=False, expire_on_commit=False
        )
