#!/bin/bash
<<<<<<< HEAD
# Script takes in url, sends a request and displays size of body rensponse
=======
# Script takes ur, sends a request to that url then displays body rensponce
>>>>>>> d93a317299874095664a138880a4b2ee2a62840c
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
