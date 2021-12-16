from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# 체크 했다 안했다를 판정할 수 있는 변수
chkvar = IntVar()   # chkvar 에 int 형으로 값을 저장한다.
chkbox = Checkbutton(root, text="매일 공부 하기", variable=chkvar)
chkbox.select()
chkbox.deselect()
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일 동안 공부하기", variable=chkvar2)
chkbox2.pack()

def btncmd():
    print(chkvar.get()) # 0 : 체크 해제, 1 : 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 반복을 하겠다
