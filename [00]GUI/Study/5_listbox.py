from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# extended : 여러개 선택 가능
# single : 하나만 선택 가능
# height : 보여지는 높이, 0 은 전부 보여 주겠다는 뜻
# 3으로 하면 3칸만 보여지고 나머지는 스크롤된다.
listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0,"사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤에 항목을 삭제
    # listbox.delete(0) # 맨 앞에 항목을 삭제

    # 갯수 확인
    print("리스트박스에는", listbox.size(), "개가 있어요")

    # 항목 확인(시작 인덱스, 끝 인덱스)
    print("1번째부터 3번째까지의 항목 :" , listbox.get(0,2))

    # 선택된 항목 확인
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 반복을 하겠다
