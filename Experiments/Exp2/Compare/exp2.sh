 #!/bin/bash

# Check if two file names are provided as arguments
if [ $# -ne 2 ]; then
  echo "Usage: $0 <file1> <file2>"
  exit 1
fi

file1="$1"
file2="$2"

# Check if both files exist
if [ ! -f "$file1" ]; then
  echo "Error: File '$file1' does not exist."
  exit 1
fi

if [ ! -f "$file2" ]; then
  echo "Error: File '$file2' does not exist."
  exit 1
fi

# Compare the contents of the files
if cmp -s "$file1" "$file2"; then
  echo "The contents of '$file1' and '$file2' are the same. Deleting '$file2'..."
  rm "$file2"
else
  echo "The contents of '$file1' and '$file2' are different."
fi

