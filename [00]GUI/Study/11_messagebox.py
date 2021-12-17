from tkinter import *   # 윈도우 창 같은 것을 사용할 수 있게 하는것
import tkinter.messagebox as msgbox

root = Tk() # 만든다
root.title("Mitier GUI")    # 윈도우창 이름
root.geometry("640x480")    # 가로 * 세로, 크기 지정

# 팝업박스

def info():
    msgbox.showinfo("알림", "정상적으로 작동")

def warn():
    msgbox.showwarning("경고", "해당 메시지는 경고입니다.")

def error():
    msgbox.showerror("에러", "강력한 에러가 발생")

def okcancel():
    msgbox.askokcancel("확인취소", "이것을 할거니?")

def retrycancel():
    msgbox.askretrycancel("재시도취소", "다시 할거니?")

def yesno():
    msgbox.askyesno("예 아니오", "이거 진짜 할거니?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="저장되지 않았다 \n 저장후 종료 할래?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 저장 하지 않고 취소 (현재 화면에서 계속 작업)
    print("응답", response) # True, False, None : 예, 아이오, 취소 : 1, 0 , 나머지
    if response == 1:
        print("예스")
    elif response == 0:
        print("아니오")
    else:
        print("취소")


Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="획인취소").pack()
Button(root, command=retrycancel, text="재시도취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()


root.mainloop() # 반복을 하겠다
