#!/bin/bash

# Filename: ex20.sh
#
# Problem: Remove the html tags from ex20.input.
cat ex20.input | awk '{
        # print the line without the html tags
        gsub(/<[^>]*>/, "")
        print $0
    }'
