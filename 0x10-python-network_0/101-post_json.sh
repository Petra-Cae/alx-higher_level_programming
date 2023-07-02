#!/bin/bash
# Sends a JSON POST req to a URL passed as the first arg,
# and displays the body of the res

curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
