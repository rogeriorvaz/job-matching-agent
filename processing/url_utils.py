from urllib.parse import urlsplit, urlunsplit


def canonicalise_url(url: str) -> str:
    parts = urlsplit(url)
    return urlunsplit((parts.scheme, parts.netloc, parts.path.rstrip("/"), "", ""))
