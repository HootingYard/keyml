# 'The Big Book of Key'
#
BOOK=bigbook
DATA=.
CODE=../../code
OUTPUT=../../bookfiles
WORKSPACE=../../workspace

include $(CODE)/Makefile.inc

.phony :: update checkimages

ARCHIVE_URL = http://hootingyard.org/archives/category/prose
ARCHIVE     = $(WORKSPACE)/prose-archive
TEMPLATES   = $(CODE)/templates/xhtml

update : 
	mkdir -p $(DATA)
	mkdir -p $(DATA)/Images
	mkdir -p $(DATA)/Text
	mkdir -p $(DATA)/Styles
	cp $(TEMPLATES)/index.html  $(DATA)/
	cp $(TEMPLATES)/style.css   $(DATA)/Styles/
	cp $(TEMPLATES)/title.xhtml $(DATA)/Text/
	cp $(TEMPLATES)/cover.png   $(DATA)/
#	cp $(TEMPLATES)/bigbookinfo.json $(DATA)/bookinfo.json
	python $(CODE)/update-big-book.py $(ARCHIVE) $(DATA) $(CODE)
	cd $(DATA)/Text ; tidy --tidy-mark no -utf8 -modify -indent -wrap 1000000 -quiet * || exit 0

checkimages:
	python2.7 $(CODE)/check-bigbook-images.py $(DATA)

download :
	mkdir -p $(ARCHIVE)
	python $(CODE)/download-prose-archive.py $(ARCHIVE_URL) $(ARCHIVE)
