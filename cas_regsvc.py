from tkinter import *
import tkinter.messagebox as tm
def cas_regsvc():
    def regsvcquit():
        regsvc.destroy()

    def regsvcconfirm():
        if nickname_repeat_flag == 1:
            tm.showwarning("warning", "昵称已经存在，请再选一个")
        else:
            tm.showinfo("info", "注册成功！")
            regsvcquit()
    regsvc = Tk()
    regsvc.title("register")
    regsvc.geometry("350x350")
    c = Canvas(regsvc, width=350, height=350)
    usrname_lb = Label(regsvc, text="username:", font='6', width=10, height=1, fg='black')
    passwd_lb = Label(regsvc, text="password:", font='6', width=10, height=1, fg='black')
    nkname_lb = Label(regsvc, text="nickname:", font='6', width=10, height=1, fg='black')
    confirm_btn = Button(regsvc, text="confirm", font='4', width=15, height=1, fg="black", command=regsvcconfirm)
    cancel_btn = Button(regsvc, text="cancel", font='4', width=15, height=1, fg="black", command=regsvcquit)
    usrname_inputbox = Entry(regsvc, textvariable="john", font=6, width=21, bd=5)
    nkname_inputbox = Entry(regsvc, textvariable="john", font=6, width=21, bd=5)
    passwd_inputbox = Entry(regsvc, textvariable="password", font=6, width=21, bd=5, show="*")
    usrname_lb.place(x=18, y=15)
    usrname_inputbox.place(x=120, y=15)
    passwd_lb.place(x=18, y=50)
    passwd_inputbox.place(x=120, y=50)
    nkname_lb.place(x=18, y=85)
    nkname_inputbox.place(x=120, y=85)
    confirm_btn.place(x=18, y=133)
    cancel_btn.place(x=178, y=133)
    c.pack()
    regsvc.mainloop()
