#!/bin/bash
# takes in a URL as an arg, sends a `GET` request to the URL,
# and displays the body of the res

curl -sH "X-HolbertonSchool-User-Id: 98" "${1}"
