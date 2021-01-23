import sys
import json
import requests
import pyperclip
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"

class shibaboard(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("shibaboard")

        # dynamic scaling ? ? ? 
        x = self.winfo_screenwidth()
        y = self.winfo_screenheight()
        self.geometry(f"{x // 4}x{y // 2}")
        self.update()
        
        # We're getting a link to an image
        self.r = requests.get(url)
        self.json_data = self.r.json()
        self.json_data = json.dumps(self.json_data)
        self.json_data = self.json_data[2:-2]

        # Sending another request to the link we just got
        self.r = requests.get(self.json_data)
        self.pil_image = Image.open(BytesIO(self.r.content))
        self.image = ImageTk.PhotoImage(self.pil_image.resize((self.winfo_width(),self.winfo_height()), Image.ANTIALIAS))

        # Put image on label
        self.shiba_label = tk.Label(image=self.image)
        self.shiba_label.pack()

        # Right-click Pop-up menu
        self.menu = tk.Menu(self, tearoff = 0)
        self.menu.add_command(label = "Copy Link", command = lambda:pyperclip.copy(self.json_data))
        self.menu.add_command(label = "Exit", command = lambda:sys.exit(0))
        self.shiba_label.bind("<Button-3>", self.evt)

        self.mainloop()

    # Event handler            
    def evt(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()


while True:
    shibaboard()
