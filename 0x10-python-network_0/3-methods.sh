#!/bin/bash
# Takes
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
