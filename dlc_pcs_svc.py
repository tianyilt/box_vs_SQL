# coding=utf-8
# dlc_pcs_svc copyright 2019 by syuizen
from tkinter import *
import tkinter.messagebox as tm
from tkinter.ttk import *


def dlc(uid):
    def confirmpurchase():
        contentchange = contentshowup.curselection()  # tuple,tuple[0]is dlc code
        if contentchange != ():
            dlc_dic = {0: 'free', 1: 'conquest', 2: 'european', 3: 'future', 4: 'midevil', 5: 'woody'}  # 提醒自己还没做
            if tm.askyesno("ご確認ください", dlc_dic[contentchange[0]] + "の購入を確認しますか？") == 1:
                tm.showinfo("メッセージ", dlc_dic[contentchange[0]] + "購入成功！")

                ########################contentchange写入数据库
                # 购买后,相关记录变更

                import pymysql
                import datetime
                dt = datetime.datetime.now()  # get current time
                dt_now = dt.strftime('%Y-%m-%d %H:%M:%S')

                db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
                cursor = db.cursor()
                sql1 = """select UID from login where UserName ='%s' """ % (uid)

                try:
                    cursor.execute(sql1)  # 执行sql语句
                    result = cursor.fetchall()
                    if result:
                        sql2 = """INSERT INTO dlc(Dtype, UID, \
                              money, date) \
                              VALUES ('%s', '%s',%d , '%s')""" % \
                               (contentchange[0], result[0][0], 6, dt_now)
                        cursor.execute(sql2)
                        db.commit()

                except Exception as e:
                    db.rollback()

                finally:
                    db.close()


            else:
                pass

    def refreshticket():
        """
        产生dlc购买视图，查询数据库查询购买状态，并能够选择相关dlc进行购买
        :return:
        """
        contentshowup.delete(0, END)
        # ['free', 'conquest', 'european', 'future', 'midevil', 'woody']是主题
        dlc_purchase_state = {0: '未购买', 1: '已拥有'}
        dlc_purchase_flag_list = [1, 0, 0, 0, 0, 0]  # 第i个元素表示第i个dlc购买状态，0没买1买了
        #################################拉取数据库视图
        import pymysql
        db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
        cursor = db.cursor()

        # sql = """SELECT dlc.Dtype FROM login CROSS JOIN dlc WHERE (login.uid = dlc.UID) AND (login.username = '%s')""" % (uid)
        sql = """SELECT Dtype FROM dlcbuy WHERE username = '%s')""" % (uid)

        try:
            cursor.execute(sql)  # 执行sql语句
            results = cursor.fetchall()  # 获取查询的所有记录
            # 返回值是一个元组的形式
            if results:
                for dlc_flag in results:
                    dlc_purchase_flag_list[dlc_flag[0]] = 1
        except Exception as e:
            db.rollback()

        finally:
            db.close()

        # dlc视图

        contentshowup.insert(END, "free\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[0]]))
        contentshowup.insert(END, "conquest\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[1]]))
        contentshowup.insert(END, "european\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[2]]))
        contentshowup.insert(END, "future\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[3]]))
        contentshowup.insert(END, "midevil\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[4]]))
        contentshowup.insert(END, "woody\t %s" % (dlc_purchase_state[dlc_purchase_flag_list[5]]))

    def dlcquit():
        dlc.destroy()

    # def management_engine():
    dlc = Toplevel()
    dlc.title("コンテンツ買う")
    dlc.geometry("390x190")
    c = Canvas(dlc, width=1280, height=720)
    frame1 = Frame(dlc, relief=RAISED, width=30, height=10)
    frame1.place(relx=0.0)
    contentshowup = Listbox(frame1, width=30, height=10)
    refreshbtn = Button(dlc, text="更新", width=18, command=refreshticket)
    purchasebtn = Button(dlc, text="買う", width=18, command=confirmpurchase)
    quitbtn = Button(dlc, text="取り消し", width=18, command=dlcquit)
    refreshbtn.place(x=230, y=20)
    contentshowup.pack()
    purchasebtn.place(x=230, y=50)
    quitbtn.place(x=230, y=140)
    c.pack()
    dlc.mainloop()
