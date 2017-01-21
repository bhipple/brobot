#!/usr/bin/env bash
echo "Checking for tabs and trailing whitespace."
git diff origin/master --check
