import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse



def extract_favicon_url(page_url: str) -> str | None:
    """
    Extracts the favicon URL from the webpage,
    Falls back to /favicon.ico if there's no <link> found,
    Returns None if request completely fails
    """

    try:
        response = httpx.get(page_url, timeout=5.0)
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
        absolute_url = urljoin(page_url, href)
        return absolute_url

   
    return fallback_favicon(page_url)


def fallback_favicon(page_url: str) -> str:
    """
    Builds default /favicon.ico path from base domain if all else fails
    """
    parsed = urlparse(page_url)
    return f"{parsed.scheme}://{parsed.netloc}/favicon.ico"
