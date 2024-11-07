#!/bin/bash

# Check if a file is provided as argument
if [ -f "$1" ]; then
    # Extract words after 'thy' (case insensitive), count occurrences, and sort in descending order
    grep -io '\bthy\b \w\+' "$1" | awk '{print $2}' | sort | uniq -c | sort -rn
fi

