[![中文](https://img.shields.io/badge/切换中文-CN-red.svg)](https://github.com/Ethan-Ming/Cyberpunk_AVS/blob/main/README.ch.md)
# Functional Braindance

This project is an enhanced cosplay prop from Cyberpunk 2077 that does the Audio-Visual-Stimulation (AVS) function. The prop is based on the Braindance (BD) device from the game and can be used to create immersive experiences.

<img src="https://i.imgur.com/1NuFsKd_d.webp?maxwidth=760&fidelity=grand" width="50%" height="50%">

source credie:imgur.com/gallery/hycC6M2

## Features

- Switch colors and preset profiles with a button press
- Default profile includes wakeup helper mode and sleep introduce mode
- Change RGB color, session length, and add or remove new profiles in the `main.py` file

## Bill of Materials

- 1 x Microswitch
- 2 x 5050 RGB LEDs or KY-009
- 1 x ESP32 board
- 1 x 3.7v vibrate motor (vibration feature is still work-in-progress)
- 1 x 2N2222
- 1 x 260ohm resistor 


## Installation

1. Clone the repository
2. know what your're doing
3. Upload the `main.py` file to your ESP32 board
4. Connect the microswitch and RGB LEDs to the ESP32 board as shown in the schematic
5. Power on the device and enjoy!

## Schematic and Simlation

https://wokwi.com/projects/380527426842242049

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
