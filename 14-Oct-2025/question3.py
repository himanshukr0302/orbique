import re
import requests
from bs4 import BeautifulSoup


def scrape_bird_habitats(url):
    """Return list of (bird_name, habitat) pairs found on the page.

    This targets pages where bird names are in <strong> tags inside
    paragraphs under a <div class="content">. It's forgiving if structure
    varies slightly.
    """
    resp = requests.get(url, headers={"User-Agent": "bird-scraper"}, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    results = []
    content_div = soup.find("div", class_="content") or soup

    for p in content_div.find_all("p"):
        strong = p.find(["strong", "b"]) or p.find("span", class_="bold")
        if not strong:
            continue

        bird_name = strong.get_text().strip().rstrip(":")
        full = p.get_text(separator=" ", strip=True)
        habitat_raw = full.replace(strong.get_text(), "", 1)
        habitat = re.sub(r"^[\s:–—-]+|[\s:–—-]+$", "", habitat_raw)
        habitat = re.sub(r"\s+", " ", habitat)

        if bird_name and habitat:
            results.append((bird_name, habitat))

    return results


if __name__ == "__main__":
    url = (
        "https://www.orchidsinternationalschool.com/science-concepts/"
        "structure-and-habitat-of-birdss"
    )
    try:
        birds = scrape_bird_habitats(url)
    except Exception as e:
        print("Error fetching or parsing page:", e)
        raise

    if not birds:
        print("No birds found.")
    else:
        for name, habitat in birds:
            print(f"{name} — {habitat}")
