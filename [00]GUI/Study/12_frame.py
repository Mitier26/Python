from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정


Label(root, text="선택해줭").pack(side="top")

Button(root, text="주문하기").pack(side="bottom")

frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="고기햄버거").pack()
Button(frame_burger, text="치즈햄버거").pack()

# side      : 왼쪽, 오른쪽으로 정렬
# fill      : 빈칸을 없는것으로 채울지
# expend    : 확장하기 

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)
Button(frame_drink, text="꼴라").pack()
Button(frame_drink, text="싸이다").pack()


root.mainloop() # 반복을 하겠다
