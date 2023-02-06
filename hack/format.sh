#!/usr/bin/env bash

set -o nounset
set -o pipefail
set -o errexit
set -o xtrace

find . -name '*.py' -exec autopep8 --max-line-length 120 -i {} \;
