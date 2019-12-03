from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *


def accountdelete():
    pass


def accountban():
    pass


def deleteselection():
    pass


def changevalue():
    pass


def changeuseropt():
    pass


def undefinedfunction():
    pass


def refresh():
    pass


def viewaccount():
    pass


def viewscore():
    pass


def viewhighscore():
    pass


def viewdlcpurchase():
    pass


def viewundefinedfunction():
    pass


def refreshticket():
    pass


def viewopt(event):
    dic = {0: viewaccount(), 1: viewscore(), 2: viewhighscore(), 3: viewdlcpurchase(), 5: viewundefinedfunction()}
    c = dic[optbox.current()]


def accountopt(event):
    dic = {0: accountdelete(), 1: accountban(), 2: deleteselection(), 3: changevalue(), 4: changeuseropt(),
           5: undefinedfunction()}
    c = dic[viewbox.current()]


# def management_engine():
dme = Tk()
dme.title("dme_svc")
dme.geometry("1280x720")
c = Canvas(dme, width=1280, height=720)
dbshowup = Text(dme, bd=5)
optbox = Combobox(dme, values=['删除账号', '封禁帐号', '清除选择的记录', '改变值', '禁用用户选项', 'undefinedfunction'])
optbox.bind('<<ComboboxSelected>>', accountopt)
viewbox = Combobox(dme, values=['查看用户', '查看用户分数', '查看最高分数', '查看购买内容', 'undefinedfunction'])
viewbox.bind('<<ComboboxSelected>>', viewopt)
refreshbtn = Button(dme, text="刷新", command=refreshticket)
c.pack()
dme.mainloop()
