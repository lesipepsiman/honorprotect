import pygetwindow as gw
from tkinter import *
import tkinter as tk

from PIL import Image, ImageTk
import time

root = tk.Tk()
label = tk.Label(root)
label.pack()

def show_image(image_path, fullscreen=False):
    image = Image.open(image_path)
    if fullscreen:
        image = image.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.LANCZOS)
    else:
        image = image.resize((529, 199), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo
    if fullscreen:
        root.attributes("-fullscreen", True)
    else:
        root.attributes("-fullscreen", False)

def read_txt_file(filename):
    with open(filename, 'r') as file:
        return file.read().strip()  # 파일 내용을 읽고 양쪽 공백 제거하여 반환

def exct():
    window_name = read_txt_file("config.txt")
    titles = gw.getAllTitles()
    if window_name in titles:
        show_image('clofol_ko.png', fullscreen=True)
        root.wm_attributes("-topmost", 1)
    else:
        show_image('sleep_ko.png', fullscreen=False)
        root.lower()

#def on_window_configure(event):
    #if not root.attributes('-fullscreen'):
        #root.update_idletasks()
        #oot.deiconify()

#root.bind('<Configure>', on_window_configure)


while True:
    exct()
    root.update()
    time.sleep(1)
