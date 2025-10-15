from __future__ import annotations
import argparse
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Tuple
import sys
import pathlib
import re
import html

URL = "https://books.toscrape.com/catalogue/category/books/science_22/index.html"
OUTFILE = pathlib.Path(__file__).parent / "books.txt"


def fetch_page(url: str) -> str:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.text


def parse_books(html_text: str) -> List[Tuple[str, float]]:
       
        soup = BeautifulSoup(html_text, "html.parser")
        items: List[Tuple[str, float]] = []
        for article in soup.select("article.product_pod"):
                # Title
                a = article.find("h3").find("a")
                title = a.get("title") or a.get_text(strip=True)

                # Price (format like "£51.77", but may contain stray chars/entities)
                price_tag = article.select_one("p.price_color")
                price_text = price_tag.get_text(strip=True) if price_tag else ""
                price = 0.0
                if price_text:
                        # Unescape HTML entities, then keep only digits, dots and commas
                        cleaned = html.unescape(price_text)
                        m = re.search(r"[\d\.,]+", cleaned)
                        if m:
                                num = m.group(0).replace(",", "")  # remove thousands separator
                                try:
                                        price = float(num)
                                except ValueError:
                                        price = 0.0

                items.append((title, price))
        return items


def save_to_txt(items: List[Tuple[str, float]], path: pathlib.Path) -> None:
        with path.open("w", encoding="utf-8") as f:
                for title, price in items:
                        f.write(f"{title} | {price:.2f}\n")


def load_into_dict(path: pathlib.Path) -> Dict[str, float]:
        data: Dict[str, float] = {}
        with path.open("r", encoding="utf-8") as f:
                for line in f:
                        parts = line.strip().rsplit("|", 1)
                        if len(parts) != 2:
                                continue
                        title = parts[0].strip()
                        try:
                                price = float(parts[1].strip())
                        except ValueError:
                                price = 0.0
                        # if duplicate title, append suffix to keep keys unique
                        key = title
                        suffix = 1
                        while key in data:
                                suffix += 1
                                key = f"{title} ({suffix})"
                        data[key] = price
        return data


def summarize(data: Dict[str, float], threshold: float) -> None:
        total_items = len(data)
        total_cost = sum(data.values())
        print(f"Total articles: {total_items}")
        print(f"Total cost: £{total_cost:.2f}")
        print()
        print(f"Threshold for rejection: £{threshold:.2f}")
        accepted = 0
        rejected = 0
        for title, price in data.items():
                status = "Rejected" if price > threshold else "Accepted"
                if status == "Rejected":
                        rejected += 1
                else:
                        accepted += 1
                print(f"{status:8} | £{price:7.2f} | {title}")
        print()
        print(f"Accepted: {accepted}, Rejected: {rejected}")


def main(argv=None):
        parser = argparse.ArgumentParser(description="Scrape books and prices, save to txt, summarize.")
        parser.add_argument("--url", "-u", default=URL, help="Page URL to scrape")
        parser.add_argument("--out", "-o", default=str(OUTFILE), help="Output txt file")
        parser.add_argument("--threshold", "-x", type=float, default=20.0, help="Reject if price > threshold")
        args = parser.parse_args(argv)

        try:
                html = fetch_page(args.url)
        except Exception as e:
                print(f"Error fetching {args.url}: {e}", file=sys.stderr)
                sys.exit(1)

        items = parse_books(html)
        outpath = pathlib.Path(args.out)
        save_to_txt(items, outpath)

        data = load_into_dict(outpath)
        summarize(data, args.threshold)


if __name__ == "__main__":
        main()