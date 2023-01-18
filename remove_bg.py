import tkinter as tk
from tkinter import filedialog
import requests
from PIL import Image, ImageTk

def remove_bg():
    filepath = filedialog.askopenfilename()
    savepath = filedialog.asksaveasfilename(defaultextension=".png")
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(filepath, 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'wsMemvdM6dn9zcnQ96nTroEB'},
    )
    if response.status_code == requests.codes.ok:
        with open(savepath, 'wb') as out:
            out.write(response.content)
        result_label.config(text="Background removed and saved as " + savepath)
        # Show the processed image
        processed_img = Image.open(savepath)
        processed_img = processed_img.resize((300, 300), Image.ANTIALIAS)
        processed_img = ImageTk.PhotoImage(processed_img)
        img_label.config(image=processed_img)
        img_label.image = processed_img
    else:
        result_label.config(text="Error: " + str(response.status_code) + " " + response.text)

root = tk.Tk()
root.title("Remove Background")
root.geometry("250x250")
root.configure(bg='#f0f0f0')

browse_button = tk.Button(root, text="Browse", command=remove_bg,bg='#99ccff',fg='white')
browse_button.pack()

result_label = tk.Label(root, font=("Helvetica", 12),bg='#f0f0f0')
result_label.pack()

img_label = tk.Label(root)
img_label.pack()

root.mainloop()
