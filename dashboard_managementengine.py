from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
def dme():
    dict ={'uid':"",'where':"",'content':"",'changecontent':"",'method':-1}
    def accountdelete(dict):
        method = 0
        dict['method']=method
        return dict


    def accountban(dict):
        method = 1
        dict['method']=method
        return dict

    def deleteselection(dict):
        method = 2
        dict['method']=method
        return dict

    def changevalue(dict):
        method = 3
        dict['method']=method
        return dict

    def changeuseropt(dict):
        method = 4
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
        method = dict['method']
        where = dict['where']
        uid = dict['uid']
        content = dict['content']
        changecontent = dict['changecontent']
        if tm.askyesno("warning","操作提交之后更改不可恢复，是否确定？") ==1:
            if method == -1:
                tm.showwarning("警告","请选择操作！")
            if method == 0:
                pass
            if method == 1:
                pass
            if method == 2:
                pass
            if method == 3:
                pass
            if method == 4:
                pass

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
    dbshowup = Listbox(frame1,height=72,width=70)
    optbox = Combobox(dme, values=['删除账号', '封禁帐号', '清除选择的记录', '改变值', '禁用用户选项'])
    optbox.bind('<<ComboboxSelected>>', accountopt)
    viewbox = Combobox(dme, values=['查看用户', '查看用户分数', '查看最高分数', '查看购买内容'])
    viewbox.bind('<<ComboboxSelected>>', viewopt)
    refreshbtn = Button(dme, text="刷新", command=refreshticket)
    clearbtn = Button(dme, text="清除", command=clearticket)
    confirmbtn = Button(dme, text="确定", command=confirmticket(dict))
    cancelbtn = Button(dme, text="取消", command=cancelticket)
    optbox.pack()
    viewbox.pack()
    refreshbtn.pack()
    clearbtn.pack()
    dbshowup.pack()
    confirmbtn.pack()
    cancelbtn.pack()
    c.pack()
    dme.mainloop()
