from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *


dict ={'uid':"",'where':"",'content':"",'changecontent':"",'method':-1}
def checkexistence(mystring,content):
    if mystring.find(content) != -1:
        return 0
    else:
        return 1
def accountdelete(dict):
    method = 0
    temp = dbshowup.curselection()
    uid = temp#############################################################################################################
    dict['uid'] = uid
    dict['method']=method
    return dict


def accountban(dict):
    method = 1
    temp = dbshowup.curselection()
    uid = temp#############################################################################################################
    dict['uid'] = uid
    dict['method']=method
    return dict

def deleteselection(dict):
    method = 2
    temp = dbshowup.curselection()
    uid = temp#############################################################################################################
    dict['uid'] = uid
    dict['method']=method
    return dict

def changevalue(dict):
    method = 3
    temp = dbshowup.curselection()
    uid = temp#############################################################################################################
    dict['uid'] = uid
    dict['method']=method
    return dict

def changeuseropt(dict):
    method = 4
    temp = dbshowup.curselection()
    uid = temp#############################################################################################################
    dict['uid'] = uid
    dict['method']=method
    return dict



def viewaccount():
    pass


def viewscore():
    pass


def viewhighscore():
    pass


def viewdlcpurchase():
    pass



def refreshticket():
    pass


def clearticket():
    dbshowup.delete(0,END)


def confirmticket(dict):
    content_flag=0
    changecontent_flag=0
    content_error_check=1
    method = dict['method']
    where = dict['where']
    uid = dict['uid']
    content = originalcontentbox.get()
    changecontent = contentbox.get()
    content_error_check=checkexistence(dbshowup.curselection(), content)
    if content  != "" and content_error_check==0:
        content_flag=1
    if changecontent!="":
        changecontent_flag =1
    if tm.askyesno("warning","操作提交之后更改不可恢复，是否确定？") ==1:
        if method == -1:
            tm.showwarning("警告","请选择操作！")
        if method == 0:
            pass
        if method == 1:
            pass
        if method == 2:
            if content_flag ==1:
                pass
            else:
                tm.showerror("error","请输入正确键值")
        if method == 3:
            if content_flag ==1 and changecontent_flag ==1:
                pass
            else:
                tm.showerror("error","请键入正确键值")
        if method == 4:
            if content_flag == 1 and changecontent_flag == 1:
                pass
            else:
                tm.showerror("error", "请键入正确键值")

        refreshticket()
        dict['method'] = -1
        dict['content'] = ""
        dict['originalcontent'] = ""
        dict['uid'] = ""
        dict['where'] = ""
        return dict

    else:
        pass
def cancelticket(dict):
    if tm.askyesno("warning","没有提交的数据会永久丢失！真的很久！！") ==1:
        refreshticket()
        dict['method'] = -1
        dict['content'] = ""
        dict['originalcontent'] = ""
        dict['uid'] = ""
        dict['where'] = ""
        return dict
    else:
        pass

def viewopt(event):
    dic = {0: viewaccount(), 1: viewscore(), 2: viewhighscore(), 3: viewdlcpurchase()}
    c = dic[optbox.current()]


def accountopt(event):
    dic = {0: accountdelete(), 1: accountban(), 2: deleteselection(), 3: changevalue(), 4: changeuseropt()}
    c = dic[viewbox.current()]


# def management_engine():
dme = Toplevel()
dme.title("dme_svc")
dme.geometry("1280x720")
c = Canvas(dme, width=1280, height=720)
frame1 = Frame(dme,relief = RAISED,width=720,height=700)
frame1.place(relx=0.0)
dbshowup = Text(frame1,height=72,width=70)
optbox = Combobox(dme, values=['删除账号', '封禁帐号', '清除选择的记录', '改变值', '禁用用户选项'])
optbox.bind('<<ComboboxSelected>>', accountopt)
viewbox = Combobox(dme, values=['查看用户', '查看用户分数', '查看最高分数', '查看购买内容'])
viewbox.bind('<<ComboboxSelected>>', viewopt)
originalcontentbox = Entry(dme)
contentbox = Entry(dme)
refreshbtn = Button(dme, text="刷新", command=refreshticket)
clearbtn = Button(dme, text="清除", command=clearticket)
confirmbtn = Button(dme, text="确定", command=confirmticket(dict))
cancelbtn = Button(dme, text="取消", command=cancelticket)
originallabel = Label(dme,text="查找：")
contentlabel = Label(dme,text="替换为：")
optbox.pack()
viewbox.pack()
refreshbtn.pack()
clearbtn.pack()
dbshowup.pack()
confirmbtn.pack()
cancelbtn.pack()
originallabel.pack()
originalcontentbox.pack()
contentlabel.pack()
contentbox.pack()
c.pack()
dme.mainloop()
