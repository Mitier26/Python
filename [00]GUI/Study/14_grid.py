from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# btn1 = Button(root, text="버튼1")
# btn2 = Button(root, text="버튼2")

# btn1.pack()
# btn2.pack()

# btn1.pack(side="left")
# btn2.pack(side="right")

# 팩과 그리드의 차이에 주목하자
# 팩은 쌓는 느낌, 추가
# 그리드는 좌표에 지정

# btn1.grid(row=0, column=0)
# btn2.grid(row=1, column=1)

# 키패드 만들어 보기

# 맨 윗줄
# padx, pady : 가운데있는 그림이나 글자를 기준으로 늘린다.
# 단, 그리드에 있는 다른요소의 크기가 클 경우 큰것을 기준으로 하기때문에 작은 것의 그리드가 이상해진다.
# 이럴 경우 padx, pady를 사용하지 않고 width, height 를 사용한다. 
# btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f16 = Button(root, text="F16", width=5, height=2)
btn_f17 = Button(root, text="F17", width=5, height=2)
btn_f18 = Button(root, text="F18", width=5, height=2)
btn_f19 = Button(root, text="F19", width=5, height=2)

# sticky : 동서남북 방향으로 늘린다.
btn_f16.grid(row=0, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_f17.grid(row=0, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_f18.grid(row=0, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_f19.grid(row=0, column=3, sticky = N+E+W+S, padx=3, pady=3)

# 2번째 줄
btn_clear = Button(root, text="clear", width=5, height=2)
btn_equal = Button(root, text="=", width=5, height=2)
btn_div = Button(root, text="/", width=5, height=2)
btn_mul = Button(root, text="*", width=5, height=2)

btn_clear.grid(row=1, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_equal.grid(row=1, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_div.grid(row=1, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_mul.grid(row=1, column=3, sticky = N+E+W+S, padx=3, pady=3)

# 3번째 줄
btn_7 = Button(root, text="7", width=5, height=2)
btn_8 = Button(root, text="8", width=5, height=2)
btn_9 = Button(root, text="9", width=5, height=2)
btn_sub = Button(root, text="-", width=5, height=2)

btn_7.grid(row=2, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_8.grid(row=2, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_9.grid(row=2, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_sub.grid(row=2, column=3, sticky = N+E+W+S, padx=3, pady=3)

# 4번째 줄
btn_4 = Button(root, text="4", width=5, height=2)
btn_5 = Button(root, text="5", width=5, height=2)
btn_6 = Button(root, text="6", width=5, height=2)
btn_add = Button(root, text="+", width=5, height=2)

btn_4.grid(row=3, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_5.grid(row=3, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_6.grid(row=3, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_add.grid(row=3, column=3, sticky = N+E+W+S, padx=3, pady=3)

# 5번째 줄

btn_1 = Button(root, text="1", width=5, height=2)
btn_2 = Button(root, text="2", width=5, height=2)
btn_3 = Button(root, text="3", width=5, height=2)
btn_enter = Button(root, text="enter", width=5, height=2)

btn_1.grid(row=4, column=0, sticky = N+E+W+S, padx=3, pady=3)
btn_2.grid(row=4, column=1, sticky = N+E+W+S, padx=3, pady=3)
btn_3.grid(row=4, column=2, sticky = N+E+W+S, padx=3, pady=3)
btn_enter.grid(row=4, column=3, rowspan=2, sticky = N+E+W+S, padx=3, pady=3)  # rowspan : row 2개를 합친다

# 6번째 줄
btn_0 = Button(root, text="0", width=5, height=2)
btn_point = Button(root, text=".", width=5, height=2)

btn_0.grid(row=5, column=0, columnspan=2, sticky = N+E+W+S, padx=3, pady=3)
btn_point.grid(row=5, column=2, sticky = N+E+W+S, padx=3, pady=3)

root.mainloop() # 반복을 하겠다
