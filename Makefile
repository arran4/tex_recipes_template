TEXFILE=book.tex
PDF=$(TEXFILE:.tex=.pdf)

all: $(PDF)

$(PDF): $(TEXFILE)
	latexmk $(TEXFILE)

clean:
	latexmk -C

.PHONY: all clean
