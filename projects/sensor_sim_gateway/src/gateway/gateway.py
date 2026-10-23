import subprocess
import json
import sys

def run_gateway_from_simulator():
    #here will initalize (reading UART ..)
    process = subprocess.Popen(
        [sys.executable, "simulator.py"],
        stdout=subprocess.PIPE,
        text=True
    )

    for line in process.stdout:
        data = json.loads(line.strip())  # JSON строка -> dict
        print("Received:", data)


if __name__ == "__main__":
    run_gateway_from_simulator()


