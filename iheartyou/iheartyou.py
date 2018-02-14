from sense_hat import SenseHat
import time

hat= SenseHat()
hat.set_rotation(180)
hat.low_light=True

blue = (0,0,127)
r=(255,0,0)
o= (0,0,0)
heart = [
	o,r,o,o,o,o,r,o,
	r,o,r,o,o,r,o,r,
	r,o,o,r,r,o,o,r,
	r,o,o,o,o,o,o,r,
	o,r,o,o,o,o,r,o,
	o,o,r,o,o,r,o,o,
	o,o,o,r,r,o,o,o,
	o,o,o,o,o,o,o,o
]

# hat.show_message("I Hello World", text_colour=r)
hat.show_letter("I");
time.sleep(2);
hat.set_pixels(heart);
time.sleep(2);
hat.show_message("You");
