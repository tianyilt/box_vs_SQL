from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
import CASClient
import dlc_pcs_svc
def purchase():
    dlc_pcs_svc.dlc()
def refreshticket():
    pass
def deletecurrent():
    if tm.askokcancel("ご注意ください","注意：ご記録は完全に削除されます、本当に長いです"):
        pass
    else:
        pass
def login():
    dme.destroy()
    CASClient.CASClient()
# def management_engine():
dme = Tk()
dme.title("ハイスクール")
dme.geometry("600x400")
c = Canvas(dme, width=1280, height=720)
frame1 = Frame(dme,relief = RAISED,width=30,height=60)
frame1.place(relx=0.0)
myshowup = Listbox(frame1,width=30,height=60)
frame2 = Frame(dme,relief = RAISED,width=30,height=60)
frame2.place(relx=0.3)
worldshowup = Listbox(frame2,width=30,height=60)
refreshbtn = Button(dme, text="更新", width= 18,command=refreshticket)
clearbtn = Button(dme, text="レコードを削除します", width= 18,command=deletecurrent)
loginbtn=Button(dme,text="ログイン",width= 18,command=login)
purchasebtn = Button(dme, text="コンテンツを贖います",width= 18, command=purchase)
quitbtn = Button(dme, text="ゲーム終了", width= 18,command=quit)
refreshbtn.place(x=430,y=40)
clearbtn.place(x=430,y=70)
myshowup.pack()
worldshowup.pack()
purchasebtn.place(x=430,y=200)
loginbtn.place(x=430,y=330)
quitbtn.place(x=430,y=360)
c.pack()
dme.mainloop()
