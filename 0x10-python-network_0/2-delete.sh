#!/bin/bash
# sends a DELETE req to the URL passed as the first arg; displays the body of the res
curl -sX DELETE "$1"
