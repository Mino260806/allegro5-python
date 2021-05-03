# ALLEGRO 5 OFFICIAL DISTRIBUTION

> Allegro is a cross-platform library mainly aimed at video game and multimedia programming. It handles common, low-level tasks such as creating windows, accepting user input, loading data, drawing images, playing sounds, etc. and generally abstracting away the underlying platform...

This is the official allegro 5 wrapper in python. It was built from the [official github repo](https://github.com/liballeg/allegro5/) using cmake.

- Tested on **windows 10** with a **32-bit** python interpreter

(It is preferable to use a 32-bit interpreter because 64-bit hasn't been tested _yet_)

Demo script
----
```py
import os

os.environ['ALLEGRO5_DLL'] = r'path\to\allegro5\dlls'
os.environ['ALLEGRO5_VERSION'] = '5.0.10' # this is just an example

from allegro5 import *

al_run_demo()
```

The demo game is hosted [here](https://github.com/liballeg/allegro5/blob/master/python/pong.py) 

Documentation
------
You can find official documentation [here](https://www.allegro.cc/manual/5/)