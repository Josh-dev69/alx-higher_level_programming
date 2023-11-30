#!/bin/bash
# sends POST request to a given url.
curl -s -X POST -d "email-test@gmail.com&subject=I will alwaysbe here for PLD" "$1"
