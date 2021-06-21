
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Prints out to the OLED screen.  ClearWidth and ClearHeight specify how much of screen to clear.
# XLoc and YLic specify X/Y Coordinates of where to print the text.
def OLED_Print(StringToPrint, FontName, FontSize, ClearWidth, ClearHeight, Clear=1, XLoc=0, YLoc=0):
    font = ImageFont.truetype(FontName, FontSize)

    if (DisplayAttached):
        # Optional Clear will clear the defined area by over writing with a black rectangle.
        if (Clear):
            draw.rectangle((0, 0, ClearWidth, ClearHeight), outline=0, fill=0)
            disp.image(image)
            disp.display()

        # Write the text.  It is the caller's responsibility to ensure string fits
        draw.text((XLoc, YLoc), StringToPrint, font=font, fill=255)

        # Display image.
        disp.image(image)
        disp.display()

# 128x64 display with hardware I2C - Setting it up.
disp = Adafruit_SSD1306.SSD1306_128_64(rst=24, i2c_address=0x3C)

# Initialize library.
try:
    disp.begin()
    # Clear display.
    disp.clear()
    disp.display()

    # Display is available
    DisplayAttached = 1
    # Getting ready to put images on screen
    image = Image.new('1', (disp.width, disp.height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)
except:
    DisplayAttached = 0
    print("No Display - print to terminal only.")

# Putting start up.
OLED_Print("01234567890123456789", "Verdana.ttf", 14, disp.width, disp.height)
OLED_Print("900C", "Verdana.ttf", 40, disp.width, disp.height, XLoc=0, YLoc=10)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass


