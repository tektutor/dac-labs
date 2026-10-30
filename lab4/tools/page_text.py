"""Print the visible text of a built HTML page, or of one section of it.

Usage:
    python tools/page_text.py PAGE.html

    python tools/page_text.py PAGE.html "Heading"

Each table row prints on one line, with " | " between the cells.
"""

import re
import sys
from html.parser import HTMLParser

HEADINGS = {"h1", "h2", "h3", "h4"}
BLOCKS = HEADINGS | {"p", "tr", "li", "dt", "dd", "pre", "table", "div"}
SKIP = {"script", "style", "nav", "footer", "header"}

class TextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.in_headerlink = False
        self.cells = 0
        self.started = False
        self.lines = []         # list of [text, is_heading]

    def new_line(self, heading=False):
        self.lines.append(["", heading])

    def handle_starttag(self, tag, attrs):
        classes = dict(attrs).get("class") or ""
        if tag in SKIP:
            self.skip += 1
            return
        if tag == "a" and "headerlink" in classes:
            self.in_headerlink = True
            return
        if tag == "h1":
            self.started = True
        if tag in ("td", "th"):
            if self.cells:
                self.lines[-1][0] += " | "
            self.cells += 1
        elif tag == "tr":
            self.cells = 0
            self.new_line()
        elif tag in BLOCKS and not self.cells:
            self.new_line(tag in HEADINGS)

    def handle_endtag(self, tag):
        if tag in SKIP:
            self.skip -= 1
        elif tag == "a":
            self.in_headerlink = False
        elif tag == "tr":
            self.cells = 0
            self.new_line()

    def handle_data(self, data):
        if self.skip or self.in_headerlink or not self.started or not self.lines:
            return
        text = " ".join(data.split())
        if text:
            self.lines[-1][0] += " " + text

def main():
    parser = TextParser()
    with open(sys.argv[1], encoding="utf-8") as handle:
         parser.feed(handle.read())
    lines = []
    for text, head in parser.lines:
        text = re.sub(r"\s+([;,:.)])", r"\1", " ".join(text.split()))
        if text:
           lines.append((text, head))
    if len(sys.argv) > 2:
        wanted = sys.argv[2]
        starts = [i for i, (text, head) in enumerate(lines) if head and text == wanted]
        if not starts:
           sys.exit(f"heading not found: {wanted}")
           start = starts[0]
           end = next((i for i in range(start + 1, len(lines)) if lines[i][1]), len(lines))
           lines = lines[start:end]
    for text, _ in lines:
        print(text)

if __name__ == "__main__":
   main()
