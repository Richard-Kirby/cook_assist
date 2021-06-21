import time
import threading

from mcp9600 import MCP9600


class Thermocouple(threading.Thread):

    # Set up thermocouple
    def __init__(self):
        print("init")
        threading.Thread.__init__(self)

        # Default address - assumes breakout doesn't have cut track (Pimoroni)
        self.mcp9600 = MCP9600(i2c_addr=0x66)

        # Set Thermocouple Type
        self.mcp9600.set_thermocouple_type('K')

        self.cold_junction_temp = None
        self.hot_junction_temp = None

    def run(self):

        hot_temp = []
        cold_temp = []

        while True:
            # Get Hot Junction Temperature (thermocouple)
            hot_temp.append(self.mcp9600.get_hot_junction_temperature())

            time.sleep(1)
            # Get Cold Junction Temperature
            cold_temp.append(self.mcp9600.get_cold_junction_temperature())

            while len(hot_temp) > 3:
                hot_temp.pop(0)

            if len(hot_temp) == 3:
                self.hot_junction_temp = int(sum(hot_temp)/3.0)
                print("Hot ", self.hot_junction_temp)

            while len(cold_temp) > 3:
                cold_temp.pop(0)

            if len(cold_temp) == 3:
                self.cold_junction_temp = int(sum(cold_temp)/3.0)
                print("Cold ", self.cold_junction_temp)

            time.sleep(1)