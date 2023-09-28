#!/bin/bash
# Script takes in a URL, sends POST request to the passed URL, and displays body of response
curl -sX POST $1 -d "email=test@gmail.com&subject=I will always be here for PLD" -L
