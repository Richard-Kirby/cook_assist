from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import threading
import queue
import time

import Adafruit_SSD1306


class Screen(threading.Thread):

    #Set up the screen
    def __init__(self, reset, address):
        print("init")
        threading.Thread.__init__(self)
        self.disp = Adafruit_SSD1306.SSD1306_128_64(reset, address)
        self.width = 128
        self.height = 64

        self.disp.begin()
        # Clear display.
        self.disp.clear()
        self.disp.display()

        # Display is available
        self.DisplayAttached = 1
        # Getting ready to put images on screen
        self.image = Image.new('1', (self.width, self.height))

        # Get drawing object to draw on image.
        print("Draw")
        self.draw = ImageDraw.Draw(self.image)

        self.temp_queue = queue.Queue()

        '''
        try:
            self.disp.begin()
            # Clear display.
            self.disp.clear()
            self.disp.display()

            # Display is available
            self.DisplayAttached = 1
            # Getting ready to put images on screen
            self.image = Image.new('1', (disp.width, disp.height))

            # Get drawing object to draw on image.
            print("Draw")
            self.draw = ImageDraw.Draw(image)

        except:
            self.DisplayAttached = 0
            print("No Display - print to terminal only.")
        '''

    def clear(self):
        self.draw.rectangle((0, 0, self.width, self.height), outline=0, fill=0)
        self.disp.image(self.image)
        self.disp.display()

    def write_text(self, StringToPrint, FontName, FontSize, XLoc=0, YLoc=0):
        font = ImageFont.truetype(FontName, FontSize)

        # Clear the temp area
        self.draw.rectangle((0, 15, self.width, 50), outline=0, fill=0)
        self.disp.image(self.image)
        self.disp.display()

        # Write the text.  It is the caller's responsibility to ensure string fits
        self.draw.text((XLoc, YLoc), StringToPrint, font=font, fill=255)

        # Display image.
        self.disp.image(self.image)
        self.disp.display()

    def run(self):
        while True:
            temp_str = None
            while not self.temp_queue.empty():
                temp_str = self.temp_queue.get_nowait()

            if temp_str is not None:
                self.write_text(temp_str, "/home/pi/cook_assist/Verdana.ttf", 40, XLoc=0, YLoc=10)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 128x64 display with hardware I2C - Setting it up.
    screen = Screen(24, 0x3C)

    screen.clear()

    # Putting start up.
    screen.write_text("Cook Assist", "¬/cook_assist/Verdana.ttf", 14)
    screen.write_text("Starting...", "¬/cook_assist/Verdana.ttf", 40, XLoc=0, YLoc=10)

    screen.start()

    for t in range(100, 999):
        screen.temp_queue.put_nowait("{}C".format(t))
        time.sleep(.01)



