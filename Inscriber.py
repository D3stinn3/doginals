import os
import time
from subprocess import run

directory = "DogeKirbies"

# Check if the directory exists
if not os.path.exists(directory) or not os.path.isdir(directory):
    print(f"Error: Directory '{directory}' not found.")
    exit(1)

# Check if there are any PNG files in the directory
png_files = [file for file in os.listdir(directory) if file.endswith(".png")]

if not png_files:
    print(f"Error: No PNG files found in '{directory}'.")
    exit(1)

# Iterate over PNG files
for file in png_files:
    file_path = os.path.join(directory, file)
    print(file_path)

    # Run the node command
    run(["node", ".", "mint", "DKvviV84ysJo3TEzsGap7sHwJhXF8QAcpL", file_path])

    while os.path.exists("pending-txs.json"):
        print("pending txs, so sleep 30s")
        os.system("ls -al pending-txs.json")
        time.sleep(30)
        print("retrying the pending")
        # This will probably just retry the pending tx, and not try to send 1.
        # FIXME: must send eg 1 to count as dust. Send 0 causes this software to send all!!!
        run(["node", ".", "wallet", "send", "D66f9q2fL3pEfnbQEuy7qPaoD2PZL7iEvP", "1"])

print("Script execution complete.")