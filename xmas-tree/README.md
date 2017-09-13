rpi-scroll-pHAT/xmas-tree
===============
Scripts to use over the *Pimoroni* **scroll-pHAT**

Displays a Christmas tree with many functions


# Usage
The arguments that can be used with the script:

```
$ python xmas-tree [-h] [-f FUNCTION] [-b BRIGHTNESS] [-p POSITION]
                    [-dt DANCE_TIMES] [-pt PULSE_TIMES] [-st SNOW_TIMES]
                    [-pd PAUSE_DANCE] [-pp PAUSE_PULSE] [-ps PAUSE_SCROLL]
                    [-psn PAUSE_SNOW] [-v]
```

Optional arguments:

* **-h, --help**
  * show help message and exit
* **-v, --verbose**
  * Increase output verbosity
* **-b BRIGHTNESS, --brightness BRIGHTNESS**
  * Set the brightness, default: 5
* **-p POSITION, --position POSITION**
  * Set the start position, default: 0
* **-dt DANCE\_TIMES, --dance_times DANCE\_TIMES**
  * Set how many times to dance, default: 3
* **-pt PULSE\_TIMES, --pulse_times PULSE\_TIMES**
  * Set how many times to pulse, default: 3
* **-st SNOW\_TIMES, --snow_times SNOW\_TIMES**
  * Set how many times to snow, default: 3
* **-pd PAUSE\_DANCE, --pause-dance PAUSE\_DANCE**
  * Set the dance pause interval in seconds, default: 0.3
* **-pp PAUSE\_PULSE, --pause-pulse PAUSE\_PULSE**
  * Set the pulse pause interval in seconds, default: 0.3
* **-ps PAUSE\_SCROLL, --pause-scroll PAUSE\_SCROLL**
  * Set the scroll pause interval in seconds, default: 0.3
* **-psn PAUSE\_SNOW, --pause-snow PAUSE\_SNOW**
  * Set the snow pause interval in seconds, default: 0.3
* **-po PAUSE\_SHOW, --pause-show PAUSE\_SHOW**
  * Set the show pause interval in seconds, default: 5
* **-f FUNCTION, --function FUNCTION**
  * Set the function to run ('scroll-in', 'scroll-out', 'dance') type, default: show-horizontal-center

# Functions
This are the already fixed functions, fell free to add or change

## Snow
* **snow-fall**
  * WIP

## Clear
* **clear**
  * WIP

## Horizontal Functions
* **horizontal-dance**
  * WIP
* **horizontal-dance-middle**
  * WIP
* **horizontal-pulse**
  * WIP
* **horizontal-pulse-middle**
  * WIP
* **horizontal-show-center**
  * WIP
* **horizontal-show-left**
  * WIP
* **horizontal-show-right**
  * WIP
* **horizontal-show-middle**
  * WIP
* **horizontal-scroll-in**
  * WIP
* **horizontal-scroll-out**
  * WIP
* **horizontal-scroll**
  * WIP
* **horizontal-scroll-dance-out**
  * WIP
* **horizontal-scroll-pulse-out**
  * WIP

## Vertical functions


* **vertical-show-center**
  * WIP
* **vertical-show-left**
  * WIP
* **vertical-show-right**
  * WIP
* **vertical-show-middle**
  * WIP
* **vertical-dance**
  * WIP
* **vertical-dance-middle**
  * WIP
* **vertical-pulse**
  * WIP
* **vertical-pulse-middle**
  * WIP
* **vertical-scroll-in**
  * WIP
* **vertical-scroll-out**
  * WIP
* **vertical-scroll**
  * WIP
* **vertical-scroll-dance-out**
  * WIP
* **vertical-scroll-pulse-out**
  * WIP

## Other functions
* **clear**
  * Clears the *scroll-pHAT* display
  * Example:

    ```
    $ python pacman.py -f clear
    ```
