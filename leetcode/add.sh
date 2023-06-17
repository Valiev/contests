#!/bin/zsh

nvim "$(echo "$@" | tr ' ' '_' | tr -d '.').py"
