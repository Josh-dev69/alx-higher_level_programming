#!/bin/bash
# sends Get request and disply the body response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
