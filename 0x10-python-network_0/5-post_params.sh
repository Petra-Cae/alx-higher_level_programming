#!/bin/bash
# takes in a URL, sends a `POST` req to the passed URL; displays the body of the res
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
