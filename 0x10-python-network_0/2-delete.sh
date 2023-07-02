#!/bin/bash
# sends a DELETE req to the URL passed as the first argument, and
# displays the body of the res

curl -sX DELETE "$1"
