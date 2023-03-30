#!/bin/bash
# get the size of the body of a response from server

 curl -sI $1 | grep -i Content-Length | awk '/Content-Length/ { print $2  }'
