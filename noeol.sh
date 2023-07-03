#!/bin/bash

if [ $# -eq 0 ]; then
  echo "No arguments provided."
  exit 1
fi

filename="$1"
perl -pi -e 'chomp if eof' "$filename"

