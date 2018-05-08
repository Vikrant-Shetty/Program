from tkinter import *
from tkinter import ttk
import time
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
top = Tk()
top.title("Alarm clock")
def addfile():
    global name
    name=askopenfilename(initialdir=r"C:\Users\Vikrant\AppData\Local\Programs\Python\Python36\Lib\tkinter",
                               filetypes =(("WAV files", "*.wav"),("All Files","*.*")),
                               title = "Choose a file."
                               )
def stop():
    PlaySound(None, SND_FILENAME)
def SubmitButton():
    global AlarmTime
    AlarmTime = entry1.get()
    Message1()
    CurrentTime = time.strftime("%H:%M")
    while AlarmTime != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime == CurrentTime:
        PlaySound(name, SND_FILENAME | SND_LOOP | SND_ASYNC)
def Snooze():
    global AlarmTime
    PlaySound(None, SND_FILENAME)
    si=entry2.get()
    re=AlarmTime.split(":")
    min=int(re[1])+int(si)
    AlarmTime=re[0]+":"+str(min)
    CurrentTime = time.strftime("%H:%M")
    while AlarmTime != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
        time.sleep(1)
    if AlarmTime == CurrentTime:
        PlaySound(name, SND_FILENAME | SND_LOOP | SND_ASYNC)
def Message1():
    label2.config(text="the Alarm time is Counting...")
    messagebox.showinfo(title='Alarm clock', message='Alarm will Ring at {}'.format(AlarmTime))
    button3 = ttk.Button(frame1, text="Stop", command=stop)
    button3.pack()
    button4 = ttk.Button(frame1, text="Snooze", command=Snooze)
    button4.pack()
frame1 = ttk.Frame(top)
frame1.pack()
frame1.config(height=250, width=150)
label1 = ttk.Label(frame1, text="Enter the Alarm time :")
label1.pack()
entry1 = ttk.Entry(frame1, width=30)
entry1.pack()
entry1.insert(3, "example - 13:15")
label2 = ttk.Label(frame1, text="Enter snooze interval in mins :")
label2.pack()
entry2 = ttk.Entry(frame1, width=30)
entry2.pack()
button1 = ttk.Button(frame1, text="Add music file", command=addfile)
button1.pack()
button2 = ttk.Button(frame1, text="submit", command=SubmitButton)
button2.pack()
label2 = ttk.Label(frame1)
label2.pack()
top.mainloop()
