from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것
import tkinter.ttk as ttk

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

values = [str(i) + "일" for i in range(1, 32)]  # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("월급날")  # 최초 타이틀 표시

# state를 정하지 않으면 콤보박스 내에 글을 입력할 수 있게 된다.
# 글 입력을 막기 위해 readonly 를 해야 한다.
readonlycombobox = ttk.Combobox(root, height=5, values=values, state="readonly")
readonlycombobox.current(0) # 0번째 인덱스 값 선택
readonlycombobox.pack()


def btncmd():
    print(combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() # 반복을 하겠다
