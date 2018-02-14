from sense_hat import SenseHat

hat = SenseHat()
hat.set_rotation(180)


temp = hat.get_temperature()
text = str(round(temp,2))
hat.show_message("Temperature = ", scroll_speed=0.05)
hat.show_message(text)

temp = hat.get_temperature_from_humidity()
text = str(round(temp,2))
hat.show_message(text, text_colour=[127, 0,127])
