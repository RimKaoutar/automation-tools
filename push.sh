#!/bin/bash

# Script to automate Git add, commit, and push

# Check if a commit message is provided as an argument
if [ $# -eq 0 ]; then
  echo "Please provide a commit message."
  exit 1
fi

# Add all changes
git add .

# Commit with the provided message
git commit -m "$1"

# Push to the default remote branch (origin and current branch)
git push origin HEAD

# You can also specify a specific remote branch to push to:
# git push <remote_name> <branch_name>

# Exit script
exit 0

