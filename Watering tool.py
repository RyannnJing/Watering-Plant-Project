import music
from microbit import *

# Declare variables
# Set pins
water_sensor = pin0
ambient_light_sensor = pin1
soil_humidity_sensor = pin2
buzzer = pin12
relay = pin13
# Set the baseline
LOW_WATER_LEVEL = 80    # production:  80, testing: 120
LOW_LIGHT_LEVEL = 50    # production:  50, testing: 100
LOW_HUMIDITY = 330      # production: 330, testing: 420


# Main loop
def main():
    while True:
        # Reset
        display.clear()
        switch_buzzer(False)
        # Get the water level and light level
        is_enough_water = water_sensor.read_analog() > LOW_WATER_LEVEL
        is_day_time = ambient_light_sensor.read_analog() > LOW_LIGHT_LEVEL
        # Water level detect
        if is_enough_water:
            # Enough water, test the humidity
            soil_need_water = track_soil_humidity()
            if soil_need_water:
                watering()
        elif is_day_time:
            # Low water level & during day time: add water
            switch_buzzer(True)
        else:
            # Low water level & at night: sleep for a while
            sleep(1000*60*60*4)


# Test the humidity
# @return is_need_water tank value
def track_soil_humidity():
    value = soil_humidity_sensor.read_analog()
    need_water = value < LOW_HUMIDITY
    if need_water:
        display.show(Image.SAD)
    else:
        display.show(Image.HAPPY)
    return need_water


# Inform users when water is running low in the tank
# @param switch_on: buzzer on or off
def switch_buzzer(switch_on):
    if switch_on:
        music.play('c4:2', pin=buzzer, wait=True, loop=False)
    else:
        music.stop(buzzer)


# Watering
def watering():
    relay.write_digital(True)
    # Stop watering after a few seconds
    sleep(1000*10)
    relay.write_digital(False)


# Call the main function.
main()
