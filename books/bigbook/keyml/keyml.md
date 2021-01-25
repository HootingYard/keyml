# KeyML

The *Big Book of Key* archive and Hooting Yard ebook source files are stored as _KeyML_. KeyML is a subset of XHTML 1.1 that can represent any text from the Hooting Yard blog, can be used in an EPUB 2.1, and contains sufficient information for translation into LaTeX to create print books. 

The __keyml.py__ script tests that XHTML files:

1. match a DTD, typically __keyml.dtd__;

2. pass a set of Schematron tests, typically in __keyml.sch__;

3. contain no broken relative links;

4. do not link to broken image files.

