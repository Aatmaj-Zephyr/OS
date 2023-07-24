#!/bin/bash

# Check if an integer is provided as a command-line argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <integer>"
  exit 1
fi

# Function to calculate factorial
calculate_factorial() {
  local num=$1
  local factorial=1

  for (( i=1; i<=num; i++ )); do
    factorial=$(( factorial * i ))
  done

  echo $factorial
}

# Check if the argument is a valid integer
if [[ "$1" =~ ^[0-9]+$ ]]; then
  number=$1
  result=$(calculate_factorial $number)
  echo "Factorial of $number is $result."
else
  echo "Error: Please provide a valid integer as the argument."
fi
