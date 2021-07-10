import time
import Display
import thermocoupler


# 128x64 display with hardware I2C - Setting it up.
screen = Display.Screen(24, 0x3C)

screen.clear()

# Putting start up.
screen.write_text("Cook Assist", "/home/pi/cook_assist/Verdana.ttf", 14)


screen.start()

thermocouple = thermocoupler.Thermocouple()
thermocouple.start()

while True:
    if thermocouple.hot_junction_temp is not None:
        temp_str = "{}C".format(thermocouple.hot_junction_temp)
        screen.temp_queue.put_nowait(temp_str)
        #print(temp_str)
        time.sleep(2)

#for t in range(100, 999):
#    screen.temp_queue.put_nowait("{}C".format(t))
#    time.sleep(.01)


