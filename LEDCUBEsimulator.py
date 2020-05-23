# coding: UTF-8
import tkinter as tk
from tkinter import ttk
import matplotlib

matplotlib.use('TkAgg')
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

import pyperclip

import platform

mac = False
otherOS = False
PLATFORM = platform.system()
if PLATFORM == "Darwin":
    mac = True
else:
    otherOS = True

LED_VALUE = 8

LED_state = list()
for i in range(LED_VALUE):
    LED_state.append(list())
    for ii in range(LED_VALUE):
        for iii in range(LED_VALUE):
            LED_state[i].append(1)

# 座標のリストを作る
def make_axes_list(value):
    axes = list()
    for i in range(LED_VALUE):
        axes.append(list())
        for ii in range(LED_VALUE):
            for iii in range(LED_VALUE):
                if value == "1x":
                    axes[i].append(ii + 1)
                if value == "2":
                    axes[i].append(0)
                if value == "1y":
                    axes[i].append(iii + 1)
                if value == "1z":
                    axes[i].append(i + 1)

    return axes

# 二重リストをフラットにする
def flatten_the_list(list_):
    flat_list = [flatten for inner in list_ for flatten in inner]
    return flat_list

# 最初にグラフを描画するためのflag
flag = True
x = make_axes_list("1x")
x2 = make_axes_list("2")
y = make_axes_list("1y")
y2 = make_axes_list("2")
z = make_axes_list("1z")
z2 = make_axes_list("2")

root = tk.Tk()
root.geometry("400x600")
root.title("LEDCUBE simulator")


f1 = tk.Frame(root, relief=tk.RIDGE)
f2 = tk.Frame(root, relief=tk.RIDGE, width=LED_VALUE * 50, height=LED_VALUE * 50)
f1.pack(expand=True)
f2.pack(expand=True)

def cb_selected(event):
    layer_state = int(cb.get().split("_")[1]) - 1
    for i in range(LED_VALUE ** 2):
        if LED_state[layer_state][i] == 1:
            if mac:
                led_bt_list[i]["highlightbackground"] = "red"
            if otherOS:
                led_bt_list[i]["bg"] = "#f80206"
        else:
            if mac:
                led_bt_list[i]["highlightbackground"] = "white"
            if otherOS:
                led_bt_list[i]["bg"] = "#d9d9d9"

# レイヤー選択
cb = ttk.Combobox(f1, state='readonly')
strings_ = ""
for i in range(LED_VALUE):
    strings_ += ("Layer_" + str(i + 1) + " ")
    cb['values'] = strings_
cb.bind('<<ComboboxSelected>>', cb_selected)
cb.pack(expand=True)

# グラフの更新
def update():
    plt.cla()
    ax.scatter(flatten_the_list(x), flatten_the_list(y), flatten_the_list(z))
    plt.show()
    info_label["text"] = "info: updated"

# クリップボードに座標データをコピー
def copy():
    #print(x)
    #output = [0 if i == "0" else 1 for i in x]
    output = list()
    for i in x:
        output.append([0 if j == 0 else 1 for j in x])
    # pyperclip.copy(str(x) + "\n" + str(y) + "\n" + str(z) + "\n")
    pyperclip.copy(str(output))
    info_label["text"] = "info: copied"

# 全てのLEDを消す
def all_turn_off():
    global x, x2, y, y2, z, z2
    global LED_state
    x = make_axes_list("2")
    x2 = make_axes_list("1x")
    y = make_axes_list("2")
    y2 = make_axes_list("1y")
    z = make_axes_list("2")
    z2 = make_axes_list("1z")
    LED_state = list()
    for i in range(LED_VALUE):
        LED_state.append(list())
        for ii in range(LED_VALUE):
            for iii in range(LED_VALUE):
                LED_state[i].append(0)

        for j in range(LED_VALUE ** 2):
            if mac:
                led_bt_list[j]["highlightbackground"] = "white"
            if otherOS:
                led_bt_list[j]["bg"] = "#d9d9d9"

    info_label["text"] = "info: all LED are turned off"

# 全てのLEDを点ける
def all_turn_on():
    global x, x2, y, y2, z, z2
    global LED_state
    x = make_axes_list("1x")
    x2 = make_axes_list("2")
    y = make_axes_list("1y")
    y2 = make_axes_list("2")
    z = make_axes_list("1z")
    z2 = make_axes_list("2")
    LED_state = list()
    for i in range(LED_VALUE):
        LED_state.append(list())
        for ii in range(LED_VALUE):
            for iii in range(LED_VALUE):
                LED_state[i].append(1)
    for j in range(LED_VALUE ** 2):
        if mac:
            led_bt_list[j]["highlightbackground"] = "red"
        if otherOS:
            led_bt_list[j]["bg"] = "#f80206"

    info_label["text"] = "info: all LED are turned on"

# 個々のLEDの点滅を切り替える
def turn_led(event):
    bt_number = int(event.widget["text"])
    layer_state = int(cb.get().split("_")[1]) - 1
    if LED_state[layer_state][bt_number] == 0:
        if mac:
            event.widget["highlightbackground"] = "red"
        if otherOS:
            event.widget["bg"] = "#f80206"
        LED_state[layer_state][bt_number] = 1
    elif LED_state[layer_state][bt_number] == 1:
        if mac:
            event.widget["highlightbackground"] = "white"
        if otherOS:
            event.widget["bg"] = "#d9d9d9"
        LED_state[layer_state][bt_number] = 0
    def replace(p_value):
        x[p_value][bt_number], x2[p_value][bt_number] = x2[p_value][bt_number], x[p_value][bt_number]
        y[p_value][bt_number], y2[p_value][bt_number] = y2[p_value][bt_number], y[p_value][bt_number]
        z[p_value][bt_number], z2[p_value][bt_number] = z2[p_value][bt_number], z[p_value][bt_number]
    try:
        replace(int(cb.get().split("_")[1]) - 1)
    except:
        info_label["text"] = "info: Please select a Layer"


update_bt = tk.Button(f1, text='update', command=update)
update_bt.pack(expand=True)

copy_bt = tk.Button(f1, text='copy', command=copy)
copy_bt.pack(expand=True)

all_turn_off_bt = tk.Button(f1, text='all turn off', command=all_turn_off)
all_turn_off_bt.pack(expand=True)

all_turn_on_bt = tk.Button(f1, text='all turn on', command=all_turn_on)
all_turn_on_bt.pack(expand=True)

info_label = tk.Label(f1, text='info: ')
info_label.pack(expand=True)

# 個々のLEDを操作するボタン
value = 0
led_bt_list = list()
for i in range(LED_VALUE ** 2):
    led_bt_list.append(tk.Button(f2, text=str(value), width=4, height=2))
    led_bt_list[i].bind("<1>", turn_led)
    led_bt_list[i].grid(row=i // LED_VALUE, column=i % LED_VALUE)
    value += 1

# グラフの作成
if flag:
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(flatten_the_list(x), flatten_the_list(y), flatten_the_list(z))
    plt.show()
    all_turn_on()
flag = False

root.mainloop()
