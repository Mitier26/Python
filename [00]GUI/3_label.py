from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하니?")
label1.pack()

photo = PhotoImage(file="[00]GUI/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="클릭을 했구나") # 내용을 바꿀 경우 config 사용

    global photo2   # 전역 변수가 아닐 경우, 가비지 컬렉터가 그림을 삭제해 버린다.
    photo2 = PhotoImage(file="[00]GUI/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop() # 반복을 하겠다
