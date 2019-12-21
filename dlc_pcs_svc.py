#dlc_pcs_svc copyright 2019 by syuizen
from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
def dlc():
    def confirmpurchase():
        contentchange=contentshowup.curselection()
        if contentchange != ():
            if tm.askyesno("ご確認ください",contentchange+"の購入を確認しますか？")==1:
               tm.showinfo("メッセージ",contentchange+"購入成功！")
               ########################contentchange写入数据库
                #购买后,相关记录变更

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


            else:
                pass
    def refreshticket():
        pass
    #################################拉取数据库视图



    #dlc视图

    def dlcquit():
        dlc.destroy()
    # def management_engine():
    dlc = Toplevel()
    dlc.title("コンテンツ買う")
    dlc.geometry("390x190")
    c = Canvas(dlc, width=1280, height=720)
    frame1 = Frame(dlc,relief = RAISED,width=30,height=10)
    frame1.place(relx=0.0)
    contentshowup = Listbox(frame1,width=30,height=10)
    refreshbtn = Button(dlc, text="更新", width= 18,command=refreshticket)
    purchasebtn = Button(dlc, text="買う",width= 18, command=confirmpurchase)
    quitbtn = Button(dlc, text="取り消し", width= 18,command=dlcquit)
    refreshbtn.place(x=230,y=20)
    contentshowup.pack()
    purchasebtn.place(x=230,y=50)
    quitbtn.place(x=230,y=140)
    c.pack()
    dlc.mainloop()
