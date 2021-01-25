from<titlwe pathlib import Path
import re

AND = {str(file) for file in Path('.').glob('*-and-*.xhtml')}

for file in Path('.').glob('*-n-*.xhtml'):
     if file.name == '2006-02-08-n-is-for-night.xhtml':
         continue
     s = str(file).replace('-n-', '-and-')
     if s in AND:
         file.unlink()
     else:
         file.rename(Path(s))

HREF = re.compile(r'href="(.*?-n-.*?)"')

for file in Path('.').glob('*.xhtml'):
    text = file.read_text()
    p = False
    for match in HREF.finditer(text):
        if not p:
            print(file)
            p = True
        print('\t', match[1])
        


