#!/bin/sh
set -e

status=0

for tex in $(find recipes -name '*.tex' -type f | sort); do
  echo "Checking $tex"
  tmpdir=$(mktemp -d)
  cat > "$tmpdir/main.tex" <<EOT
\documentclass{book}
\usepackage[utf8]{inputenc}
\usepackage{amsmath}
\usepackage{makeidx}
\usepackage{graphicx}
\usepackage[margin=1in]{geometry}
\usepackage{hyperref}
\usepackage{underscore}
\usepackage{textcomp}
\usepackage{xspace}
\usepackage{siunitx}
\newcommand{\half}{\textonehalf\xspace}
\newcommand{\quarter}{\textonequarter\xspace}
\makeindex
\begin{document}
\input{$PWD/$tex}
\end{document}
EOT
  if ! (cd "$tmpdir" && pdflatex -interaction=nonstopmode -halt-on-error main.tex >/dev/null 2>&1); then
    echo "FAILED: $tex"
    status=1
  fi
  rm -rf "$tmpdir"
done

exit $status
