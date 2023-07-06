#!/bin/bash
# Makes a req to 0.0.0.0:5000/catch_me that gets the server to respond with a msg
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
