#!/bin/bash
# Sends a req to a URL passed as an arg; displays only the status code of the res
curl -so /dev/null -w "%{http_code}" "$1"
