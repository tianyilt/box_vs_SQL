from tkinter import *
import box
import tkinter.messagebox as tm
import cas_regsvc
import dashboard_managementengine

def CASClient():
    def casquit():
        cas.destroy()

    # 验证输入账户和CAS数据库是否匹配
    def casconfirm():
        inputusrname = usrname_inputbox.get()
        inputpasswd = passwd_inputbox.get()
        # 此行连接数据
        verify_return_flag = 1
        admin_flag = 0
        if verify_return_flag == 1:
            tm.showinfo("歓迎", "お帰りなさい，" + inputusrname)
            if admin_flag ==0:
                cas.destroy()
                box.box(2)#####################################################################################################################################################
            else:
                cas.destroy()
                dashboard_managementengine.dme()


        if verify_return_flag == 0:
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
    cas.geometry("350x180")
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
    cancel_btn.place(x=178, y=98)
    register_btn.place(x=18, y=135)
    c.pack()
    cas.mainloop()
