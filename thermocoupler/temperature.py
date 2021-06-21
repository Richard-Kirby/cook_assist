from mcp9600 import MCP9600
import time

# Default address - assumes breakout doesn't have cut track (Pimoroni)
mcp9600 = MCP9600(i2c_addr=0x66)

# Set Thermocouple Type
mcp9600.set_thermocouple_type('K')

while(1):
    # Get Hot Junction Temperature (thermocouple)
    print("Hot Side", mcp9600.get_hot_junction_temperature())

    time.sleep(1)
    # Get Cold Junction Temperature
    print("Cold Side", mcp9600.get_cold_junction_temperature())
    time.sleep(5)


