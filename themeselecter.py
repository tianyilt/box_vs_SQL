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
        purchase_flag = 1
        if purchase_flag ==1:
            themesvc.destroy()
            box.box(cd,uid)
        else:
            tm.showerror("エラー","テーマは買いません")
            if tm.askyesno("メッセージ","テーマは買いますか？"):
                dlc_pcs_svc.dlc()
            else:
                pass
    def accountopt():
        dic = {0:0, 1: 1, 2:2, 3: 3, 4:4,5:5}
        cd=dic[optbox.current()]
        return cd
    themesvc = Tk()
    themesvc.title("テーマ"+uid)
    themesvc.geometry("400x200")
    c = Canvas(themesvc, width=350, height=350)
    theme_lb = Label(themesvc,text="テーマ選択",font="10",fg="black")
    optbox = wtk.Combobox(themesvc, values=['free', 'conquest', 'european', 'future', 'midevil', 'woody'])
    optbox.bind('<<ComboboxSelected>>', accountopt)
    confirm_btn = Button(themesvc, text="確認", font=4, width=30, height=1, fg="black", command=themesvcconfirm)
    confirm_btn.place(x=18, y=133)
    theme_lb.pack()
    optbox.pack()
    c.pack()
    themesvc.mainloop()