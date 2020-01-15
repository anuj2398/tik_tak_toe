from tkinter import *
from tkinter import messagebox as m
root=Tk()
root.geometry("400x350")
root.resizable(width=False,height=False)
root.title("GAME")
label=Label(root,text="Tik_tak_toe")
label=Label(root,text="Tik_tak_toe",bg="black",fg="white",font=("Ariel",15,"bold"),padx=1550)
label.pack(side=TOP)
root.config(background="orange")
turn=1
def clicked(a):
    global turn
    if a=='0':
        if btn0["text"]==" ":
            if turn==1:
                turn=2
                btn0["text"]="X"
            else:
                turn=1
                btn0["text"]="O"
            wins()
    if a=='1':
        if btn1["text"]==" ":
            if turn==1:
                turn=2
                btn1["text"]="X"
            else:
                turn=1
                btn1["text"]="O"
            wins()
    if a=='2':
        if btn2["text"]==" ":
            if turn==1:
                turn=2
                btn2["text"]="X"
            else:
                turn=1
                btn2["text"]="O"
            wins()
    if a=='3':
        if btn3["text"]==" ":
            if turn==1:
                turn=2
                btn3["text"]="X"
            else:
                turn=1
                btn3["text"]="O"
            wins()
    if a=='4':
        if btn4["text"]==" ":
            if turn==1:
                turn=2
                btn4["text"]="X"
            else:
                turn=1
                btn4["text"]="O"
            wins()
    if a=='5':
        if btn5["text"]==" ":
            if turn==1:
                turn=2
                btn5["text"]="X"
            else:
                turn=1
                btn5["text"]="O"
            wins()
    if a=='6':
        if btn6["text"]==" ":
            if turn==1:
                turn=2
                btn6["text"]="X"
            else:
                turn=1
                btn6["text"]="O"
            wins()
    if a=='7':
        if btn7["text"]==" ":
            if turn==1:
                turn=2
                btn7["text"]="X"
            else:
                turn=1
                btn7["text"]="O"
            wins()
    if a=='8':
        if btn8["text"]==" ":
            if turn==1:
                turn=2
                btn8["text"]="X"
            else:
                turn=1
                btn8["text"]="O"
            wins()
def close():
    root.destroy()
def restart():
    global turn
    turn=1
    btn0["text"]=" "
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
over=0
def wins():
    global turn,over
    b0=btn0["text"]
    b1=btn1["text"]
    b2=btn2["text"]
    b3=btn3["text"]
    b4=btn4["text"]
    b5=btn5["text"]
    b6=btn6["text"]
    b7=btn7["text"]
    b8=btn8["text"]
    over=over+1
    if over==9:
        over=0
        disp="Opps! no one wins"
        m.showinfo(disp)
        restart()
    else:
        if (b0=="X" and b1=="X" and b2=="X") or (b0=="O" and b1=="O" and b2=="O"):
            msg(turn)
        elif (b0=="X" and b4=="X" and b8=="X") or (b0=="O" and b4=="O" and b8=="O"):
            msg(turn)
        elif (b0=="X" and b3=="X" and b6=="X") or (b0=="O" and b3=="O" and b6=="O"):
            msg(turn)
        elif (b3=="X" and b4=="X" and b5=="X") or (b3=="O" and b4=="O" and b5=="O"):
            msg(turn)
        elif (b6=="X" and b7=="X" and b8=="X") or (b6=="O" and b7=="O" and b8=="O"):
            msg(turn)
        elif (b1=="X" and b4=="X" and b7=="X") or (b1=="O" and b4=="O" and b7=="O"):
            msg(turn)
        elif (b2=="X" and b5=="X" and b8=="X") or (b2=="O" and b5=="O" and b8=="O"):
            msg(turn)
        elif (b2=="X" and b4=="X" and b6=="X") or (b2=="O" and b4=="O" and b6=="O"):
            msg(turn)
def msg(player):
    if player==1:
        player=2
    else:
        player=1
    disp="Game complete sucessfully and player ",player,"wins :)"
    m.showinfo("CONGRATULATIONS",disp)
    restart()
btn0=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('0'))
btn0.place(x=100,y=50)
btn1=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('1'))
btn1.place(x=175,y=50)
btn2=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('2'))
btn2.place(x=250,y=50)
btn3=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('3'))
btn3.place(x=100,y=124)
btn4=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('4'))
btn4.place(x=175,y=124)
btn5=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('5'))
btn5.place(x=250,y=124)
btn6=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('6'))
btn6.place(x=100,y=198)
btn7=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('7'))
btn7.place(x=175,y=198)
btn8=Button(root,text=" ",bg="white",fg="black",width=9,height=4,command=lambda:clicked('8'))
btn8.place(x=250,y=198)
btnrestart=Button(root,text="RESTART",bg="green",fg="white",width=9,height=4,command=lambda:restart())
btnrestart.place(x=250,y=270)
btnclose=Button(root,text="CLOSE",bg="red",fg="white",width=9,height=4,command=lambda:close())
btnclose.place(x=100,y=270)
root.mainloop()
