from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것
import tkinter.ttk as ttk
import time

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# 좌우로 왔다갔다 하는것
progressbar1 = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar1.start(10)   # 10ms 마다 움직임, 이것은 바가 움직이는 속도
progressbar1.pack()

# 1 > 100 으로 차오르다.
progressbar2 = ttk.Progressbar(root, maximum=100, mode="determinate")
progressbar2.start(10)   # 10ms 마다 움직임, 이것은 바가 움직이는 속도
progressbar2.pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3)
progressbar3.pack()


def btncmd1():
    progressbar2.stop() # 작동 중지

btn1 = Button(root, text="중지", command=btncmd1)
btn1.pack()


def btncmd2():
    for i in range(1,101):
        time.sleep(0.01)    # 0.01초 대기

        p_var3.set(i)   # 프로그래스 바의 값을 설정
        progressbar3.update()   # UI 없데이트, 없으면 한번에 올라 간다.
        print(p_var3.get())


btn2 = Button(root, text="시작", command=btncmd2)
btn2.pack()

root.mainloop() # 반복을 하겠다
