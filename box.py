# 坐标数组
import pygame,sys
import os
from tkinter import *
import random
from tkinter.messagebox import *
current_theme=0
def box(current_theme,uid):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("sound/HAIKARA.mp3")

    pygame.mixer.music.play(loops=-1,start=0.0)
    host_lo = [0, 0]
    box_lo = [0, 0]
    ter_lo = [0, 0]
    x_obs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_obs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    score = [0, 0]
    #
    #TODO： 获取历史最高分

    # 障碍点个数
    w = [0]
    # initiallize difficulty
    current_mode = [""]
    x = Tk()
    x.title("player:"+uid+"  online")
    x.geometry("350x420")
    c = Canvas(x, width=350, height=350)
    c.pack()
    # 初始化标签内容
    label_1 = Label(x, text="current score:%d" % score[0], font="10", width=40, height=1, fg="black")
    label_1.pack()
    label_2 = Label(x, text="High score:%d" % score[1], font="10", width=40, height=1, fg="black")
    label_2.pack()
    # 贴图
    if current_theme == 0:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/free/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/free/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/free/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/free/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/free/brick.gif'))
    if current_theme == 1:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/conquest/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/conquest/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/conquest/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/conquest/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/conquest/brick.gif'))
    if current_theme == 2:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/european/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/european/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/european/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/european/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/european/brick.gif'))
    if current_theme == 3:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/future/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/future/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/future/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/future/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/future/brick.gif'))
    if current_theme == 4:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/midevil/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/midevil/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/midevil/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/midevil/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/midevil/brick.gif'))
    if current_theme == 5:
        box_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/woody/box.gif'))
        ter_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/woody/terminate.gif'))
        obs_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/woody/wall.gif'))
        host_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/woody/host.gif'))
        bg_img = PhotoImage(file=os.path.join(os.path.dirname(__file__) + '/textures/woody/brick.gif'))
    # 初始化背景
    for i in range(0, 11):
        for j in range(0, 11):
            t = c.create_image(32 * i + 16, 32 * j + 16, image=bg_img)
    # 外边界
    for i in range(0, 12):
        t = c.create_image(32 * i + 16, 16, image=obs_img)
    for i in range(0, 12):
        t = c.create_image(32 * i + 16, 336, image=obs_img)
    for i in range(1, 11):
        t = c.create_image(16, 32 * i + 16, image=obs_img)
    for i in range(1, 11):
        t = c.create_image(336, 32 * i + 16, image=obs_img)


    # 五个基本函数
    def scores():
        label_1.config(text="現在得点:%d" % score[0])
        label_2.config(text="最高得点:%d" % score[1])


    def erased(i, j):
        t = c.create_image(32 * i + 16, 32 * j + 16, image=bg_img)


    def host(i, j):
        t = c.create_image(32 * i + 16, 32 * j + 16, image=host_img)


    def box(i, j):
        t = c.create_image(32 * i + 16, 32 * j + 16, image=box_img)


    def terminate(i, j):
        t = c.create_image(32 * i + 16, 32 * j + 16, image=ter_img)


    def fill_black(i, j):
        t = c.create_image(32 * i + 16, 32 * j + 16, image=obs_img)


    # 清盘
    def clear_all():
        for i in range(1, 10):
            for j in range(1, 10):
                erased(i, j)


    # 随机生成五个障碍点
    def lay_obs():
        i = 0
        while i < w[0]:
            p = 0
            x_obstacle = random.randint(1, 9)
            y_obstacle = random.randint(1, 9)
            for k in range(0, i):
                if x_obs[k] == x_obstacle and y_obs[k] == y_obstacle:
                    p = 1
                    break
            if p == 0:
                fill_black(x_obstacle, y_obstacle)
                x_obs[i] = x_obstacle
                y_obs[i] = y_obstacle
                i = i + 1
        # print("x_obs=",x_obs)
        # print("y_obs=",y_obs)


    # 随机生成目标点
    def lay_ter():
        while 1:
            p = 0
            tx = random.randint(3, 7)
            ty = random.randint(3, 7)
            for i in range(0, w[0]):
                if tx == x_obs[i] and ty == y_obs[i]:
                    p = 1
                    break
            if p == 0:
                terminate(tx, ty)
                ter_lo[0] = tx
                ter_lo[1] = ty
                break
        # print ("terminate=",ter_lo)


    # 随机生成箱子坐标
    def lay_box():
        while 1:
            p = 0
            bx = random.randint(3, 7)
            by = random.randint(3, 7)
            for i in range(0, w[0]):
                if bx == x_obs[i] and by == y_obs[i]:
                    p = 1
                    break
            if bx == ter_lo[0] and by == ter_lo[1]:
                p = 1
            if p == 0:
                box(bx, by)
                box_lo[0] = bx
                box_lo[1] = by
                break
        # print("box_start=",box_lo)


    # 随机生成起点坐标
    def lay_sta():
        while 1:
            p = 0
            hx = random.randint(1, 9)
            hy = random.randint(1, 9)
            for i in range(0, w[0]):
                if hx == x_obs[i] and hy == y_obs[i]:
                    p = 1
                    break
            if hx == ter_lo[0] and hy == ter_lo[1]:
                p = 1
            if hx == box_lo[0] and hy == box_lo[1]:
                p = 1
            if p == 0:
                host(hx, hy)
                host_lo[0] = hx
                host_lo[1] = hy
                break
        # print("host_start=",host_lo)


    # 安置各个色块
    def start_game():
        lay_obs()
        lay_ter()
        lay_box()
        lay_sta()


    # 终点相关的判定
    def judged():
        if box_lo[0] == ter_lo[0] and box_lo[1] == ter_lo[1]:
            showwarning(message="成功!")
            # x.destroy()
            if current_mode[0] == "2":
                score[0] = score[0] + 3
                compare_score()
                scores()
                w_high()
            if current_mode[0] == "1":
                score[0] = score[0] + 2
                compare_score()
                scores()
                w_medium()
            if current_mode[0] == "0":
                score[0] = score[0] + 1
                compare_score()
                scores()
                w_low()
            return
        if (host_lo[0] == ter_lo[0] and host_lo[1] == ter_lo[1]) \
                or (box_lo[0] == ter_lo[0] and box_lo[1] == ter_lo[1]):
            pass
        else:
            terminate(ter_lo[0], ter_lo[1])


    # 四个host移动函数
    def move_up():
        if host_lo[1] == 1:  # 防止上出界
            return
        erased(host_lo[0], host_lo[1])
        host(host_lo[0], host_lo[1] - 1)
        host_lo[1] = host_lo[1] - 1
        # print("host=",host_lo)


    def move_down():
        if host_lo[1] == 9:
            return
        erased(host_lo[0], host_lo[1])
        host(host_lo[0], host_lo[1] + 1)
        host_lo[1] = host_lo[1] + 1
        # print("host=",host_lo)


    def move_left():
        if host_lo[0] == 1:
            return
        erased(host_lo[0], host_lo[1])
        host(host_lo[0] - 1, host_lo[1])
        host_lo[0] = host_lo[0] - 1


    # print("host=",host_lo)
    def move_right():
        if host_lo[0] == 9:
            return
        erased(host_lo[0], host_lo[1])
        host(host_lo[0] + 1, host_lo[1])
        host_lo[0] = host_lo[0] + 1
        # print("host=",host_lo)


    # 四个box移动函数
    def box_up():
        if box_lo[1] == 1:
            return
        erased(box_lo[0], box_lo[1])
        box(box_lo[0], box_lo[1] - 1)
        box_lo[1] = box_lo[1] - 1


    # print("box=",box_lo)
    def box_down():
        if box_lo[1] == 9:
            return
        erased(box_lo[0], box_lo[1])
        box(box_lo[0], box_lo[1] + 1)
        box_lo[1] = box_lo[1] + 1
        # print("box=",box_lo)


    def box_left():
        if box_lo[0] == 1:
            return
        erased(box_lo[0], box_lo[1])
        box(box_lo[0] - 1, box_lo[1])
        box_lo[0] = box_lo[0] - 1


    # print("box=",box_lo)
    def box_right():
        if box_lo[0] == 9:
            return
        erased(box_lo[0], box_lo[1])
        box(box_lo[0] + 1, box_lo[1])
        box_lo[0] = box_lo[0] + 1


    #  print("box=",box_lo)
    # 四个推箱子函数
    def push_up():
        p = 0
        if host_lo[1] - 1 == box_lo[1] and host_lo[0] == box_lo[0]:  # 判定host与box是否在要推动的方向上紧邻
            if box_lo[1] == 1:
                pass
            else:
                for i in range(0, w[0]):
                    if y_obs[i] + 1 == box_lo[1] and x_obs[i] == box_lo[0]:
                        p = 1
                        break
                if p == 0:
                    box_up()
                    move_up()
        else:
            for i in range(0, w[0]):
                if y_obs[i] + 1 == host_lo[1] and x_obs[i] == host_lo[0]:
                    p = 1
                    break
            if p == 0:
                move_up()
        judged()


    def push_down():
        p = 0
        if host_lo[1] + 1 == box_lo[1] and host_lo[0] == box_lo[0]:
            if box_lo[1] == 9:
                pass
            else:
                for i in range(0, w[0]):
                    if y_obs[i] - 1 == box_lo[1] and x_obs[i] == box_lo[0]:
                        p = 1
                        break
                if p == 0:
                    box_down()
                    move_down()
        else:
            for i in range(0, w[0]):
                if y_obs[i] - 1 == host_lo[1] and x_obs[i] == host_lo[0]:
                    p = 1
                    break
            if p == 0:
                move_down()
        judged()


    def push_left():
        p = 0
        if host_lo[0] - 1 == box_lo[0] and host_lo[1] == box_lo[1]:
            if box_lo[0] == 1:
                pass
            else:
                for i in range(0, w[0]):
                    if x_obs[i] + 1 == box_lo[0] and y_obs[i] == box_lo[1]:
                        p = 1
                        break
                if p == 0:
                    box_left()
                    move_left()
        else:
            for i in range(0, w[0]):
                if x_obs[i] + 1 == host_lo[0] and y_obs[i] == host_lo[1]:
                    p = 1
                    break
            if p == 0:
                move_left()
        judged()


    def push_right():
        p = 0
        if host_lo[0] + 1 == box_lo[0] and host_lo[1] == box_lo[1]:
            if box_lo[0] == 9:
                pass
            else:
                for i in range(0, w[0]):
                    if x_obs[i] - 1 == box_lo[0] and y_obs[i] == box_lo[1]:
                        p = 1
                        break
                if p == 0:
                    box_right()
                    move_right()
        else:
            for i in range(0, w[0]):
                if x_obs[i] - 1 == host_lo[0] and y_obs[i] == host_lo[1]:
                    p = 1
                    break
            if p == 0:
                move_right()
        judged()


    # 关联键盘
    def key_detect(event):
        if event.keysym == "Up" or event.keysym == "w" or event.keysym == "W":
            push_up()
        elif event.keysym == "Down" or event.keysym == "s" or event.keysym == "S":
            push_down()
        elif event.keysym == "Left" or event.keysym == "a" or event.keysym == "A":
            push_left()
        elif event.keysym == "Right" or event.keysym == "d" or event.keysym == "D":
            push_right()
        else:
            pass


    kd = Button(x)
    kd.bind_all("<KeyPress>", key_detect)


    # 难度设置
    def w_low():
        w[0] = 5
        clear_all()
        start_game()
        current_mode[0] = "0"


    def w_medium():
        w[0] = 8
        clear_all()
        start_game()
        current_mode[0] = "1"


    def w_high():
        w[0] = 10
        clear_all()
        start_game()
        current_mode[0] = '2'


    # 说明
    def explain():
        showinfo(title="ゲームの説明", message="キーボードのWASDキーを使って、子供を操作して、箱を終点まで押してください")


    # 重开
    def re():
        if current_mode[0] == "2":
            w_high()
        if current_mode[0] == "1":
            w_medium()
        if current_mode[0] == "0":
            w_low()


    # 清除分数
    def unregister():
        handle = open(os.path.join(os.path.dirname(__file__) + '/saves/highscore.txt'), 'w+')
        handle.write("0")
        handle.close()
        score[0] = 0
        label_2.config(text="high score:0")
        label_1.config(text="current score:0")


    # 注册最高分
    def regist():
        pass
        #TODO：上传数据库


    # 比较分数
    def compare_score():
        if score[0] <= score[1]:
            pass
        else:
            score[1] = score[0]
            regist()


    # 菜单栏
    Menubar = Menu(x)
    diffculty = Menu(Menubar, tearoff=0)
    Menubar.add_cascade(label="難易度選択", menu=diffculty)
    diffculty.add_command(label="低い", command=w_low)
    diffculty.add_command(label="中くらい", command=w_medium)
    diffculty.add_command(label="高い", command=w_high)
    restart = Menu(Menubar, tearoff=0)
    Menubar.add_command(label="リスタート", command=re)
    Menubar.add_command(label="ゲームの説明", command=explain)
    Menubar.add_command(label="ゲーム終了", command=quit)
    Menubar.add_command(label="レコードを削除します", command=unregister)
    x.config(menu=Menubar)
    x.mainloop()
