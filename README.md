# Sample Recipe Book

This repository provides a LaTeX template for building a printable collection of recipes. Replace the sample files under `recipes/` with your own dishes and organise them into chapters of your choosing.

## Building

You need the `latexmk` build tool and a LaTeX distribution. On Ubuntu systems you can install both with:

```bash
sudo apt-get install latexmk texlive-full
```

On Gentoo you can emerge the same tools with:

```bash
sudo emerge --ask app-text/texlive dev-tex/latexmk
```

The `dev-texlive/texlive-mathscience` set provides the `siunitx` package used by some recipes.

If you prefer a lighter environment, install only the packages listed below:

```bash
sudo apt-get install make latexmk texlive-latex-extra texlive-fonts-recommended
make
```

The resulting `book.pdf` will contain a table of contents and an alphabetical index.

## Releasing

When you create a tag, GitHub Actions will build the PDF and attach it to a release automatically. The repository also includes a `.gitlab-ci.yml` file so the same can be done with GitLab CI.

## Coding Style

All `.tex` files use spaces for indentation with two spaces per level. This is enforced in the repository's `.editorconfig` so editors can apply the same formatting automatically. Continuous integration runs `chktex` to flag common formatting mistakes and also compiles each recipe individually to catch errors early.

## AI Agent Notes

If you use an AI coding assistant such as Codex to modify this repository, make sure to follow the guidelines in `AGENTS.md`. After editing recipes run:

```bash
scripts/check_formatting.sh
scripts/check_compile.sh
make
```

to verify formatting and compilation before committing your changes.
