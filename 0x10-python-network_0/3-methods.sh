#!/bin/bash
# takes in a url and displays all HTTP methods the server will accept
curl -sI "$1" | grep Allow | cut -df " " 2-
