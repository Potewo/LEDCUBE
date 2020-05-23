# LEDCUBESimulator
The simulator of LEDCUBE.  

This program shows 3D graph of matplotlib and it can control by GUI using tkinter.  
## Requires
- Python3
- matplotlib
- pyperclip
- tkinter
- platform

please install `matplotlib` and `pyperclip`.
`platform` is pre-installed in Python.
If you don't have `tkinter`, please install it.

## Usage
1. Select each layer
1. Switch LEDs by press buttons
1. Press `update` button.

If you run `LEDCUBE-simulator.py`, it will automatically open a winsow of matplotlib and tkinter.  
The matplotlib window has 512 points drawn on it.  
You can rotate it by dragging it.
On the tkinter window, there are 64 buttons which can control on/off of LED.
`upgrade`, `copy`, `all turn off`, `all turn on` buttons can update the graph, copy the coordinate data to clipboard, turn off all LED, turn on all LED.  
Drop-down list can choose which layer you control.  


