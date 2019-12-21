from tkinter import *
import tkinter.messagebox as tm
import cas_regsvc
import dashboard_client
import themeselecter
def CASClient():
    def casquit():
        cas.destroy()
    # 验证输入账户和CAS数据库是否匹配




    def casconfirm():
        inputusrname = usrname_inputbox.get()
        inputpasswd = passwd_inputbox.get()
        if inputusrname and inputpasswd:
        #此行连接数据
            import pymysql
            db = pymysql.connect('182.254.217.138', 'ZNDY', 'ZNDY@ecust123', 'box_vs_sql', charset="utf8")
            cursor = db.cursor()

            sql = """select PassWord from login where UserName ='%s' """ % (inputusrname)
            # 判断，查看用户名和密码名是否为空
            # 不为空之后在进行查询和判断
            # 不然当密码或用户名为空时会出现会导致出错
            try:
                cursor.execute(sql)  # 执行sql语句
                results = cursor.fetchall()  # 获取查询的所有记录
                # 返回值是一个元组的形式
                # print(type(results))
                if results:
                    if results[0][0] == inputpasswd:
                        # 表示登陆成功
                        verify_return_flag = 1
                        # print("sucessful")

                    else:
                        verify_return_flag = 0


                else:
                    verify_return_flag = 0
            except Exception as e:
                db.rollback()
        #verify_return_flag ==1则参考数据库验证通过,先看username有没有,没有返回0,有的话,看password是否符合
        else:
            verify_return_flag = 0


        #verify_return_flag = 1
        if verify_return_flag == 1:
            tm.showinfo("歓迎", "お帰りなさい，" + inputusrname)
            cas.destroy()
            dashboard_client.dbc(inputusrname)#####################################################################################################################################################
        else:
            tm.showerror("エラー", "ユーザー未登録又はパスワードエラー")
            registeryesno = tm.askyesno('レジスト', 'アカウントを登録しますか？')
            if registeryesno == 1:
                cas_regsvc.cas_regsvc()
            else:
                pass

    def casregister():
        cas_regsvc.cas_regsvc()

    # CASClient main framework
    cas = Tk()
    cas.title("CAS client")
    cas.geometry("360x200")
    c = Canvas(cas, width=350, height=180)
    usrname_lb = Label(cas, text="お名前:", font='6', width=10, height=1, fg='black')
    passwd_lb = Label(cas, text="パスワード:", font='6', width=10, height=1, fg='black')
    confirm_btn = Button(cas, text="確認", font='4', width=15, height=1, fg="black", command=casconfirm)
    cancel_btn = Button(cas, text="取り消し", font='4', width=15, height=1, fg="black", command=casquit)
    register_btn = Button(cas, text="don't have account?", font='2', width=31, height=1, fg="black",command=casregister)
    usrname_inputbox = Entry(cas, textvariable="john", font=6, width=21, bd=5)
    passwd_inputbox = Entry(cas, textvariable="password", font=6, width=21, bd=5, show="*")
    usrname_lb.place(x=18, y=15)
    usrname_inputbox.place(x=120, y=15)
    passwd_lb.place(x=18, y=50)
    passwd_inputbox.place(x=120, y=50)
    confirm_btn.place(x=18, y=98)
    cancel_btn.place(x=180, y=98)
    register_btn.place(x=18, y=140)
    c.pack()
    cas.mainloop()
