#!/bin/bash

# Define the host and port
host="pyrat.thm"
port=8000

# Use netcat to connect to the server
(
    # Wait for a moment to ensure the connection is established
    sleep 0.1

    # Send the username
    echo "admin"
    echo "[~] Sending admin"

    # Send the password
    echo "abc123"
    echo "[~] Sending abc123"

    # Wait before receiving the response
    echo "[~] Waiting for response"
    sleep 0.5
) | telnet "$host" "$port"  # Connect to the specified host and port

# To read the response, you can redirect output from netcat directly to a variable if needed
response=$(telnet "$host" "$port")
echo "[+] Response:"
echo "$response"
