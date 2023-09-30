#!/bin/bash
# script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond
curl -o /dev/null -sw "You find me!" 0.0.0.0:5000/catch_me
