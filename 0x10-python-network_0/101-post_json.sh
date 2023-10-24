#!/bin/bash
# sends a JSON POST request to URL passed as first argument, and displays the body of the response
curl -sX POST $1 -H "Content-Type: application/json" -d @$2 -L
