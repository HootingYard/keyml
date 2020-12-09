# -*- coding: utf-8 -*-

import re, codecs, glob

def edit(filepath):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        text = f.read()
    text = re.sub(ur'<h1 id="(.+?)".*?>', ur'<h1 id="\1" class="center">', text)
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(text)
    

for filepath in glob.glob('[0-9]*.xhtml'):
    print filepath
    edit(filepath)
