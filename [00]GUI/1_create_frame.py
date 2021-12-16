from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정
#root.geometry("640x480+100+300")    # 가로 * 세로 + x좌표 + y좌표

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 


root.mainloop() # 반복을 하겠다
