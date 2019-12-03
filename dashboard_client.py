from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *

def refreshticket():
    pass
def deletecurrent():
    if tm.askokcancel("ご注意ください","注意：ご記録は完全に削除されます、本当に長いです"):
        pass
    else:
        pass

# def management_engine():
dme = Tk()
dme.title("ハイスクール")
dme.geometry("1280x720")
c = Canvas(dme, width=1280, height=720)
frame1 = Frame(dme,relief = RAISED,width=450,height=600)
frame1.place(relx=0.0)
myshowup = Listbox(frame1,width=450,height=600)
frame2 = Frame(dme,relief = RAISED,width=450,height=600)
frame2.place(relx=0.5)
worldshowup = Listbox(frame2,width=450,height=600)
refreshbtn = Button(dme, text="更新", command=refreshticket)
clearbtn = Button(dme, text="レコードを削除します", command=deletecurrent)


refreshbtn.pack()
clearbtn.pack()
myshowup.pack()
worldshowup.pack()
c.pack()
dme.mainloop()
