#!/bin/bash
# takes in a URL, sends a req to it, & displays the size of the body of the res

curl -s "$1" | wc -c
