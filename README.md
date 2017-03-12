# WallPiSense
A simple game for Raspberry Pi Sense Hat 

# Introduction
The Raspberry Pi Sense Hat is a great device for messing around with your favourite computer. While exploring the 8x8 matrix and joystick, I found amusing to improvise a game like that.

# Requirements
## Hardware
* [Sense Hat](https://www.raspberrypi.org/products/sense-hat/): the add-on board that enables the game
* Raspberry Pi Model 1, 2 and 3
  * Note that the Sense Hat is not compatible with Raspberry Pi 1 Model B

## Software
Installing python3-sense-hat should be the only requirement
```bash
sudo apt-get install python3-sense-hat
```

# Playing
Use the joystick to move your hero to avoid walls progressing from right to left
```bash
sudo python3 wallpisense.py
```

Note that `sudo` is required by Sense Hat for controlling the 8x8 matrix.

Enjoy!
