#!/bin/bash
# Script takes in a URL as argument, sends a GET request to the URL, and displays body of response
curl -sX GET $1 -H "X-HolbertonSchool-User-Id: 98" -L
