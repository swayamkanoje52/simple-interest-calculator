#!/usr/bin/env bash

# Simple Interest Calculator (Bash)
# Prompts user for principal, rate, and time then calculates simple interest.

set -euo pipefail

re='^[0-9]+([.][0-9]+)?$'

read -p "Enter Principal Amount (P): " principal
if ! [[ $principal =~ $re ]]; then
  echo "Error: Principal must be a non-negative number." >&2
  exit 1
fi

read -p "Enter Annual Interest Rate (R) in %: " rate
if ! [[ $rate =~ $re ]]; then
  echo "Error: Rate must be a non-negative number." >&2
  exit 1
fi

read -p "Enter Time Period (T) in Years: " time
if ! [[ $time =~ $re ]]; then
  echo "Error: Time must be a non-negative number." >&2
  exit 1
fi

# Calculate simple interest and total amount using bc for floating point arithmetic
interest=$(echo "scale=6; ($principal * $rate * $time) / 100" | bc -l)
total=$(echo "scale=6; $principal + $interest" | bc -l)

# Format results to 2 decimal places
interest_f=$(printf "%.2f" "$interest")
total_f=$(printf "%.2f" "$total")

printf "\n========================================\n"
printf "           SIMPLE INTEREST RESULT      \n"
printf "========================================\n"
printf "Principal Amount    : %s\n" "$principal"
printf "Annual Interest Rate: %s%%\n" "$rate"
printf "Time Period         : %s years\n" "$time"
printf "----------------------------------------\n"
printf "Simple Interest     : %s\n" "$interest_f"
printf "Total Amount        : %s\n" "$total_f"
printf "========================================\n"
