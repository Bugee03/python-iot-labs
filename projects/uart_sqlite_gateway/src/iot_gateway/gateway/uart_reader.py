import serial
import json


class UARTReader:

    def __init__(self,port : str,baudrate: int = 115200):
        self.port = port
        self.baudrate = baudrate
        self.connection = None


    def connect(self):

        self.connection = serial.Serial(self.port, self.baudrate, timeout=1)


    def read_line(self):
        line = self.connection.readline().decode("utf-8").rstrip()
        if line:
            return json.loads(line)
        return None