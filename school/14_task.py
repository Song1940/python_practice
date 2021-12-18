from tkinter import *
from PIL import ImageTk
import tkinter.messagebox
import tkinter.simpledialog


win  = Tk()
win.title("introduce myself")


canvas = Canvas(win, width = 500, height = 400)
canvas.pack()

img_path = ImageTk.PhotoImage(file = '/Users/kimsong/Desktop/python/school/KakaoTalk_Photo_2021-07-30-00-50-23.jpeg' )
shapes = canvas.create_image(250, 200, image = img_path)

def bclick():
    tkinter.messagebox.showinfo("환영","안녕하세요! 경제통상학부 3학년 김송입니다 :)")

btn = Button(win, text = "welcome",  foreground = 'Blue' ,font = 'Arial 20 italic', command = bclick)
btn.pack(side = LEFT , fill = Y, padx = 40)

global la_result

def radio():
    if var_info.get ==1:
        tkinter.messagebox.showinfo("이름", "제 이름은 김송입니다!")



var_info = IntVar()


def info():

    smallwin = Tk()
    smallwin.title("Song's info")
    smallwin.geometry("400x400")
    radio1 = Radiobutton(smallwin, text = "김송",  value = 1, variable =var_info)
    radio2 = Radiobutton(smallwin, text = "26세",  value = 2, variable =var_info)
    radio3 = Radiobutton(smallwin, text = "BI 융합전공으로 컴퓨터공학 배우는중",  value = 3, variable =var_info)

    label = Label(smallwin, text = "*함수내에서 또 이벤트 처리를 해보고싶었는데 실패했습니다...",fg = 'Red')
    label.pack(side = TOP , pady = 20)

    radio1.pack(side = TOP, pady = 40)
    radio2.pack(side = TOP, pady = 40)
    radio3.pack(side = TOP, pady = 40)

infobtn = Button(win, text = "about me", foreground = "Red", font = "돋움체 20",command = info)
infobtn.pack(side = LEFT, fill = Y, padx =40)
def easterclick():
    name = tkinter.simpledialog.askstring("Q","성함이 어떻게 되시나요?")
    if name == "류춘화":
        tkinter.messagebox.showinfo("Thanks", "교수님 한학기동안 정말 감사했습니다. 즐거운 방학되세요 :)")
    else:
        tkinter.messagebox.showwarning("Oops", "제가 찾는 사람이 아니군요..")
        tkinter.messagebox.showinfo("Hint", "누가 파이썬을 가르쳐 주셨죠?")

easterbtn = Button(win, text = "who are you?", font = 'Arial 20', foreground = 'Green', command = easterclick)
easterbtn.pack(side = LEFT ,fill = Y,padx = 40 )
quitbtn = Button(win, text = 'quit', font = '궁서체 20' , command = quit)
quitbtn.pack(side = LEFT , fill = Y,padx = 40)

win.mainloop()