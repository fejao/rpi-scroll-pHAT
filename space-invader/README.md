rpi-scroll-pHAT/space-invader
===============
Display a Space-Invader character over your scroll-pHAT from Pimoroni

Script was written to not be complicated and re-factored easily, maybe in future adding for *scroll-pHAT-HD* also

# Usage
The arguments that can be used with the script:

```
$ python space-invader.py [-h] [-v] [-b BRIGHTNESS] [-dt DANCE_TIMES]
                         [-pt PULSE_TIMES] [-pd PAUSE_DANCE] [-pp PAUSE_PULSE]
                         [-ps PAUSE_SCROLL] [-po PAUSE_SHOW] [-f FUNCTION]
```

Optional arguments:

* **-h, --help**
  * show help message and exit
* **-v, --verbose**
  * Increase output verbosity
* **-b BRIGHTNESS, --brightness BRIGHTNESS**
  * Set the brightness, default: 5
* **-dt DANCE\_TIMES, --dance_times DANCE\_TIMES**
  * Set how many times to dance, default: 3
* **-pt PULSE\_TIMES, --pulse_times PULSE\_TIMES**
  * Set how many times to pulse, default: 3
* **-pd PAUSE\_DANCE, --pause-dance PAUSE\_DANCE**
  * Set the dance pause interval in seconds, default: 0.3
* **-pp PAUSE\_PULSE, --pause-pulse PAUSE\_PULSE**
  * Set the pulse pause interval in seconds, default: 0.3
* **-ps PAUSE\_SCROLL, --pause-scroll PAUSE\_SCROLL**
  * Set the scroll pause interval in seconds, default: 0.3
* **-po PAUSE\_SHOW, --pause-show PAUSE\_SHOW**
  * Set the show pause interval in seconds, default: 5
* **-f FUNCTION, --function FUNCTION**
  * Set the function to run ('dance', 'pulse', 'show','scroll-in', 'scroll-out', 'scroll', 'scroll-and-dance', 'scroll-and-pulse', 'clear'), default: scroll-and-pulse

# Functions
  This are the already fixed functions, fell free to add or change

* **dance**
  * Display the *Space-Invader* figure dancing. It can be used with:
      * **-b/--brightness**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python space-invader.py -f dance -b 7 -dt 3 -pd 0.2
      ```

      ![Imgur Image](http://i.imgur.com/w1VbJJ1.gif)

* **pulse**
  * Display the *Space-Invader* figure pulsing.
  * It can be used with:
      * **-pp/--pause-pulse**
      * **-pt/--pulse_times**
  * Example:

      ```
      $ python space-invader.py -f pulse -pt 3 -pp 0.4
      ```

      ![Imgur Image](http://i.imgur.com/HuSA28G.gif)

* **show-arms-down**
  * Display the *Space-Invader* with the arms down.
  * It can be used with:
      * **-b/--brightness**
      * **-po/--pause_show**
  * Example:

      ```
      $ python space-invader.py -f show-arms-down -b 5 -po 1.3
      ```

      ![Imgur Image](http://i.imgur.com/NPYSzSB.gif)

  * **show-arms-up**
    * Display the *Space-Invader* with the arms up.
    * It can be used with:
        * **-b/--brightness**
        * **-po/--pause_show**
    * Example:

        ```
        $ python space-invader.py -f show-arms-up -b 4 -po 2.3
        ```

        ![Imgur Image](http://i.imgur.com/U5vqD0F.gif)

* **scroll-in**
  * Scroll-in the *Space-Invader* figure.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python space-invader.py -f scroll-in -b 5 -ps 0.6
      ```

      ![Imgur Image](http://i.imgur.com/C7uPH6d.gif)

* **scroll-out**
  * Scroll-out the *Space-Invader* figure.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python space-invader.py -f scroll-in -b 5 -ps 0.6
      ```

      ![Imgur Image](http://i.imgur.com/uWuKPgm.gif)

* **scroll**
  * Scroll-in and out the *Space-Invader* figure.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python space-invader.py -f scroll -b 7 -ps 1.8
      ```

      ![Imgur Image](http://i.imgur.com/A8x8uYr.gif)


* **scroll-and-dance**
  * Scroll-in the *Space-Invader* figure, dancing in the middle and scroll-out.
  * It can be used with:
      * **-b/--brightness**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python space-invader.py -f scroll-and-dance -pd 0.4 -ps 0.5
      ```

      ![Imgur Image](http://i.imgur.com/0RxCdsr.gif)

* **scroll-and-pulse**
  * Scroll-in the *Space-Invader* figure, pulsing in the middle and scroll-out.
  * It can be used with:
      * **-b/--brightness**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python space-invader.py -f scroll-and-dance -pp 0.5 -ps 0.4
      ```

      ![Imgur Image](http://i.imgur.com/x8ZZOrJ.gif)

## Other functions
* **clear**
  * Clears the *scroll-pHAT* display
  * Example:

    ```
    $ python pacman.py -f clear
    ```
