#dashboardclient copyright 2019 by syuizen
from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
import CASClient
import themeselecter
import dlc_pcs_svc
def dbc(uid):
    def purchase():
        dlc_pcs_svc.dlc()
    def refreshticket():
        #########################################拉取数据库视图
        """
        前提:有个视图
        UID高分视图
        全局高分视图
        return 
        """
        # import pymysql
        # db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
        # cursor = db.cursor()
        #
        # sql = """select PassWord from login where UserName ='%s' """ % (inputusrname)
        #
        # try:
        #     cursor.execute(sql)  # 执行sql语句
        #
        # except Exception as e:
        #     db.rollback()
        #
        # finally:
        #     db.close()


    def deletecurrent():
        if tm.askokcancel("ご注意","ご注意ください：ご記録は完全に削除されます、本当に長いです"):
            if myshowup.curselection() !=  ():#TODO:if uid=uid,ok
                datachange=myshowup.curselection()
                myshowup.delete(myshowup.curselection())
                #######################################################################################从数据库删除datachange
                #数据库中也删除dashboard记录





            else:
                tm.showerror("エラー","何も選択しない！")
        else:
            pass
    def login():
        dme.destroy()
        themeselecter.ts(uid)
    # def management_engine():
    dme = Tk()
    dme.title("ハイスコア"+uid)
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
    loginbtn=Button(dme,text="遊び",width= 18,command=login)
    purchasebtn = Button(dme, text="コンテンツを買います",width= 18, command=purchase)
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
