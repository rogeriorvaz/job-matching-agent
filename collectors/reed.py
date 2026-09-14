from typing import Any
from playwright.async_api import Browser
from .base import JobCollector


class ReedCollector(JobCollector):
    source = "reed"

    def __init__(self, browser: Browser):
        self.browser = browser

    async def search(self, query: str, location: str) -> list[dict[str, Any]]:
        return []

    async def extract_job(self, url: str) -> dict[str, Any]:
        return {"source": self.source, "url": url}
