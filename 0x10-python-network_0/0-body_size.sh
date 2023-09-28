#!/bin/bash
# Script takes ur, sends a request to that url then displays body rensponce
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
