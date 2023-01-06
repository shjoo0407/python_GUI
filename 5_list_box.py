from tkinter import *

root = Tk()
root.title("Sehyun GUI")
root.geometry("640x480")

listbox = Listbox(root,selectmode = "extended",height=0)
listbox.insert(0,"사과")
listbox.insert(1,"딸기")
listbox.insert(2,"바나나")
listbox.insert(END,"수박")
listbox.insert(END,"포도")
listbox.pack()


def btncmd():
    #삭제
    #listbox.delete(END)
    #항목확인
    #print(listbox.get(0,2))
    #선택된 항목 확인(위치로 반환)
    print("선택된 항목 : ", listbox.curselection())

btn = Button(root,text="클릭",command=btncmd())
btn.pack()
root.mainloop()
