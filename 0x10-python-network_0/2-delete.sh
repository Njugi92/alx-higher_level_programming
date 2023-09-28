#!/bin/bash
# Script sends a delete request to url passed as first argument and displays body of rensponse
curl -sX DELETE $1 -L
