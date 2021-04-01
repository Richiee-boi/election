from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry('1360x700+0+0')
window.title("ELECTION")
window.config(bg="grey")

#===============variables===================
cb1=IntVar()
cb2=IntVar()
cb3=IntVar()
cb4=IntVar()
cb5=IntVar()
cb6=IntVar()
cb7=IntVar()
cb8=IntVar()
cb9=IntVar()
cb10=IntVar()

vcounting1=0
vcounting2=0
vcounting3=0
vcounting4=0
vcounting5=0
vcounting6=0
vcounting7=0
vcounting8=0
vcounting9=0
vcounting10=0

#================functions====================

def show_frame(frame):
    frame.tkraise()

def framereveal():
    for i in (detailframe,castframe):
        i.place(x=460,y=90,width=900,height=610)


    show_frame(castframe)

def casting():
    global vcounting1
    global vcounting2
    global vcounting3
    global vcounting4
    global vcounting5
    global vcounting6
    global vcounting7
    global vcounting8
    global vcounting9
    global vcounting10
    if cb1.get()==1:
        vcounting1+=1
    
    
    if cb2.get()==1:
        vcounting2+=1


    if cb3.get()==1:
        vcounting3+=1
    

    if cb4.get()==1:
        vcounting4+=1

    
    if cb5.get()==1:
        vcounting5+=1


    if cb6.get()==1:
        vcounting6+=1
    

    if cb7.get()==1:
        vcounting7+=1

    
    if cb8.get()==1:
        vcounting8+=1


    if cb9.get()==1:
        vcounting9+=1


    if cb10.get()==1:
        vcounting10+=1


    if (vcounting1+vcounting2+vcounting3+vcounting4+vcounting5+vcounting6+vcounting7+vcounting8+vcounting9+vcounting10)!=4:
        if (vcounting1+vcounting2+vcounting3+vcounting4+vcounting5+vcounting6+vcounting7+vcounting8+vcounting9+vcounting10)>=4:
            messagebox.showerror('error','only select 4 members')
            vcounting1=0
            vcounting2=0
            vcounting3=0
            vcounting4=0
            vcounting5=0
            vcounting6=0
            vcounting7=0
            vcounting8=0
            vcounting9=0
            vcounting10=0
        elif (vcounting1+vcounting2+vcounting3+vcounting4+vcounting5+vcounting6+vcounting7+vcounting8+vcounting9+vcounting10)<=4:
            messagebox.showerror('error','plz select 4 members')

    else:
        messagebox.showinfo('success','vote casted successfully')
        window.destroy()
        import main_2

#    print(vcounting1)
#    print(vcounting2)
#    print(vcounting3)
#    print(vcounting4)
#    print(vcounting5)
#    print(vcounting6)
#    print(vcounting7)
#    print(vcounting8)
#    print(vcounting9)
#    print(vcounting10)


#    print(cb1.get())
#    print(cb2.get())
#    print(cb3.get())
#    print(cb4.get())
 #   print(cb5.get())
#    print(cb6.get())
#    print(cb7.get())
#    print(cb8.get())
#    print(cb9.get())
#    print(cb10.get())
#================names=============
c1='1'
c2='2'
c3='3'
c4='4'
c5='5'
c6='6'
c7='7'
c8='8'
c9='9'
c10='10'

#================title frame================================
title_frame=Frame(window,bd=6,relief='ridge',bg='grey')
title_frame.pack(side=TOP,fill=X)

frame1_title=Label(title_frame,text='VOTE FOR CAPTIANS',font=("Copperplate Gothic Bold",50),bg='grey',fg='white')
frame1_title.pack(fill='x')


#=================name frame==================================

nameframe=Frame(window,bd=6,relief='ridge',bg='grey')
nameframe.place(x=0,y=90,height=610,width=460)

C1=Button(nameframe,text=c1,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C2=Button(nameframe,text=c2,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C3=Button(nameframe,text=c3,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C4=Button(nameframe,text=c4,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C5=Button(nameframe,text=c5,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C6=Button(nameframe,text=c6,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C7=Button(nameframe,text=c7,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C8=Button(nameframe,text=c8,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C9=Button(nameframe,text=c9,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
C10=Button(nameframe,text=c10,font=("Times New Roman",15,'bold'),command=lambda:show_frame(detailframe)).pack(fill='x',pady=10,padx=7)
#frame1_btn=Button(frame2,text='Cast Vote',font=("Times New Roman",15),command=lambda:show_frame(frame3))
#frame1_btn.place(x=640,y=700)

#=================detail frame===================================
detailframe=Frame(window,bd=6,relief='ridge',bg='grey')
detailframe.place(x=460,y=90,width=900,height=610)

T1=Button(detailframe,text="detail frame",font=("Times New Roman",15,'bold'),).pack(fill='x',pady=10,padx=7)

close=Button(detailframe,text='CLOSE',font=("Times New Roman",15,'bold'),command=lambda:show_frame(castframe)).pack()
#=================cast frame===================================
castframe=Frame(window,bd=6,relief='ridge',bg='grey')
castframe.place(x=460,y=90,width=900,height=610)

T1=Button(castframe,text="cast frame",font=("Times New Roman",15,'bold')).pack(fill='x',pady=10,padx=7)

V1=Checkbutton(castframe,text=c1,variable=cb1,bg='grey',activebackground='grey',height=2).pack()
V2=Checkbutton(castframe,text=c2,variable=cb2,bg='grey',activebackground='grey',height=2).pack()
V3=Checkbutton(castframe,text=c3,variable=cb3,bg='grey',activebackground='grey',height=2).pack()
V4=Checkbutton(castframe,text=c4,variable=cb4,bg='grey',activebackground='grey',height=2).pack()
V5=Checkbutton(castframe,text=c5,variable=cb5,bg='grey',activebackground='grey',height=2).pack()
V6=Checkbutton(castframe,text=c6,variable=cb6,bg='grey',activebackground='grey',height=2).pack()
V7=Checkbutton(castframe,text=c7,variable=cb7,bg='grey',activebackground='grey',height=2).pack()
V8=Checkbutton(castframe,text=c8,variable=cb8,bg='grey',activebackground='grey',height=2).pack()
V9=Checkbutton(castframe,text=c9,variable=cb9,bg='grey',activebackground='grey',height=2).pack()
V10=Checkbutton(castframe,text=c10,variable=cb10,bg='grey',activebackground='grey',height=2).pack()



castbutton=Button(castframe,text="cast vote",font=("Times New Roman",15,'bold'),command=casting).pack(pady=10,padx=7)








framereveal()

window.resizable(False,False)
window.mainloop()