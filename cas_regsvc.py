from tkinter import *
import tkinter.messagebox as tm
def cas_regsvc():
    def regsvcquit():
        regsvc.destroy()

    def regsvcconfirm():
        inputusrname=usrname_inputbox.get()
        inputpasswd=passwd_inputbox.get()
        inputnkname=nkname_inputbox.get()

        if inputusrname and inputpasswd and inputnkname:
            import pymysql
            # 此行添加数据库连接
            db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
            cursor = db.cursor()
            sql = """select NickName from login where UserName ='%s' """ % (inputusrname)
            try:
                cursor.execute(sql)  # 执行sql语句
                results = cursor.fetchall()  # 获取查询的所有记录
                # 返回值是一个元组的形式
                if results:
                    # 表示有重复的username
                    nickname_repeat_flag = 1
                else:
                    # 表示没有重复的username，开始把账户信息写入login
                    nickname_repeat_flag = 0
                    sql = """INSERT INTO login(UserName, \
                           PassWord, NickName) \
                           VALUES ('%s', '%s', '%s')""" % \
                          (inputusrname, inputpasswd, inputnkname)
                    # 执行sql语句
                    cursor.execute(sql)
                    # 提交到数据库执行
                    db.commit()

            except Exception as e:
                db.rollback()
            finally:
                db.close()


        else:
            nickname_repeat_flag = 0




        #nickname_repeat_flag ==1说明参考数据库昵称定义重复\
        #nickname_repeat_flag = 1

        if nickname_repeat_flag == 1:
            tm.showwarning("ご注意ください", "ニックネーム既に存在しました、もう一度付けてください")
        else:
            tm.showinfo("情報", "登録成功！")
            regsvcquit()
#CASregsvc main framework
    regsvc = Tk()
    regsvc.title("レジスト")
    regsvc.geometry("400x200")
    c = Canvas(regsvc, width=350, height=350)
    usrname_lb = Label(regsvc, text="お名前:", font='6', width=12, height=1, fg='black')
    passwd_lb = Label(regsvc, text="パスワード:", font='6', width=12, height=1, fg='black')
    nkname_lb = Label(regsvc, text="ニックネーム:", font='6', width=12, height=1, fg='black')
    confirm_btn = Button(regsvc, text="確認", font='4', width=17, height=1, fg="black", command=regsvcconfirm)
    cancel_btn = Button(regsvc, text="取り消し", font='4', width=17, height=1, fg="black", command=regsvcquit)
    usrname_inputbox = Entry(regsvc, textvariable="john", font=6, width=21, bd=5)
    nkname_inputbox = Entry(regsvc, textvariable="johnny", font=6, width=21, bd=5)
    passwd_inputbox = Entry(regsvc, textvariable="password", font=6, width=21, bd=5, show="*")
    usrname_lb.place(x=18, y=15)
    usrname_inputbox.place(x=165, y=15)
    passwd_lb.place(x=18, y=50)
    passwd_inputbox.place(x=165, y=50)
    nkname_lb.place(x=18, y=85)
    nkname_inputbox.place(x=165, y=85)
    confirm_btn.place(x=18, y=133)
    cancel_btn.place(x=200, y=133)
    c.pack()
    regsvc.mainloop()

