# Import the modules to send commands to the system and access GPIO pins
import RPi.GPIO as gpio
from time import sleep
from os import system
 
# Define a function to keep script running
def loop():
    while True:
        sleep(600)
 
# Define a function to run when an interrupt is called
def shutdown(pin):
    print("Interrupt detected... Halting the system!")
    system('shutdown -h now')

#print("Setting GPIO...") 
gpio.setmode(gpio.BOARD) # Set pin numbering to board numbering
gpio.setup(26, gpio.IN, pull_up_down=gpio.PUD_UP) # Set up pin 26 as an input and internal pullup resistor
#print("Setting interrupt...")
gpio.add_event_detect(26, gpio.FALLING, callback=shutdown, bouncetime=200) # Set up an interrupt to look for button presses
 
loop() # Run the loop function to keep script running
