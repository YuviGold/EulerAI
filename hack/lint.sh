#!/usr/bin/env bash

set -o nounset
set -o pipefail
set -o errexit
set -o xtrace

python -m flake8 --max-line-length 120
find . -name '*.sh' -type f -not -path "./.git/*" -exec shellcheck {} +
git diff --shortstat --exit-code
