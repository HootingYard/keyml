# 'The Big Book of Key'
#
BOOK=bigbook
DATA=.
CODE=../../../greasepencil
OUTPUT=$(HOME)/Documents/hootingyard-books
WORKSPACE=$(HOME)/hootingyard-workspace
include $(CODE)/Makefile.inc

.phony :: update

ARCHIVE_URL = http://hootingyard.org/archives/category/prose
ARCHIVE     = $(WORKSPACE)/prose-archive
TEMPLATES   = $(CODE)/templates/xhtml

update : 
	mkdir -p $(DATA)
	mkdir -p $(DATA)/Images
	mkdir -p $(DATA)/Text
	mkdir -p $(DATA)/Styles
#	cp $(TEMPLATES)/index.html  $(DATA)/
#	cp $(TEMPLATES)/style.css   $(DATA)/Styles/
#	cp $(TEMPLATES)/title.xhtml $(DATA)/Text/
#	cp $(TEMPLATES)/cover.png   $(DATA)/
#	cp $(TEMPLATES)/bigbookinfo.json $(DATA)/bookinfo.json
	python $(CODE)/update-big-book.py $(ARCHIVE) $(DATA) $(CODE)
	cd $(DATA)/Text ; tidy --tidy-mark no -utf8 -modify -indent -wrap 1000000 -quiet * || exit 0

download :
	mkdir -p $(ARCHIVE)
	rm -f prose-*.html
	python $(CODE)/download-prose-archive.py $(ARCHIVE_URL) $(ARCHIVE)
