latexfile = marking

all: $(latexfile).pdf

$(latexfile).pdf : $(latexfile).tex vc.tex
	while (pdflatex $(latexfile) ; \
	grep -q "Rerun to get cross" $(latexfile).log ) do true ; \
	done
