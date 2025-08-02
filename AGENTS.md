# Development Rules

The repository builds a LaTeX recipe book. When updating recipes or other files, follow these rules:

1. **Recipe structure**: Each `.tex` file in `recipes/` must start with `\section{...}\label{sec:...}\index{...}` and end with `\clearpage`. Use `\subsection*{Ingredients}` and `\subsection*{Method}`.
2. **Book index**: After adding or renaming recipes, run:
   ```bash
   python scripts/generate_alphabetical_list.py
   ```
   to refresh `recipes/appendix/alphabetical_list.tex`.
3. **Compilation checks**: Ensure formatting and compilation succeed by running:
   ```bash
   scripts/check_formatting.sh
   scripts/check_compile.sh
   make
   ```
4. **book.tex updates**: Add new recipes to `book.tex` in the relevant chapter so no files remain orphaned.
5. **Indentation**: Two spaces per level. `.editorconfig` enforces this.
6. **Cover page**: The cover is generated with LaTeX; no external image is required.
7. **Pull requests**: Describe your change and confirm that the checks above were run successfully.
