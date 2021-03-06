# MicroPython
Dojo notes and scripts for Arklow Coder Dojo.

## Links

micropython main site = http://micropython.org/

micropython docs - https://docs.micropython.org/en/latest/index.html

micropython getting started with esp8266 - https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#intro

thonny ide set up for micropython - https://bitbucket.org/plas/thonny/wiki/MicroPython

ampy tool to copy files to esp8266 - https://learn.adafruit.com/micropython-basics-load-files-and-run-code/install-ampy

good tutorial on running a webserver - https://randomnerdtutorials.com/esp32-esp8266-micropython-web-server/

webrepl - https://docs.micropython.org/en/latest/esp8266/tutorial/repl.html#webrepl-a-prompt-over-wifi

firmwares - http://micropython.org/download#esp8266

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

### Check the firmware
Useful if things are not working

```python
import esp
esp.check_fw()
```

### Free up memory

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

### help

On the board

```python
help()

Welcome to MicroPython!

For online docs please visit http://docs.micropython.org/en/latest/esp8266/ .

For diagnostic information to include in bug reports execute 'import port_diag'.

Control commands:
  CTRL-A        -- on a blank line, enter raw REPL mode
  CTRL-B        -- on a blank line, enter normal REPL mode
  CTRL-C        -- interrupt a running program
  CTRL-D        -- on a blank line, do a soft reset of the board
  CTRL-E        -- on a blank line, enter paste mode

For further help on a specific object, type help(obj)

```

### List modules

```python
help('modules')
```

### Basic wifi configuration

```Python

import network
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.scan()                             # Scan for available access points
sta_if.connect("<AP_name>", "<password>") # Connect to an AP
sta_if.isconnected()                      # Check for successful connection

# Change name/password of ESP8266's AP:
ap_if = network.WLAN(network.AP_IF)
ap_if.config(essid="<AP_NAME>", authmode=network.AUTH_WPA_WPA2_PSK, password="<password>")

```


### Writing and reading files

MicroPython on the ESP8266 supports the standard way of accessing files in Python, using the built-in open() function.

To create a file try:

```python
>>> f = open('data.txt', 'w')
>>> f.write('some data')
9
>>> f.close()
```

The “9” is the number of bytes that were written with the write() method. Then you can read back the contents of this new file using:

```python
>>> f = open('data.txt')
>>> f.read()
'some data'
>>> f.close()
```