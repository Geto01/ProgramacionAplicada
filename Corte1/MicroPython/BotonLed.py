import time

from machine import Pin
led = Pin(21, Pin.OUT)
led1 = Pin(19, Pin.OUT)
push_button = Pin(13, Pin.IN)

while True:
  logic_state = push_button.value()
  if logic_state == True:
    led.value(1)
  else:
    led.value(0)
