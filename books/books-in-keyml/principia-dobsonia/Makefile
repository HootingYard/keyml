# 'Principia Dobsonia'

HOOTINGYARD=$(abspath $(HOME)/Projects/HootingYard)

NAME=principia-dobsonia
BOOK=.
OUTPUT=$(HOOTINGYARD)/epubs
UBER=$(HOOTINGYARD)/ubercoordinator
WORKSPACE=$(HOOTINGYARD)/workspace
BIGBOOK=$(HOOTINGYARD)/bigbook

include $(UBER)/src/Makefile.inc

.PHONY: refresh

refresh: $(UBER)/src/prepare_book.py
	cp -f $(BOOK)/cover.png $(BOOK)/Images/
	python3 $(CODE)/src/prepare_book.py -e . -b $(BIGBOOK) -u $(UBER)


