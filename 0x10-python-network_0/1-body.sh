#!/bin/bash
# Script takes url, sends a get request to url and displays body of rensponse
curl -sX GET $1 -L
