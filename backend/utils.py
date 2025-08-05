import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("uvicorn.error")
## NOTE - I cannot extract the favicons from the gov and police websites as they are forbidden, even with headers to mimic browsers. Error logic has been applied to them
def extract_favicon_url(page_url: str) -> str | None:
    """
    Extracts the favicon URL from the webpage,
    Falls back to /favicon.ico if there's no link found
    """
    
    logger.info(f"Extracting favicon from: {page_url}")
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    }
    try:
        response = httpx.get(page_url, timeout=5.0, headers=headers)
        response.raise_for_status()
    except Exception as e:
        print(f"[utils.py] Failed to fetch page: {page_url} | Error: {e}")
        return fallback_favicon(page_url)

    soup = BeautifulSoup(response.text, "html.parser")
    
    icon_link = (
        soup.find("link", rel="icon")
        or soup.find("link", rel="shortcut icon")
        or soup.find("link", rel="apple-touch-icon")
    )

    if icon_link and icon_link.get("href"):
        href = icon_link["href"]
        icon_url = href if bool(urlparse(href).netloc) else urljoin(page_url, href)
        try:
            icon_resp = httpx.get(icon_url, timeout=5.0, headers=headers)
            icon_resp.raise_for_status()
        except Exception as e:
            logger.warning(f"Icon URL not reachable or forbidden, falling back: {icon_url} | Error: {e}")
            return fallback_favicon(page_url)
        return icon_url
   
    return fallback_favicon(page_url)


def fallback_favicon(page_url: str) -> str:
    """
    Builds default /favicon.ico path from base domain if all else fails
    """
    parsed = urlparse(page_url)
    #particular case for the police website - gives 403 forbidden so cannot access
    if "police.uk" in parsed.netloc:
        return "https://www.citizensadvice.org.uk/favicon.ico"
    
    return f"{parsed.scheme}://{parsed.netloc}/favicon.ico"
