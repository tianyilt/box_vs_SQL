# coding=utf-8
from tkinter import *
import tkinter.messagebox as tm
import box
import tkinter.ttk as wtk
import dlc_pcs_svc
def ts(uid):
    cd = 0
    global purchase_flag
    purchase_flag = 0

    def themesvcconfirm():
        ######################
        cd = accountopt()
        #purchase_flag ==1 则dlc已经购买
        purchase_flag=0
        import pymysql
        db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
        cursor = db.cursor()

        sql = """SELECT Dtype FROM dlcbuy WHERE username = '%s'""" % (uid)
        try:
            cursor.execute(sql)  # 执行sql语句
            results = cursor.fetchall()  # 获取查询的所有记录
            # 返回值是一个元组的形式
            if results:
                for dlc_flag in results:
                    if dlc_flag[0] == cd:#因为是元组，所以如果有一个购买记录的dtype和cd一样就ok
                        purchase_flag = 1

        except Exception as e:
            db.rollback()

        finally:
            db.close()







        #purchase_flag = 1#测试金手指
        if purchase_flag ==1:
            themesvc.destroy()
            box.box(cd,uid)
        else:
            tm.showerror("エラー","テーマは買いません")
            if tm.askyesno("メッセージ","テーマは買いますか？"):
                dlc_pcs_svc.dlc(uid)
            else:
                pass
    def accountopt():
        dic = {0:0, 1: 1, 2:2, 3: 3, 4:4,5:5}
        cd=dic[optbox.current()]
        return cd
    themesvc = Tk()
    themesvc.title("テーマ選択")
    themesvc.geometry("240x110")
    c = Canvas(themesvc, width=240, height=110)
    theme_lb = Label(themesvc,text="テーマ選択",font="10",fg="black")
    optbox = wtk.Combobox(themesvc, values=['free', 'conquest', 'european', 'future', 'midevil', 'woody'])
    optbox.bind('<<ComboboxSelected>>', accountopt)
    confirm_btn = Button(themesvc, text="確認", font=4, width=10, height=1, fg="black", command=themesvcconfirm)
    theme_lb.pack()
    optbox.pack()
    confirm_btn.place(x=60,y=60 )
    c.pack()
    themesvc.mainloop()