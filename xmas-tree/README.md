rpi-scroll-pHAT/xmas-tree
===============
Scripts to use over the *Pimoroni* **scroll-pHAT**

Displays a Christmas tree with many functions


# 1-  Usage
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
  * Set the function to run ('horizontal-dance', 'horizontal-dance-middle', 'horizontal-pulse', 'horizontal-pulse-middle', 'horizontal-show', 'horizontal-show-left', 'horizontal-show-right', 'horizontal-show.middle', 'horizontal-scroll-in', 'horizontal-scroll-out', 'horizontal-scroll', 'horizontal-scroll-dance-out', 'horizontal-scroll-pulse-out', 'vertical-show', 'vertical-show-left', 'vertical-show-right', 'vertical-show-middle', 'vertical-dance', 'vertical-dance-middle', 'vertical-pulse', 'vertical-pulse-middle', 'vertical-scroll-in', 'vertical-scroll-out', 'vertical-scroll', 'vertical-scroll-dance-out', 'vertical-scroll-pulse-out', 'snow-fall', 'clear'), default: horizontal-scroll-dance-out

# 2 - Functions
This are the already fixed functions, fell free to add or change

## 2.1 - Snow
* **snow-fall**
  * Display the *Snow falling*.
  * It can be used with:
      * **-b/--brightness**
  * Example:

      ```
      $ python xmas-tree.py -f snow-fall -b 4
      ```

      ![Imgur Image](http://i.imgur.com/2fGEb6s.gif)

## 2.2 - Horizontal Functions
Functions to be used to display the *Christmas Tree* horizontally.

### 2.2.1 - Horizontal Dance
* **horizontal-dance**
  * Display the *Christmas Tree* dancing horizontally.
  * It can be used with:  
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-dance -b 3 -p 4 -dt 3 -pd 0.4
      ```

      ![Imgur Image](http://i.imgur.com/py6DCLV.gif)

* **horizontal-dance-middle**
  * Display the *Christmas Tree* dancing horizontally.
  * It can be used with:  
      * **-b/--brightness**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-dance-middle -b 6 -dt 4 -pd 1.2
      ```

      ![Imgur Image](http://i.imgur.com/R5ViBiy.gif)

### 2.2.2 - Horizontal Pulse
* **horizontal-pulse**
  * Display the *Christmas Tree* pulsing horizontally.
  * It can be used with:  
      * **-p/--position**
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-pulse -p 3 -pt 2 -pp 0.2
      ```

      ![Imgur Image](http://i.imgur.com/Eq1rMw1.gif)

* **horizontal-pulse-middle**
  * Display the *Christmas Tree* pulsing at the middle horizontally.
  * It can be used with:  
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-pulse-middle -pt 2 -pp 0.2
      ```

      ![Imgur Image](http://i.imgur.com/UMG3GNq.gif)

### 2.2.3 - Horizontal Scroll
* **horizontal-scroll-in**
  * Scroll-in the *Christmas Tree* from *right* to *left* horizontally.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-scroll-in -b 5 -ps 0.8
      ```

      ![Imgur Image](http://i.imgur.com/pHQ84RO.gif)

* **horizontal-scroll-out**
  * Scroll-out the *Christmas Tree* from *right* to *left* horizontally.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-scroll-out -b 3 -ps 1.3
      ```

      ![Imgur Image](http://i.imgur.com/zEaxNog.gif)

* **horizontal-scroll**
  * Scroll-in and out the *Christmas Tree* from *right* to *left* horizontally.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-scroll -b 7 -ps 0.9
      ```

      ![Imgur Image](http://i.imgur.com/0ZofwJm.gif)

* **horizontal-scroll-dance-out**
  * Scroll-in the *Christmas Tree* from *right* to *left* dancing in the middle and scrolling out from *right* to *left* horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-scroll-dance-out -b 4 -dt 3 -pd 0.4 -ps 1.3
      ```

      ![Imgur Image](http://i.imgur.com/ahaETH5.gif)

* **horizontal-scroll-pulse-out**
  * Scroll-in the *Christmas Tree* from *right* to *left* dancing in the middle and scrolling out from *right* to *left* horizontally.
  * It can be used with:
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-scroll-pulse-out -pt 4 -pp 1.5 -ps 0.3
      ```

      ![Imgur Image](http://i.imgur.com/OyQrCMT.gif)

### 2.2.4 - Horizontal Show
* **horizontal-show**
  * Display the *Christmas Tree* horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-show -b 3 -p 4 -po 2.9
      ```

      ![Imgur Image](http://i.imgur.com/51lP6He.gif)

* **horizontal-show-left**
  * Display the *Christmas Tree* bended to the left horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-show-left -b 2 -p 1 -po 4.2
      ```

      ![Imgur Image](http://i.imgur.com/xzjEjTy.gif)

* **horizontal-show-right**
  * Display the *Christmas Tree* bended to the right horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-show-right -b 4 -p 2 -po 2.7
      ```

      ![Imgur Image](http://i.imgur.com/SFENcDQ.gif)

* **horizontal-show-middle**
  * Display the *Christmas Tree* at the middle horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f horizontal-show-middle -b 7 -p 3 -po 6.1
      ```

      ![Imgur Image](http://i.imgur.com/9fOutXX.gif)

## 2.3 - Vertical functions
Functions to be used to display the *Christmas Tree* vertically.

### 2.3.1 - Vertical Dance
* **vertical-dance**
  * Display the *Christmas Tree* dancing vertically.
  * It can be used with:  
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-dance -b 3 -p 4 -dt 3 -pd 0.4
      ```

      ![Imgur Image](http://i.imgur.com/DyJugIf.gif)

* **vertical-dance-middle**
  * Display the *Christmas Tree* dancing at the middle vertically.
  * It can be used with:  
      * **-b/--brightness**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-dance -b 3 -p 4 -dt 3 -pd 0.4
      ```

      ![Imgur Image](http://i.imgur.com/JOoocWR.gif)

### 2.3.2 - Vertical Pulse
* **vertical-pulse**
  * Display the *Christmas Tree* pulsing vertically.
  * It can be used with:  
      * **-p/--position**
      * **-pt/--dance_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-pulse -p 2 -pt 7 -pp 4.8
      ```

      ![Imgur Image](http://i.imgur.com/wuc47uJ.gif)

* **vertical-pulse-middle**
  * Display the *Christmas Tree* pulsing at the middle vertically.
  * It can be used with:  
      * **-pt/--dance_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-pulse-middle -dt 2 -pd 0.6
      ```

      ![Imgur Image](http://i.imgur.com/jl5rESI.gif)

### 2.3.3 - Vertical Scroll
* **vertical-scroll-in**
  * Scroll-in the *Christmas Tree* from *bottom* to *up* vertically.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-scroll-in -b 5 -ps 0.8
      ```

      ![Imgur Image](http://i.imgur.com/YNNUwZe.gif)

* **vertical-scroll-out**
  * Scroll-out the *Christmas Tree* from *bottom* to *up* vertically.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-scroll-out -b 2 -ps 2.1
      ```

      ![Imgur Image](http://i.imgur.com/ZNjsn0E.gif)

* **vertical-scroll**
  * Scroll-in and out the *Christmas Tree* from *bottom* to *up* vertically.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-scroll-out -b 2 -ps 2.1
      ```

      ![Imgur Image](http://i.imgur.com/5BSXyUM.gif)

* **vertical-scroll-dance-out**
  * Scroll-in the *Christmas Tree* from *bottom* to *up* dancing in the middle and scrolling out from *bottom* to *up* horizontally.
  * It can be used with:
      * **-b/--brightness**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-scroll-dance -b 8 -dt 5 -pd 1.3 -ps 0.8
      ```

      ![Imgur Image](http://i.imgur.com/3t9Ya7K.gif)

* **vertical-scroll-pulse-out**
  * Scroll-in the *Christmas Tree* from *bottom* to *up* pulsing in the middle and scrolling out from *bottom* to *up* horizontally.
  * It can be used with:
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-scroll-dance -pt 3 -pp 0.9 -ps 0.5
      ```

      ![Imgur Image](http://i.imgur.com/tENvbeL.gif)

### 2.3.4 - Vertical Show
* **vertical-show**
  * Display the *Christmas Tree* vertically.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-show -b 3 -p 4
      ```

      ![Imgur Image](http://i.imgur.com/wKo42F6.gif)

* **vertical-show-left**
  * Display the *Christmas Tree* bended to the left vertically.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-show-left -b 2 -p 1 -po 3.5
      ```

      ![Imgur Image](http://i.imgur.com/rIkqddm.gif)

* **vertical-show-right**
  * Display the *Christmas Tree* bended to the right vertically.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-show-right -b 5 -p 3 -po 0.7
      ```

      ![Imgur Image](http://i.imgur.com/TjOIVct.gif)

* **vertical-show-middle**
  * Display the *Christmas Tree* at the middle vertically.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-po/ --pause-show**
  * Example:

      ```
      $ python xmas-tree.py -f vertical-show-middle -b 7 -p 3 -po 6.1
      ```

      ![Imgur Image](http://i.imgur.com/G7wBIqx.gif)

## 2.4 - Other functions
* **clear**
  * Clears the *scroll-pHAT* display
  * Example:

    ```
    $ python pacman.py -f clear
    ```
