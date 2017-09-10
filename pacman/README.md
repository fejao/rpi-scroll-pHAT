rpi-scroll-pHAT/pacman
===============
Display a Pacman character over your scroll-pHAT from Pimoroni

Script was written to not be complicated and re-factored easily, maybe in future adding for *scrll-PHET-HD* also

# Usage
The arguments that can be used with the script:

```
$ python space-invaders.py [-h] [-v] [-b BRIGHTNESS] [-dt DANCE_TIMES]
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
  * Set the dance pause interval in seconds, default: 0.5
* **-pp PAUSE\_PULSE, --pause-pulse PAUSE\_PULSE**
  * Set the pulse pause interval in seconds, default: 0.25
* **-ps PAUSE\_SCROLL, --pause-scroll PAUSE\_SCROLL**
  * Set the scroll pause interval in seconds, default: 0.3
* **-f FUNCTION, --function FUNCTION**
  * Set the function to run ('dance', 'pulse', 'show','scroll-in', 'scroll-out', 'scroll', 'scroll-and-dance', 'scroll-and-pulse', 'clear') type, default: scroll-and-pulse

# Functions
This are the already fixed functions, fell free to add or change

* **dance-left**
  * Open and close the Pacman mouth with the *left orientation*. It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

      ```
      $ python pacman.py -f dance-left -p 2 -dt 3
      ```

      ![Alt text](../pics/pacman/dance-left.gif?raw=true "Pacman dance-left scroll-pHAT")

* **dance-right**
  * Open and close the Pacman mouth with the *right orientation*. It can be used with:
      * **-b/--brightness**
      * **-p/--position**
      * **-dt/--dance_times**
      * **-pd/--pause-dance**
  * Example:

        ```
        $ python pacman.py -f dance-right -p 3 -dt 2
        ```

      ![Alt text](../pics/pacman/dance-right.gif?raw=true "Pacman dance-right scroll-pHAT")

* **pulse-left**
  * Pulse the Pacman figure with the mouth rotate to the left. It can be used with:
      * **-p/--position**
      * **-pp/--pause-pulse**
      * **-pt/--pulse_times**
  * Example:

      ```
      $ python pacman.py -f pulse-left -p 4 -pt 3
      ```

      ![Alt text](../pics/pacman/pulse-left.gif?raw=true "Pacman pulse-left scroll-pHAT")

* **pulse-right**
  * Pulse the Pacman figure. It can be used with:
      * **-p/--position**
      * **-pp/--pause-pulse**
      * **-pt/--pulse_times**
  * Example:

      ```
      $ python pacman.py -f pulse-right -p 1 -pt 2
      ```

      ![Alt text](../pics/pacman/pulse-right.gif?raw=true "Pacman pulse-right scroll-pHAT")

* **show-closed**
  * Display the Pacman figure with the mouth closed. It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-closed -p 5
      ```

      ![Alt text](../pics/pacman/show-closed.jpg?raw=true "Pacman show-closed scroll-pHAT")

* **show-open-left**
  * Display the Pacman figure with the mouth open *left orientated*. It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-open-left -p 2 -b 3
      ```

      ![Alt text](../pics/pacman/show-open-left.jpg?raw=true "Pacman show-open-left scroll-pHAT")

* **show-open-right**
  * Display the Pacman figure with the mouth open *right orientated*. It can be used with:
      * **-b/--brightness**
      * **-p/--position**
  * Example:

      ```
      $ python pacman.py -f show-open-right -p 5 -b 7
      ```

      ![Alt text](../pics/pacman/show-open-right.jpg?raw=true "Pacman show-open-right scroll-pHAT")

* **scroll-left-right-in**
  * Scroll-in the Pacman figure from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-in -ps 0.8
      ```

      ![Alt text](../pics/pacman/scroll-left-right-in.gif?raw=true "Pacman scroll-left-right-in scroll-pHAT")

* **scroll-left-right-out**
  * Scroll-out the Pacman figure from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-out -ps 0.5
      ```

      ![Alt text](../pics/pacman/scroll-left-right-out.gif?raw=true "Pacman scroll-left-right-out scroll-pHAT")

* **scroll-left-right**
  * Scroll-in and out the Pacman figure from *left* to *right*.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right -ps 0.3
      ```

      ![Alt text](../pics/pacman/scroll-left-right.gif?raw=true "Pacman scroll-left-right scroll-pHAT")

* **scroll-left-right-dance**
  * Scroll-in and display the Pacman figure open and closing the mouth and scroll-out *from left to right*. It can be used with:
      * **-b/--brightness**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
      * **-dt/--dance-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-dance -b 5 -pd 0.3 -ps 0.4 -dt 3
      ```

      ![Alt text](../pics/pacman/scroll-left-right-dance.gif?raw=true "Pacman scroll-left-right-dance scroll-pHAT")

* **scroll-left-right-pulse**
  * Scroll-in and display the Pacman figure open and closing the mouth *pulsing* and scroll-out *from left to right*. It can be used with:
      * **-ps/--pause-scroll**
      * **-pp/--pause-pulse**
      * **-pt/--pulse-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-pulse -ps 0.5 -pp 0.4 -pt 3
      ```

      ![Alt text](../pics/pacman/scroll-left-right-pulse.gif?raw=true "Pacman scroll-left-right-pulse scroll-pHAT")

* **scroll-right-left-in**
  * Scroll-in the Pacman figure from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left-in -ps 0.6
      ```

      ![Alt text](../pics/pacman/scroll-right-left-in.gif?raw=true "Pacman scroll-right-left-in scroll-pHAT")

* **scroll-right-left-out**
  * Scroll-out the Pacman figure from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left-out -ps 0.3
      ```

      ![Alt text](../pics/pacman/scroll-right-left-out.gif?raw=true "Pacman scroll-right-left-out scroll-pHAT")

* **scroll-right-left**
  * Scroll-in and out the Pacman figure from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle, use: **show-closed**
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python pacman.py -f scroll-right-left -ps 0.5 -b 7
      ```

      ![Alt text](../pics/pacman/scroll-right-left.gif?raw=true "Pacman scroll-right-left scroll-pHAT")

* **scroll-right-left-dance**
  * Scroll-in and display the Pacman figure open and closing the mouth and scroll-out *from right to left*. It can be used with:
      * **-b/--brightness**
      * **-pd/--pause-dance**
      * **-ps/--pause-scroll**
      * **-dt/--dance-times**
  * Example:

      ```
      $ python pacman.py -f scroll-left-right-dance -b 5 -pd 0.3 -ps 0.4 -dt 3
      ```

      ![Alt text](../pics/pacman/scroll-right-left-dance.gif?raw=true "Pacman scroll-right-left-dance scroll-pHAT")

* **scroll-right-left-pulse**
  * Scroll-in and display the Pacman figure open and closing the mouth *pulsing* and scroll-out *from right to left*. It can be used with:
      * **-ps/--pause-scroll**
      * **-pp/--pause-pulse**
      * **-pt/--pulse-times**
  * Example:

    ```
    $ python pacman.py -f scroll-right-left-pulse -ps 0.5 -pp 0.4 -pt 3
    ```

    ![Alt text](../pics/pacman/scroll-right-left-pulse.gif?raw=true "Pacman scroll-right-left-pulse scroll-pHAT")
