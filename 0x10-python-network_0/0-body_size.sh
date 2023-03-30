#!/bin/bash
# get the size of the body of a response from server
curl -s "$1" | wc -c
