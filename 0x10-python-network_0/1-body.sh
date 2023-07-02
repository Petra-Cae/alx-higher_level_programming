#!/usr/bin/bash
# Takes in a URL, sends a GET request to it, and
# displays the body of the 200 status code response

curl -sL "$1"
