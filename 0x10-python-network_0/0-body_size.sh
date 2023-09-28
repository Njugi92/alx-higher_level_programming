#!/bin/bash
# Script takes in url, sends a request and displays size of body rensponse
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
