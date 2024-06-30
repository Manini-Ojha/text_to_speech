#testing the imported library


'''
import pyttsx3
engine = pyttsx3.init()
engine.say('Hello sir, how may I help you sir.')
engine.runAndWait()
'''


import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyttsx3
import os

root=Tk()
root.title("Text to speech")
root.geometry("900x450+200+200")
root.resizable(False,False)
root.configure(bg="#9BE8D8")

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0,END)
    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')
    

    def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            engine.say(text)
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            engine.say(text)
            engine.runAndWait()
        

    if(text):
        if(speed == "Fast"):
            engine.setProperty('rate',250)
            setvoice()
        elif(speed == 'Normal'):
            engine.setProperty('rate', 150)
            setvoice()
        else:
            engine.setProperty('rate',60)
            setvoice()


def download():
     text = text_area.get(1.0,END)
     gender = gender_combobox.get()
     speed = speed_combobox.get()
     voices = engine.getProperty('voices')

     def setvoice():
        if(gender == 'Male'):
            engine.setProperty('voice', voices[0].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()
        else:
            engine.setProperty('voice', voices[1].id)
            path=filedialog.askdirectory()
            os.chdir(path)
            engine.save_to_file(text,'text.mp3')
            engine.runAndWait()

     if(text):
         if(speed == "Fast"):
             engine.setProperty('rate',250)
             setvoice()
         elif(speed == 'Normal'):
                engine.setProperty('rate', 150)
                setvoice()
         else:
                engine.setProperty('rate',60)
                setvoice()

            
#icon

image_icon=PhotoImage(file="speak.png")
root.iconphoto(False,image_icon)


#Top Frame

Top_frame=Frame(root,bg="white", width=900,height=75)
Top_frame.place(x=0,y=0)

Logo=PhotoImage(file="tts.png")
Label(Top_frame,image=Logo,bg="white").place(x=10,y=2)

Label(Top_frame,text="TEXT TO SPEECH", font="constantia 20 bold",bg="white",fg="#068FFF").place(x=100,y=25)


#

text_area=Text(root,font="Robote 20", bg="white",relief=GROOVE,wrap=WORD)
text_area.place(x=50,y=150,width=400,height=250)

'''
scrollbar=Scrollbar(text_area)
#scrollbar.place(x=50,y=150,width=400,height=250)
scrollbar.pack(side=RIGHT, fill=Y)
mylist = Listbox(text_area, yscrollcommand=scrollbar.set)
for line in range(100):
    text = text_area.get(1.0,END)
    mylist.insert(END,text)
mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
'''

Label(root,text="VOICE",font="arial 15 bold", bg="#9BE8D8", fg="white").place(x=580,y=160)
Label(root,text="SPEED",font="arial 15 bold", bg="#9BE8D8", fg="white").place(x=760,y=160)

gender_combobox=Combobox(root,values=["Male","Female"],font="century 14",state='r',width=10)
gender_combobox.place(x=550,y=200)
gender_combobox.set('Male')

speed_combobox=Combobox(root,values=['Fast', 'Normal', 'Slow'], font="century 14", state='r',width=10)
speed_combobox.place(x=730,y=200)
speed_combobox.set('Normal')


imageicon=PhotoImage(file="speak.png")
btn=Button(root,text="Speak",compound=LEFT, image=imageicon ,width=130,bg="white",fg="black",font="century 14 bold",command=speaknow)
btn.place(x=550,y=280)

imageicon2=PhotoImage(file="download2.png")
save=Button(root,text="Save",compound=LEFT, image=imageicon2 ,width=130,bg="white",fg="#068FFF",font="century 14 bold",command=download)
save.place(x=730,y=280)


root.mainloop()
#F3FDE8
