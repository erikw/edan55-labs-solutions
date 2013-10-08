latexfile = independentset

all: $(latexfile).pdf

$(latexfile).pdf : $(latexfile).tex output.data
	while (pdflatex $(latexfile) ; \
	grep -q "Rerun to get cross" $(latexfile).log ) do true ; \
	done
clean:
	$(RM) $(latexfile).pdf
