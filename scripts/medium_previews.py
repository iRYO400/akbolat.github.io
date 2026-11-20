#!/usr/bin/env python3
"""Snapshot the opening of each Medium post into data/medium.json.

A post page whose body is only a medium.com link shows this opening, faded out, above
"Read on Medium". Rerun after publishing or editing a Medium post:

    python3 scripts/medium_previews.py

The feed (medium.com/feed/@iRYO400) carries the full text of the latest posts only, so
entries already in data/medium.json are kept when a post drops out of the feed.
"""
import html
import json
import pathlib
import re
import urllib.request
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

FEED = "https://medium.com/feed/@iRYO400"
OUT = pathlib.Path(__file__).resolve().parent.parent / "data" / "medium.json"
WORDS = 90          # stop the opening once it has this many words
FIGURES = 1         # at most this many pictures in it
ALLOWED = {"p", "a", "strong", "em", "code", "br", "ul", "ol", "li", "blockquote", "figure", "img", "figcaption"}
BLOCK = re.compile(r"<(figure|p|h3|h4|pre|ul|ol|blockquote)\b[^>]*>.*?</\1>", re.S)


class Clean(HTMLParser):
    """Keeps text and a few tags; links keep href, pictures keep src and alt."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []

    def handle_starttag(self, tag, attrs):
        if tag not in ALLOWED:
            return
        a = dict(attrs)
        if tag == "a" and a.get("href"):
            self.out.append(f'<a href="{html.escape(a["href"])}">')
        elif tag == "img" and a.get("src"):
            self.out.append(f'<img src="{html.escape(a["src"])}" alt="{html.escape(a.get("alt") or "")}" loading="lazy" referrerpolicy="no-referrer">')
        elif tag not in ("a", "img"):
            self.out.append(f"<{tag}>")

    def handle_endtag(self, tag):
        if tag in ALLOWED and tag not in ("img", "br"):
            self.out.append(f"</{tag}>")

    def handle_data(self, data):
        self.out.append(html.escape(data, quote=False))


def clean(fragment):
    c = Clean()
    c.feed(fragment)
    return "".join(c.out)


def words(fragment):
    return len(re.sub(r"<[^>]+>", " ", fragment).split())


def opening(content):
    parts, count, figures = [], 0, 0
    for i, m in enumerate(BLOCK.finditer(content)):
        tag, block = m.group(1), m.group(0)
        if tag in ("figure", "h3", "h4") and not parts:
            continue                      # the cover and the subtitle: the post page shows its own
        if tag in ("pre", "h3", "h4") or "<pre" in block:
            break                         # code and the first subheading end the opening
        if tag == "figure":
            if figures == FIGURES:
                break
            figures += 1
        parts.append(clean(block))
        count += words(block) if tag != "figure" else 0
        if count >= WORDS:
            break
    return "\n".join(parts)


def main():
    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0"})
    root = ET.fromstring(urllib.request.urlopen(req, timeout=30).read())
    ns = {"content": "http://purl.org/rss/1.0/modules/content/"}
    data = json.loads(OUT.read_text()) if OUT.exists() else {}
    for item in root.iter("item"):
        link = item.findtext("link").split("?")[0]
        post_id = link.rsplit("-", 1)[-1]
        content = item.find("content:encoded", ns).text or ""
        data[post_id] = {
            "url": link,
            "title": item.findtext("title"),
            "minutes": max(1, round(words(content) / 230)),
            "excerpt": opening(content),
        }
        print(f"{post_id}  {data[post_id]['minutes']} min  {words(data[post_id]['excerpt'])} words  {data[post_id]['title'][:60]}")
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
