from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

label1 = Label(root, text="메뉴를 선택하세요").pack()

burger_var = IntVar()
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈햄버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="감자햄버거", value=3, variable=burger_var)



label2 = Label(root, text="음료를 선택하세요").pack()
drink_var = StringVar()
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var)
btn_drink1.select()
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var)
btn_drink3 = Radiobutton(root, text="판타", value="판타", variable=drink_var)
# 생성과 동시에 .pack() 을 사용하면 select()를 사용할 수 없게 된다.
# pack 는 따로 하는것이 좋을 것 같다.

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()
btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


def btncmd():
    print(burger_var.get(), "선택") # value 값을 반환한다.
    print(drink_var.get(), "선택한 음료")

btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() # 반복을 하겠다
