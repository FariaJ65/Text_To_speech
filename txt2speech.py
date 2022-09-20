from cgitb import text
import tkinter as tk
from tkinter import *
import pyttsx3

engine=pyttsx3.init()

def speaknow():
    engine.say(textv.get())
    for voice in engine.getProperty('voices'):
        print(f"Voice: {voice.name}")
    engine.setProperty('voice', voice.id)  # first male then female voice 
    engine.runAndWait()
    engine.stop()

root=Tk()

textv=StringVar()

obj=LabelFrame(root,text="Text to speech",font=20,bd=2)
obj.pack(fill="both",expand="yes",padx=10,pady=10)

lbl=Label(obj,text="Text",font=30)
lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=2)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text="speak",font=20,bg="black",fg="white",command=speaknow)
btn.pack(side=tk.LEFT,padx=10)

root.title("Text To Speech")
root.geometry("400x200")
root.configure(bg="gray")
root.resizable(False,False)

root.mainloop()