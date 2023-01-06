from tkinter import *

root = Tk()
root.title("Sehyun GUI")
btn1 = Button(root, text="버튼1")
btn1.pack()

btn2 = Button(root, padx=5,pady=10, text="버튼2")
btn2.pack()

btn3 = Button(root, padx=10,pady=5, text = "버튼3")
btn3.pack()

# 고정된 크기
btn4 = Button(root, width=0, height=3, text="버튼4")
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text = "버튼5")
btn5.pack()

photo = PhotoImage(file="C:/SHproject/GUI/img.png")
btn6 = Button(root, image = photo)
btn6.pack()

def btncmd():
    print("원영아 사랑해")

btn7 = Button(root, text="원영이는 누르시오.", command=btncmd)
btn7.pack()

root.mainloop()
