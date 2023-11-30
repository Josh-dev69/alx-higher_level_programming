#!/bin/bash
# Get the body size of a request

curl -s -o /dev/null -w "%{size_download}" "$1"; echo
