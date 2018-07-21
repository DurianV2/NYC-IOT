import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class oledwrapper:
    RST = 24
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0

    def clear_screen():
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
        
        disp.begin()
        
        disp.clear()
        disp.display()

    def display_text(text):
        disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        disp.begin()

        disp.clear()
        disp.display()

        clear_screen()

        width = disp.width
        height = disp.height

        image = Image.new('1', (width, height))

        font = ImageFont.load_default()

        draw = ImageDraw.Draw(image)

        draw.rectangle((0, 0, width, height), outline=0, fill=0)

        draw.text((0, 0), text, font=font, fill=255)

        disp.image(image)
        disp.display()
