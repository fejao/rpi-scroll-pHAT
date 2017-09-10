rpi-scroll-pHAT/pacman
===============
Display a Pacman character over your scroll-pHAT from Pimoroni

Script was written to not be complicated and re-factored easily, maybe in future adding for *scroll-pHAT-HD* also

# Usage
The arguments that can be used with the script:

```
$ python pacman.py [-h] [-v] [-b BRIGHTNESS] [-p POSITION] [-dt DANCE_TIMES]
                 [-pt PULSE_TIMES] [-pd PAUSE_DANCE] [-pp PAUSE_PULSE]
                 [-ps PAUSE_SCROLL] [-f FUNCTION]
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
* **-f FUNCTION, --function FUNCTION**
  * Set the function to run ('dance-left', 'dance-right', 'pulse-left', 'pulse-right', 'show-closed', 'show-open-left', 'show-open-right', 'scroll-left-right-in', 'scroll-left-right-out', 'scroll-left-right', 'scroll-left-right-dance', 'scroll-left-right-in-pulse', 'scroll-right-left-in', 'scroll-right-left-out', 'scroll-right-left', 'scroll-right-left-dance', 'scroll-right-left-pulse', 'clear') , default: scroll-left-right-pulse

# Functions
This are the already fixed functions, fell free to add or change

* **dance-left**
  * Open and close the *Pacman* mouth with the *left orientation*.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python pacman.py -f dance-left -p 2 -dt 3
      ```

      ![Imgur Image](http://i.imgur.com/DYvmhCM.gif)

* **dance-right**
  * Open and close the *Pacman* mouth with the *right orientation*.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

        ```
        $ python pacman.py -f dance-right -p 3 -dt 2
        ```

      ![Imgur Image](http://i.imgur.com/IY28On1.gif)

* **pulse-left**
  * Pulse the *Pacman figure* with the mouth rotate to the left.
  * It can be used with:
      * **-p/--position**
      * **-pp/--pause-pulse**
      * **-pt/--pulse_times**
  * Example:

      ```
      $ python pacman.py -f pulse-left -p 4 -pt 3
      ```

      ![Imgur Image](http://i.imgur.com/ZR7NNmm.gif)

* **pulse-right**
  * Pulse the *Pacman figure* with the mouth rotate to the right.
  * It can be used with:
      * **-p/--position**
      * **-pp/--pause-pulse**
      * **-pt/--pulse_times**
  * Example:

      ```
      $ python pacman.py -f pulse-right -p 1 -pt 2
      ```

      ![Imgur Image](http://i.imgur.com/L5iniRf.gif)

* **show-closed**
  * Display the *Pacman figure* with the mouth closed.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-closed -p 5
      ```

      ![Imgur Image](http://i.imgur.com/eipl7QX.jpg)

* **show-open-left**
  * Display the *Pacman figure* with the mouth open *left orientated*.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-open-left -p 2 -b 3
      ```

      ![Imgur Image](http://i.imgur.com/cP8MvpM.jpg)

* **show-open-right**
  * Display the *Pacman figure* with the mouth open *right orientated*.
  * It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-open-right -p 5 -b 7
      ```

      ![Imgur Image](http://i.imgur.com/3X8jInZ.jpg)

* **scroll-left-right-in**
  * Scroll-in the *Pacman figure* from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-in -ps 0.8
      ```

      ![Imgur Image](http://i.imgur.com/Qk1tEQ9.gif)

* **scroll-left-right-out**
  * Scroll-out the *Pacman figure* from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-out -ps 0.5
      ```

      ![Imgur Image](http://i.imgur.com/yODmCvo.gif)

* **scroll-left-right**
  * Scroll-in and out the *Pacman figure* from *left* to *right*.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right -ps 0.3
      ```

      ![Imgur Image](http://i.imgur.com/nscLTig.gif)

* **scroll-left-right-dance**
  * Scroll-in and display the *Pacman figure* open and closing the mouth and scroll-out *from left to right*.
  * It can be used with:
      * **-b/--brightness**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
      * **-dt/--dance-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-dance -b 5 -pd 0.3 -ps 0.4 -dt 3
      ```

      ![Imgur Image](http://i.imgur.com/4KhZnw2.gif)

* **scroll-left-right-pulse**
  * Scroll-in and display the *Pacman figure* open and closing the mouth *pulsing* and scroll-out *from left to right*.
  * It can be used with:
      * **-ps/--pause-scroll**
      * **-pp/--pause-pulse**
      * **-pt/--pulse-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-pulse -ps 0.5 -pp 0.4 -pt 3
      ```

      ![Imgur Image](http://i.imgur.com/aouZp2E.gif)

* **scroll-right-left-in**
  * Scroll-in the *Pacman figure* from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left-in -ps 0.6
      ```

      ![Imgur Image](http://i.imgur.com/iJ2WLei.gif)

* **scroll-right-left-out**
  * Scroll-out the *Pacman figure* from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left-out -ps 0.3
      ```

      ![Imgur Image](http://i.imgur.com/32mHVYL.gif)

* **scroll-right-left**
  * Scroll-in and out the *Pacman figure* from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left -ps 0.5 -b 7
      ```

      ![Imgur Image](http://i.imgur.com/a01Ljya.gif)

* **scroll-right-left-dance**
  * Scroll-in and display the *Pacman figure* open and closing the mouth and scroll-out *from right to left*.
  * It can be used with:
      * **-b/--brightness**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
      * **-dt/--dance-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-dance -b 5 -pd 0.3 -ps 0.4 -dt 3
      ```

      ![Imgur Image](http://i.imgur.com/GFdWND3.gif)

* **scroll-right-left-pulse**
  * Scroll-in and display the *Pacman figure* open and closing the mouth *pulsing* and scroll-out *from right to left*.
  * It can be used with:
      * **-ps/--pause-scroll**
      * **-pp/--pause-pulse**
      * **-pt/--pulse-times**
  * Example:

    ```
    $ python pacman.py -f scroll-right-left-pulse -ps 0.5 -pp 0.4 -pt 3
    ```

    ![Imgur Image](http://i.imgur.com/bTZe3tQ.gif)
