latexfile = collatz81

all: $(latexfile).pdf

$(latexfile).pdf : $(latexfile).tex 
	while (pdflatex $(latexfile) ; \
	grep -q "Rerun to get cross" $(latexfile).log ) do true ; \
	done
