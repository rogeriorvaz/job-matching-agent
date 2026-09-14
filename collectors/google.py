from typing import Any
from urllib.parse import quote_plus

from playwright.async_api import Browser
from .base import JobCollector


class GoogleCollector(JobCollector):
    source = "google"

    def __init__(self, browser: Browser):
        self.browser = browser

    async def search(self, query: str, location: str) -> list[dict[str, Any]]:
        page = await self.browser.new_page()
        try:
            search = f'"{query}" jobs "{location}"'
            url = "https://www.google.com/search?q=" + quote_plus(search)
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)

            results = []
            for link in await page.locator("a").all():
                href = await link.get_attribute("href")
                text = (await link.inner_text()).strip()
                if href and text and href.startswith("http"):
                    results.append({
                        "source": self.source,
                        "title": text,
                        "url": href,
                        "search_term": query,
                    })
            return results
        finally:
            await page.close()

    async def extract_job(self, url: str) -> dict[str, Any]:
        page = await self.browser.new_page()
        try:
            await page.goto(url, wait_until="domcontentloaded", timeout=30000)
            return {
                "source": self.source,
                "title": await page.title(),
                "description": await page.locator("body").inner_text(),
                "url": url,
            }
        finally:
            await page.close()
