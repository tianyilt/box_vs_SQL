# coding=utf-8
# dashboardclient copyright 2019 by syuizen
from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *
import CASClient
import themeselecter
import dlc_pcs_svc


def dbc(uid):
    def purchase():
        dlc_pcs_svc.dlc(uid)

    def refreshticket():
        worldshowup.delete(0, END)
        myshowup.delete(0, END)

        # worldshowup.insert(END,"Athrun_Zala 10086")
        # myshowup.insert(END,"Athrun_Zala 2019-01-20 10086")
        #########################################拉取数据库视图
        """
        前提:有个视图
        UID高分视图
        全局高分视图
        
        """

        import pymysql
        db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
        cursor = db.cursor()

        sql_world = """select * from dashboard limit 10;"""
        sql_my = """select * from dashboard where username = '%s' limit 10 """ % (uid)
        try:
            cursor.execute(sql_world)  # 执行sql语句
            result = cursor.fetchall()  # 二维tuple，username:string score:int endtime:datetime.datetime(2019, 12, 5, 18, 0, 1).strftime('%Y-%m-%d %H:%M:%S')
            for record in result:
                insert_record = "%s %d %s" % (record[0], record[1], record[2].strftime('%Y-%m-%d %H:%M:%S'))
                worldshowup.insert(END, insert_record)

            cursor.execute(sql_my)  # 执行sql语句
            result = cursor.fetchall()  # 二维tuple，username:string score:int endtime:datetime.datetime(2019, 12, 5, 18, 0, 1).strftime('%Y-%m-%d %H:%M:%S')
            for record in result:
                insert_record = "%s %d %s" % (record[0], record[1], record[2].strftime('%Y-%m-%d %H:%M:%S'))
                myshowup.insert(END, insert_record)
        except Exception as e:
            db.rollback()

        finally:
            db.close()

    def deletecurrent():
        if tm.askokcancel("ご注意", "ご注意ください：ご記録は完全に削除されます、本当に長いです"):
            if myshowup.curselection() != ():  # TODO:if uid=uid,ok
                datachange = myshowup.curselection()
                myshowup.delete(myshowup.curselection())
                #######################################################################################从数据库删除datachange
                # 数据库中也删除dashboard记录

                import pymysql
                db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
                cursor = db.cursor()

                sql_my = """select * from dashboard where username = '%s' limit 10 """ % (uid)
                try:
                    cursor.execute(sql_my)  # 执行sql语句
                    result = cursor.fetchall()  # 二维tuple，username:string score:int endtime:datetime.datetime(2019, 12, 5, 18, 0, 1).strftime('%Y-%m-%d %H:%M:%S')
                    record=result[datachange[0]]
                    #再查询一次，选择与datachange位置一样的记录，然后根据score与endtime来删除gamerecord中记录
                    sql="""DELETE from gamerecord where Score ='%s' AND endtime ='%s' """ %(record[1], record[2].strftime('%Y-%m-%d %H:%M:%S'))
                    cursor.execute(sql)
                    db.commit()
                except Exception as e:
                    db.rollback()

                finally:
                    db.close()







            else:
                tm.showerror("エラー", "何も選択しない！")
        else:
            pass

    def login():
        dme.destroy()
        themeselecter.ts(uid)

    # def management_engine():
    dme = Tk()
    dme.title("ハイスコア" + uid)
    dme.geometry("600x400")
    c = Canvas(dme, width=1280, height=720)
    frame1 = Frame(dme, relief=RAISED, width=30, height=60)
    frame1.place(relx=0.0)
    myshowup = Listbox(frame1, width=30, height=60)
    frame2 = Frame(dme, relief=RAISED, width=30, height=60)
    frame2.place(relx=0.3)
    worldshowup = Listbox(frame2, width=30, height=60)
    refreshbtn = Button(dme, text="更新", width=18, command=refreshticket)
    clearbtn = Button(dme, text="レコードを削除します", width=18, command=deletecurrent)
    loginbtn = Button(dme, text="遊び", width=18, command=login)
    purchasebtn = Button(dme, text="コンテンツを買います", width=18, command=purchase)
    quitbtn = Button(dme, text="ゲーム終了", width=18, command=quit)
    refreshbtn.place(x=430, y=40)
    clearbtn.place(x=430, y=70)
    myshowup.pack()
    worldshowup.pack()
    purchasebtn.place(x=430, y=200)
    loginbtn.place(x=430, y=330)
    quitbtn.place(x=430, y=360)
    c.pack()
    dme.mainloop()
