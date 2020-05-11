# Watering-Plant-Project
Water plant project based on the BBC Micro: Bit, written in Python

# Introduction
To get started, please wire the sensors up as the following:
Water Sensor
-:G0, +:V0, S:S0
— — —
Ambient Light Sensor
-:G1, +:V1, S:S1
— — —
Soil Humidity Sensor
-:G2, +:V2, S:S2
— — —
Digital Buzzer Module
-:G12, +:V12, S:S12
- - -
Red LED Module
-:G13, +:V13, S:S13

# How it works
When the plant needs water, a water pump will automatically pump water out from the watet tank and water the plant. During day time, a buzzer will ring to inform users to add more water when the water level is low in the tank.
The red LER module is used to situmlate the water pump.
