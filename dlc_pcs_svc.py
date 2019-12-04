from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
def dlc():
    def confirmpurchase():
        pass
    def refreshticket():
        pass
    def dlcquit():
        dlc.destroy()
    # def management_engine():
    dlc = Toplevel()
    dlc.title("コンテンツ贖う")
    dlc.geometry("390x190")
    c = Canvas(dlc, width=1280, height=720)
    frame1 = Frame(dlc,relief = RAISED,width=30,height=10)
    frame1.place(relx=0.0)
    contentshowup = Listbox(frame1,width=30,height=10)
    refreshbtn = Button(dlc, text="更新", width= 18,command=refreshticket)
    purchasebtn = Button(dlc, text="贖う",width= 18, command=confirmpurchase)
    quitbtn = Button(dlc, text="取り消し", width= 18,command=dlcquit)
    refreshbtn.place(x=230,y=20)
    contentshowup.pack()
    purchasebtn.place(x=230,y=50)
    quitbtn.place(x=230,y=140)
    c.pack()
    dlc.mainloop()
