#!/bin/bash
# Sends a JSON POST req to a URL passed as the first arg; displays the body of the res
curl -sH "Content-Type: application/json" -d "$(cat "$2")" "$1"
