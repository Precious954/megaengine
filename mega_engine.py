import os
import sys
import time
import ctypes
from ctypes import wintypes
from tkinter import Tk, filedialog, StringVar, Button, Label, Entry
from PIL import Image, ImageTk
import win32api
import win32con
import win32gui
import threading

class MegaEngine:
    def __init__(self):
        self.root = Tk()
        self.root.title("MegaEngine - Customize and Animate Desktop Icons")
        
        self.icon_path = StringVar()
        self.icon_path.set("Select an icon image...")
        
        self.animation_speed = StringVar()
        self.animation_speed.set("Enter animation speed in seconds...")

        Label(self.root, text="Icon Image:").pack()
        Entry(self.root, textvariable=self.icon_path, width=50).pack()
        Button(self.root, text="Browse", command=self.select_icon).pack()

        Label(self.root, text="Animation Speed:").pack()
        Entry(self.root, textvariable=self.animation_speed, width=50).pack()

        Button(self.root, text="Apply", command=self.apply_customization).pack()
        
        self.root.mainloop()

    def select_icon(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.ico *.png *.jpg *.jpeg")])
        if file_path:
            self.icon_path.set(file_path)

    def apply_customization(self):
        try:
            icon_path = self.icon_path.get()
            animation_speed = float(self.animation_speed.get())
            
            if not os.path.exists(icon_path):
                raise FileNotFoundError("Icon image not found.")

            threading.Thread(target=self.animate_icon, args=(icon_path, animation_speed)).start()
        except Exception as e:
            print(f"Error: {e}")

    def animate_icon(self, icon_path, animation_speed):
        while True:
            # Simplified example for changing icon
            # For real implementation, you would need to interact with desktop icons directly
            shell32 = ctypes.WinDLL('shell32', use_last_error=True)
            if shell32 is not None:
                print(f"Animating icon using {icon_path}")
                # Real icon change logic would go here
            time.sleep(animation_speed)

if __name__ == "__main__":
    MegaEngine()