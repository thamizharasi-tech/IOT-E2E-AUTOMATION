#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64
vm_a2a_test="/vendor/bin/vm_a2a_test"

cd /vendor/bin || { echo "✘ Unable to access /vendor/bin"; exit 1; }

# Start vm_a2a_test if not already running
if ! pgrep -f "$vm_a2a_test" > /dev/null; then
    echo "Starting vm_a2a_test..."
    $vm_a2a_test &
    sleep 5
else
    echo "vm_a2a_test is already running."
fi

# Get the process ID of vm_a2a_test
vm_pid=$(pgrep -f "vm_a2a_test")

# Ensure process is running before sending input
if [ -n "$vm_pid" ]; then
    echo "Sending input 'a' to vm_a2a_test..."
    echo "a" > /proc/$vm_pid/fd/0  # Send input correctly
    echo "Message sent."
else
    echo "vm_a2a_test is not running. Message not sent."
    exit 1
fi

# Keep the script running for interactive use
echo "Script is now idle and waiting for further input. Press Ctrl+C to stop."
while true; do
    sleep 60
done
