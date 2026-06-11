#!/bin/sh

export LD_LIBRARY_PATH=/vendor/lib64

ddl_file_name=$(echo "$1" | tr -d "'\"")
echo "Using DDL Filename: '$ddl_file_name'"

if [ -z "$ddl_file_name" ]; then
    echo "ERROR: DDL File name not provided."
    exit 1
fi

C2C_TEST_CONSOLE="/data/c2c_test_console"
DMARF_LOG="/data/dmarf_output.log"

# Ensure /data directory exists
if [ ! -d "/data" ]; then
    echo "[INFO] Creating /data directory..."
    mkdir -p /data
fi

# Ensure the test console is terminated on script exit
trap 'pkill -f c2c_test_console' EXIT

# Run the test console with commands and redirect output to log file
(
    echo 'mechapp'
    sleep 2
    echo "dmarf /data/$ddl_file_name"
    sleep 10
) | $C2C_TEST_CONSOLE > "$DMARF_LOG" 2>&1 &

# Wait for the background process to complete
sleep 30  # Adjust based on expected dmarf duration

# Kill the test console process
pkill -f c2c_test_console

echo "dmarf execution completed. Output saved to $DMARF_LOG"

exit 0