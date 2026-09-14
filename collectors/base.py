from abc import ABC, abstractmethod
from typing import Any


class JobCollector(ABC):
    source: str

    @abstractmethod
    async def search(self, query: str, location: str) -> list[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    async def extract_job(self, url: str) -> dict[str, Any]:
        raise NotImplementedError
