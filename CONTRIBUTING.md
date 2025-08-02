# Contributing Guide

This project builds a printable recipe book using LaTeX. All recipes live under the `recipes/` directory and must compile on their own before being included in `book.tex`.

## Coding Style

- Use spaces for indentation as configured in `.editorconfig`. Two spaces per level.
- Recipe files are written in LaTeX and end with `\clearpage` so each dish starts on a new page.
- Begin each recipe with a `\section{...}` followed by `\label{sec:...}` and `\index{...}`.
- Use `\subsection*{Ingredients}` and `\subsection*{Method}` with `itemize`/`enumerate` lists.

## Adding a Recipe

1. Place the new `.tex` file under the appropriate chapter directory inside `recipes/`.
2. Give it a unique `\label{sec:...}` so the index works correctly.
3. Run `python scripts/generate_alphabetical_list.py` to refresh `recipes/appendix/alphabetical_list.tex`.
4. Execute `scripts/check_compile.sh` to ensure every recipe compiles individually.
5. Run `make` to build `book.pdf` and verify there are no LaTeX errors.
6. Commit your changes and open a pull request.

Pull requests should include a short description of the recipe and confirm that the checks above have passed.
