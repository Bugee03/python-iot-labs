from uart_reader import UARTReader
from database import Database
import time

PORT = "/dev/tty.usbmodem1203"

def main():
    uart = UARTReader(PORT)
    db = Database()

    uart.connect()

    print("Gateway started...")

    while True:
        data = uart.read_line()
        if data:
            print("Received:", data)
            db.insert(data)
        time.sleep(0.1)

if __name__ == "__main__":
    main()
