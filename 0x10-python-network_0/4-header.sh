#!/bin/bash
# sends Get request and disply the body response
curl -s -H "X-School-User-Id: 98" -X GET "$1"
