#!/bin/bash
# Sends
curl -s -o /dev/null -w "%{http_code}" "$1"
