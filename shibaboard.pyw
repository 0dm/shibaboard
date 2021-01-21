import os
import sys
import json
import tkinter as tk
import requests
from io import BytesIO
from PIL import Image, ImageTk

url = "http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true"

while 1:
    root = tk.Tk()
    root.title("shibaboard")


    r = requests.get(url)
    json_data = r.json()
    json_data = json.dumps(json_data)
    json_data = json_data[2:-2]

    r = requests.get(json_data)
    pilImage = Image.open(BytesIO(r.content))
    image = ImageTk.PhotoImage(pilImage)
    label = tk.Label(image=image)
    label.pack()
    root.mainloop()

