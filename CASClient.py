from tkinter import *
import os
import tkinter.messagebox as tm
import cas_regsvc
def CASClient():
    def casquit():
        cas.destroy()
#验证输入账户和CAS数据库是否匹配
    def casconfirm():
        inputusrname= usrname_inputbox.get()
        inputpasswd=passwd_inputbox.get()
        #此行连接数据库
        if verify_return_flag ==1:
            tm.showinfo("welcome","欢迎回来，"+inputusrname)
        if verify_return_flag ==0:
            tm.showerror("invalid attempt","用户名不存在或者密码错误")
            registeryesno=tm.askyesno('注册', '是否要快速注册账号？')
            if  registeryesno== 1:
                cas_regsvc.cas_regsvc()
            else:
                pass
    def casregister():
        cas_regsvc.cas_regsvc()
#CASClient main framework
    cas=Tk()
    cas.title("CAS client")
    cas.geometry("350x180")
    c=Canvas(cas,width=350,height=180)
    usrname_lb=Label(cas,text="username:",font='6',width=10,height=1,fg='black')
    passwd_lb=Label(cas,text="password:",font='6',width=10,height=1,fg='black')
    confirm_btn=Button(cas,text="confirm",font = '4',width=15,height=1,fg="black",command=casconfirm)
    cancel_btn=Button(cas,text="cancel",font = '4',width=15,height=1,fg="black",command=casquit)
    register_btn=Button(cas,text="don't have account?",font = '2',width=31,height=1,fg="black",command=casregister)
    usrname_inputbox=Entry(cas,textvariable="john",font=6,width=21,bd=5)
    passwd_inputbox=Entry(cas,textvariable="password",font=6,width=21,bd=5,show="*")
    usrname_lb.place(x=18,y=15)
    usrname_inputbox.place(x=120,y=15)
    passwd_lb.place(x=18,y=50)
    passwd_inputbox.place(x=120,y=50)
    confirm_btn.place(x=18,y=98)
    cancel_btn.place(x=178,y=98)
    register_btn.place(x=18,y=135)
    c.pack()
    cas.mainloop()