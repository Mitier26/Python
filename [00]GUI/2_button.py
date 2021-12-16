from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")

btn1 = Button(root, text="버튼1")
btn1.pack()

# 버튼의 크기를 조정
# pad : 크기가 고정이 되지 않는다. 내용의 크기에 따라 버튼의 크기도 달라진다.
btn2 = Button(root, padx = 5, pady=10, text="버튼2222222222222")
btn2.pack()

btn3 = Button(root, padx = 10, pady=5, text="버튼3")
btn3.pack()

# 크기값을 고정한다.
btn4 = Button(root, width=10, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5")
btn5.pack()

photo = PhotoImage(file="[00]GUI/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었다")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()

root.mainloop() # 반복을 하겠다
