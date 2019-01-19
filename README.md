# micropython
Dojo notes and scripts for Arklow Coder Dojo.

## Links
micropython main site = http://micropython.org/

micropython docs - https://docs.micropython.org/en/latest/index.html

micropython getting started with esp8266 - https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro

thonny ide set up for micropython - https://bitbucket.org/plas/thonny/wiki/MicroPython

ampy tool to copy files to esp8266 - https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

good tutorial on running a webserver - https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

webrepl - https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi


## Definitions

REPL - read–eval–print loop

A read–eval–print loop (REPL), also termed an interactive toplevel or language shell, is a simple, interactive computer programming environment that takes single user inputs (i.e., single expressions), evaluates them, and returns the result to the user; a program written in a REPL environment is executed piecewise.

https://en.m.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

## Scripts Examples

simple_webserver.py - based on random tutorials.com without the led

square_numbers.py - print the sum of numbes 1-10


### Running scripts on start up 

There are two files that are treated specially by the ESP8266 when it starts up:```boot.py ```and ```main.py```. The boot.py script is executed first (if it exists) and then once it completes the main.py script is executed. You can create these files yourself and populate them with the code that you want to run when the device starts up.

## Other

### List files on esp 

```python
import os
os.listdir()
```

### Write file

```python
import os
os.listdir()
```

### Check the firmware

Useful if things are not working

```python
import esp
esp.check_fw()
```

### free up memory

```python
import gc
gc.collect()
```


### GPIO Pins
https://docs.micropython.org/en/latest/esp8266/quickref.html#pins-and-gpio

```python
from machine import Pin

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation
```

