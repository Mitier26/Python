from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# Text : 여러줄을 입력할 수 있다.
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요")

# 엔트리는 1 줄 만 입력 받을 수 있다.
e = Entry(root, width = 30)
e.pack()
e.insert(0, "한 줄만 입력 가능")

def btncmd():
    print(txt.get("1.0", END))
    # Text에 입력한 것을 가지고 온다.
    # () < 내용은 처음 부터 끝까지 가지고 오라는 뜻
    # 1.0 : 1 = 1번 라인, 0 = 0번 colum 위치
    print(e.get())

    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 반복을 하겠다
