#!/bin/sh
set -e

status=0

for tex in $(git ls-files '*.tex'); do
  echo "Linting $tex"
  # -q reduces noise, exit code non-zero if issues found
  if ! chktex -q "$tex"; then
    status=1
  fi
  echo
done

exit $status
