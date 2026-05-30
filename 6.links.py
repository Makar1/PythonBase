import datetime
from datetime import date
import logging


from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

def _extract_hrefs(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="accordeon-inner__item-title link xls")
    return [link.get("href") for link in links if link.get("href")]


def _parse_date_from_href(href: str) -> date | None:
    try:
        raw = href.split("oil_xls_")[1][:8]
        return datetime.datetime.strptime(raw, "%Y%m%d").date()
    except Exception as e:
        logger.warning(f"Не удалось извлечь дату из ссылки {href}: {e}")
        return None


def _normalize_url(href: str) -> str:
    if href.startswith("http"):
        return href
    return f"https://spimex.com{href}"


def parse_page_links(html: str, start_date: date, end_date: date) -> list[tuple[str, date]]:
    results = []
    for href in _extract_hrefs(html):
        href = href.split("?")[0]
        if "/upload/reports/oil_xls/oil_xls_" not in href or not href.endswith(".xls"):
            continue
        file_date = _parse_date_from_href(href)
        if file_date is None:
            continue
        if start_date <= file_date <= end_date:
            results.append((_normalize_url(href), file_date))
        else:
            logger.debug(f"Ссылка {href} вне диапазона дат")
    return results