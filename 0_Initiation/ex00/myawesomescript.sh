#!/bin/sh

# Check if an argument was provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <bit.ly URL>"
    exit 1
fi

# Use curl to fetch the header of the URL and grep to find the location header
url=$(curl -sI "$1" | grep -i location: | cut -d ' ' -f2 | tr -d '\r')

# Output the final URL
echo $url

