# LEDCUBESimulator
This is a simulator of LEDCUBE.  

This program shows a 3D graph of matplotlib and it can be controled by GUI using tkinter.  
## Requires
- Python3
- matplotlib
- pyperclip
- tkinter
- platform

please install `matplotlib` and `pyperclip`.
`platform` is originally pre-installed in Python and if you don't have `tkinter`, please install it.

## Usage
1. Select each layer
1. Switch LEDs by press buttons
1. Press `update` button.

Once you run `LEDCUBE-simulator.py`, it will automatically open a winsow that shows matplotlib and tkinter.  
512 points are drawn on the matplotlib window.  
You can rotate it by dragging it.
On the tkinter window, there are 64 buttons which can control on/off of LED.
`upgrade`, `copy`, `all turn off`, `all turn on` buttons can update the graph, copy the coordinate data to clipboard, turn off all LED, turn on all LED.  
You can choose layer that you control by using Drop-down list.  


