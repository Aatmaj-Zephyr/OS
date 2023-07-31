#!/bin/bash
processcount=$(ps -e --no-header|wc -l)
echo "($processcount)"
