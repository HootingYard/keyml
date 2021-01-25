from lxml.html import XHTMLParser, tostring
from lxml.html import parse
from pathlib import Path
from datetime import datetime
from unidecode import unidecode
import re

def soup_committee_id(date: datetime, title: str) -> str:
    """Create a canonical identifier for one of Frank Key's works.
        An ISO date followed by the title, in lowercase with accents
        and punctuation removed, with all words separated by dashes.
        Example: "2004-03-19-what-is-hooting-yard".
    :param date: date of first publication
    :param title: title of work
    :return: the identifier
    """
    s = unidecode(title)  # remove accents
    s = re.sub(r"\b'\b", "", s)  # remove apostrophes
    s = s.lower().replace("&", "and")  # keep  the "&" sign
    s = re.sub(r"\W+", " ", s)  # remove punctuation, shrink whitespace
    s = s.strip().replace(" ", "-")  # replace spaces with "-"
    return date.strftime("%Y-%m-%d") + "-" + s  # prepend ISO date

Text = Path('~/books-in-keyml/hooting-yard-home-page/Text').expanduser()

date = datetime(2003,1,1)

new_names = {}

for file in Text.glob('*.xhtml'):
    text = file.read_text()
    title = re.search(r'<title>(.+?)</title>', text)[1]
    new_names[file.name] = soup_committee_id(date, title) + '.xhtml'
    new_names['toc.xhtml'] = 'toc.xhtml'
    new_names['foreword.xhtml'] = 'foreword.xhtml'

def sub(match):
    name = match[1]
    new_name = new_names.get(name, name)
    return f'href="{new_name}"'

for file in Text.glob('*.xhtml'):
    text = file.read_text()
    text = re.sub(r'href="(.+?)"', sub, text)
    if file.name == 'toc.xhtml':
        print(text)
    #file.write_text(text)
    #file.rename(file.parent / new_names[file.name])
