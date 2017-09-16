rpi-scroll-pHAT/twitter
===============
Display a Pacman character over your scroll-pHAT from Pimoroni

Script was written to not be complicated and re-factored easily, maybe in future adding for *scrll-PHET-HD* also

# 1 - Before using
##  1.1 - Create a Twitter Dev Account
* You need to setup a twitter developer account for setting your **consumer\_key, consumer\_secret, access\_token** and **access\_token\_secret**.
* Take a look at the video to see how to setup your developer account.

[![Alt text](https://img.youtube.com/vi/1p8veF-sIIo/0.jpg)](https://www.youtube.com/watch?v=1p8veF-sIIo)


## 1.2 - Configuration File
After that you created your account (if you don't have any) enter the credentials from your created API to the **twitter_config.py** file.

```
consumer_key="xxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

## 1.3 - Install depancencies
* You have to install the python twitter API:

```
$ sudo pip install tweepy
```

+ [Here you can take a look at the source code](https://github.com/tweepy/tweepy)

# 2 - Usage
The arguments that can be used with the script:

```
$ python space-invaders.py [-h] [-v] [-b BRIGHTNESS] [-dt DANCE_TIMES]
                  [-pt PULSE_TIMES] [-pd PAUSE_DANCE] [-pp PAUSE_PULSE]
                  [-ps PAUSE_SCROLL] [-po PAUSE_SHOW] [-pts PAUSE_TEXT_SCROLL]
                  [-u USER_NAME] [-nt NUM_TWEETS] [-m MESSAGE] [-f FUNCTION]
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
* **-pts PAUSE\_TEXT\_SCROLL, --pause-text-scroll PAUSE\_TEXT\_SCROLL**
  * Set the text scroll pause interval in seconds, default: 0.2
* **-u USER\_NAME, --user-name USER\_NAME**
  * Set the Twitter user name to fetch the tweets, default: fejao
* **-nt NUM\_TWEETS, --num-tweets NUM\_TWEETS**
  * Set the how many last tweets to be fetched, default: 1
* **-m MESSAGE, --message MESSAGE**
  * Display a message, default: test message
* **-f FUNCTION, --function FUNCTION**
  * Set the function to run ('logo-show', 'logo-pulse', 'logo-scroll-in', 'logo-scroll-out', 'logo-scroll', 'logo-scroll-pulse', 'logo-scroll-right-left-in', 'logo-scroll-right-left-out', 'logo-scroll-right-left', 'logo-scroll-right-left-pulse', 'logo-show-inverted', 'logo-pulse-inverted', 'logo-scroll-in-inverted', 'logo-scroll-out-inverted', 'logo-scroll-inverted', 'logo-scroll-pulse-inverted', 'logo-scroll-right-left-in-inverted', 'logo-scroll-right-left-out-inverted', 'logo-scroll-right-left-inverted', 'logo-scroll-right-left-pulse-inverted', 'message-write', 'fetch', 'fetch-with-scrolling-logo', 'clear'), default: fetch-with-scrolling-logo

# 3 - Functions
This are the already fixed functions, fell free to add or change

## 3.1 - Message
Functions to display text at your *scroll-pHAT*

* **fetch-with-logo**
  * Display the *Twitter Logo* and the *fetched tweets* from user.
  * It can be used with:
      * **-pt/--pulse-times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
      * **-u/--user-name**
      * **-nt/--num-tweets**
  * Example:

      ```
      $ python twitter.py -f fetch-with-logo -pt 3 -pp 0.7 -ps 0.23 -u '<TWITTER_NAME>' -nt 2
      ```

      ![Imgur Image](http://i.imgur.com/qj4PWU8.gif)

* **fetch**
  * Display the *fetched tweets* from user.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
      * **-u/--user-name**
      * **-nt/--num-tweets**
  * Example:

      ```
      $ python twitter.py -f fetch -b 3 -pt 3 -pp 0.7 -ps 0.23 -u '<TWITTER_NAME>' -nt 3
      ```

      ![Imgur Image](http://i.imgur.com/CPogccT.jpg)

* **message-write**
  * Display a text at your *scroll-pHAT*.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
      * **-m/--message**
  * Example:

      ```
      $ python twitter.py -f message-write -b 4 -ps 0.2 -m '<YOUR_TEXT>'
      ```

      ![Imgur Image](http://i.imgur.com/nGxIHbY.jpg)

## 3.2 - Logo
## 3.2.1 - Logo Show
* **logo-show**
  * Display the *Twitter Logo*.
  * It can be used with:
      * **-b/--brightness**
      * **-po/--pause-show**
  * Example:

      ```
      $ python twitter.py -f logo-show -b 3 -po 3.2
      ```

      ![Imgur Image](http://i.imgur.com/n3lYp3X.jpg)

## 3.2.2 - Logo Pulse
* **logo-pulse**
  * Display the *Twitter Logo* pulsing.
  * It can be used with:
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python twitter.py -f logo-pulse -pt 3 -pp 0.2
      ```

      ![Imgur Image](http://i.imgur.com/7GT0okK.gif)

## 3.2.3 - Logo Scroll
* **logo-scroll-in**
  * Scroll-in the *Twitter Logo* from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-in -b 7 -ps 0.2
      ```

      ![Imgur Image](http://i.imgur.com/RNsm0Hx.gif)

* **logo-scroll-out**
  * Scroll-out the *Twitter Logo* from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-out -b 3 -ps 1.5
      ```

      ![Imgur Image](http://i.imgur.com/tiHAKrX.gif)

* **logo-scroll**
  * Scroll-in and out the *Twitter Logo* from *left* to *right*.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll -b 6 -ps 2.3
      ```

      ![Imgur Image](http://i.imgur.com/KalbSlm.gif)

* **logo-scroll-pulse**
  * Scroll-in and out the *Twitter Logo* from *left* to *right* pulsing in the middle.
  * It can be used with:
      * **-pt/--pulse-times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-pulse -pt 2 -pp 0.8 -ps 0.75
      ```

      ![Imgur Image](http://i.imgur.com/7zOIVbQ.gif)

## 3.2.3 - Logo Scroll Right to the Left
* **logo-scroll-right-left-in**
  * Scroll-in the *Twitter Logo* from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-in -b 3 -ps 0.95
      ```

      ![Imgur Image](http://i.imgur.com/r5eOx1a.gif)

* **logo-scroll-right-left-out**
  * Scroll-out the *Twitter Logo* from *right* to *left*.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-out -b 4 -ps 0.27
      ```

      ![Imgur Image](http://i.imgur.com/uul9wFi.gif)

* **logo-scroll-right-left**
  * Scroll-in and out the *Twitter Logo* from *right* to *left*.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left -b 6 -ps 0.45
      ```

      ![Imgur Image](http://i.imgur.com/P5jULMW.gif)

* **logo-scroll-right-left-pulse**
  * Scroll-in and out the *Twitter Logo* from *right* to *left* pulsing in the middle.
  * It can be used with:
      * **-pt/--pulse-times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-pulse -pt 4 -pp 0.3 -ps 0.72
      ```

      ![Imgur Image](http://i.imgur.com/7LgyLcS.gif)

## 3.3 - Logo Inverted
## 3.3.1 - Logo Inverted Show
* **logo-show-inverted**
  * Display the *Twitter Logo* inverted.
  * It can be used with:
      * **-b/--brightness**
      * **-po/--pause-show**
  * Example:

      ```
      $ python twitter.py -f logo-show-inverted -b 3 -po 3.2
      ```

      ![Imgur Image](http://i.imgur.com/Uqry8sd.jpg)

## 3.3.2 - Logo Inverted Pulse
* **logo-pulse-inverted**
  * Display the *Twitter Logo* pulsing inverted.
  * It can be used with:
      * **-pt/--pulse_times**
      * **-pp/--pause-pulse**
  * Example:

      ```
      $ python twitter.py -f logo-pulse-inverted -pt 3 -pp 0.2
      ```

      ![Imgur Image](http://i.imgur.com/CrZtkZk.gif)

## 3.3.3 - Logo Inverted Scroll
* **logo-scroll-in-inverted**
  * Scroll-in the *Twitter Logo* from *left* to *right* inverted.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-in-inverted -b 7 -ps 0.2
      ```

      ![Imgur Image](http://i.imgur.com/WXm7NAD.gif)

* **logo-scroll-out-inverted**
  * Scroll-out the *Twitter Logo* from *left* to *right*.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-out-inverted -b 3 -ps 1.5
      ```

      ![Imgur Image](http://i.imgur.com/t3TClDu.gif)

* **logo-scroll-inverted**
  * Scroll-in and out the *Twitter Logo* from *left* to *right* inverted.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-inverted -b 6 -ps 2.3
      ```

      ![Imgur Image](http://i.imgur.com/Fi76cRv.gif)

* **logo-scroll-pulse**
  * Scroll-in and out the *Twitter Logo* from *left* to *right* pulsing in the middle inverted.
  * It can be used with:
      * **-pt/--pulse-times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-pulse-inverted -pt 2 -pp 0.8 -ps 0.75
      ```

      ![Imgur Image](http://i.imgur.com/507UEm7.gif)

## 3.3.4 - Logo Inverted Scroll Right to Left
* **logo-scroll-right-left-in-inverted**
  * Scroll-in the *Twitter Logo* from *right* to *left* inverted.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-in-inverted -b 3 -ps 0.95
      ```

      ![Imgur Image](http://i.imgur.com/EJPyVdf.gif)

* **logo-scroll-right-left-out-inverted**
  * Scroll-out the *Twitter Logo* from *right* to *left* inverted.
  * It will scroll till the middle **-1** position, to display at the middle,
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-out-inverted -b 4 -ps 0.27
      ```

      ![Imgur Image](http://i.imgur.com/Y3pReuC.gif)

* **logo-scroll-right-left-inverted**
  * Scroll-in and out the *Twitter Logo* from *right* to *left* inverted.
  * It can be used with:
      * **-b/--brightness**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-inverted -b 6 -ps 0.45
      ```

      ![Imgur Image](http://i.imgur.com/XA8bg0u.gif)

* **logo-scroll-right-left-pulse-inverted**
  * Scroll-in and out the *Twitter Logo* from *right* to *left* pulsing in the middle inverted.
  * It can be used with:
      * **-pt/--pulse-times**
      * **-pp/--pause-pulse**
      * **-ps/--pause-scroll**
  * Example:

      ```
      $ python twitter.py -f logo-scroll-right-left-pulse-inverted -pt 4 -pp 0.3 -ps 0.72
      ```

      ![Imgur Image](http://i.imgur.com/CRA6YIA.gif)

## 3.4 - Other functions
* **clear**
  * Clears the *scroll-pHAT* display
  * Example:

    ```
    $ python twitter.py -f clear
    ```
