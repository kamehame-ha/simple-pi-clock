import time
import board
import busio
from adafruit_ht16k33.segments import Seg7x4
from datetime import datetime

# Display setup
i2c = busio.I2C(board.SCL, board.SDA)
display = Seg7x4(i2c)

# Clear display & set brightness
display.fill(0)
display.brightness = 0.2

def get_time():
    datetime_obj = datetime.now()
    formatted_time = datetime_obj.strftime("%H:%M")
    formatted_date = datetime_obj.strftime("%d.%m")
    
    result = {
        "time": formatted_time,
        "date": formatted_date
    }
    
    return result

def display_on_display(time):
    display.print(time)


while True:
    display_on_display(get_time().get('time'))
    time.sleep(1)
