from tkinter import *
from tkinter import messagebox
from pytube import YouTube

def convert():
    link = url_entry.get()
    if len(link)==0:
        messagebox.showinfo(title="Note",message="Please don't leave the link field empty")
    else:
        Label(window,text="Downloading",font=("courier",12),bg="white").place(x=175,y=330)
        convert = YouTube(link).streams.first().download()
        if convert:
            Label(window, text="Downloaded Succesfully", font=("courier", 12), bg="white").place(x=175, y=330)
            url_entry.delete(0,END)
        else:
            Label(window, text="Oops Try Again", font=("courier", 12), bg="white").place(x=175, y=330)
#Tk configuration
window = Tk()
window.title("Youtube Mp4 Converter")
window.minsize(670,500)
window.maxsize(670,500)
window.config(bg="white")
window.iconbitmap("C:\\Users\\Ziraoui_Anas\\Desktop\\resume\\pythonProject\\download.ico")

#configuring the Canvas
image_convert = PhotoImage(file="youtube.png")
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=image_convert)
canvas.config(bg="white")
canvas.place(x=210,y=80)

#configuring Entry :
url_entry = Entry(window,text="",font=("courier",12))
url_entry.place(x=100,y=290,width=500)
url_entry.focus()
#configuring labels :
Label(window,text="Welcome to the fastest  Converter",font=("courier",12),bg="white").place(x=185,y=30)
url = Label(window,text="URL : ",font=("courier",12,"bold"),bg="white")
url.place(x=35,y=290)

#configuring Buttons
Button(window,text="Convert",font=("courier",12),command=convert).place(x=150,y=390,width=150)
Button(window,text="Quit",font=("courier",12),command=window.destroy).place(x=340,y=390,width=150)

window.mainloop()




