from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as pysql


window = Tk()
window.geometry('1360x700+0+0')
window.title("ELECTION")
window.config(bg="grey")

#===============variables===================
namelst=[]

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

#================Pictures==============
PIC_VC1=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC1.jpg'))
PIC_VC2=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC2.jpg'))
PIC_VC3=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC3.jpg'))
PIC_VC4=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC4.jpg'))
PIC_VC5=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC5.jpg'))
PIC_VC6=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC6.jpg'))
PIC_VC7=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC7.jpg'))
PIC_VC8=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC8.jpg'))
PIC_VC9=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC9.jpg'))
PIC_VC10=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\VC\VC10.jpg'))

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


def Fetching_name():
    db=pysql.connect(host='localhost',user='root',passwd='2234841',database='election')
    cur=db.cursor()
    cur.execute('select Name from vicecaptains Order By Name ASC')
    
    datacur=cur.fetchall()
    for name in datacur:
        name=name[0]
        namelst.append(str(name))
    db.commit()

#================names=============
Fetching_name()

try:
    c1=namelst[0]
    c2=namelst[1]
    c3=namelst[2]
    c4=namelst[3]
    c5=namelst[4]
    c6=namelst[5]
    c7=namelst[6]
    c8=namelst[7]
    c9=namelst[8]
    c10=namelst[9]
except:
    pass

#================title frame================================
title_frame=Frame(window,bd=6,relief='ridge',bg='grey')
title_frame.pack(side=TOP,fill=X)

frame1_title=Label(title_frame,text='VOTE FOR VICE CAPTIANS',font=("Copperplate Gothic Bold",50),bg='grey',fg='white')
frame1_title.pack(fill='x')


#=================name frame==================================

nameframe=Frame(window,bd=6,relief='ridge',bg='grey')
nameframe.place(x=0,y=90,height=610,width=460)

C1=Button(nameframe,text=c1,font=("Times New Roman",15,'bold'),command=lambda:call_details_C1()).pack(fill='x',pady=10,padx=7)
C2=Button(nameframe,text=c2,font=("Times New Roman",15,'bold'),command=lambda:call_details_C2()).pack(fill='x',pady=10,padx=7)
C3=Button(nameframe,text=c3,font=("Times New Roman",15,'bold'),command=lambda:call_details_C3()).pack(fill='x',pady=10,padx=7)
C4=Button(nameframe,text=c4,font=("Times New Roman",15,'bold'),command=lambda:call_details_C4()).pack(fill='x',pady=10,padx=7)
C5=Button(nameframe,text=c5,font=("Times New Roman",15,'bold'),command=lambda:call_details_C5()).pack(fill='x',pady=10,padx=7)
C6=Button(nameframe,text=c6,font=("Times New Roman",15,'bold'),command=lambda:call_details_C6()).pack(fill='x',pady=10,padx=7)
C7=Button(nameframe,text=c7,font=("Times New Roman",15,'bold'),command=lambda:call_details_C7()).pack(fill='x',pady=10,padx=7)
C8=Button(nameframe,text=c8,font=("Times New Roman",15,'bold'),command=lambda:call_details_C8()).pack(fill='x',pady=10,padx=7)
C9=Button(nameframe,text=c9,font=("Times New Roman",15,'bold'),command=lambda:call_details_C9()).pack(fill='x',pady=10,padx=7)
C10=Button(nameframe,text=c10,font=("Times New Roman",15,'bold'),command=lambda:call_details_C10()).pack(fill='x',pady=10,padx=7)
#frame1_btn=Button(frame2,text='Cast Vote',font=("Times New Roman",15),command=lambda:show_frame(frame3))
#frame1_btn.place(x=640,y=700)

#=================detail frame===================================
detailframe=Frame(window,bd=6,relief='ridge',bg='grey')
detailframe.place(x=460,y=90,width=900,height=610)

#T1=Button(detailframe,text="detail frame",font=("Times New Roman",15,'bold'),).pack(fill='x',pady=10,padx=7)

close=Button(detailframe,text='CLOSE',font=("Times New Roman",15,'bold'),command=lambda:show_frame(castframe)).pack()

def call_details_C1():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC1).place(x=200,y=80)

def call_details_C2():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC2).place(x=200,y=80)

def call_details_C3():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC3).place(x=200,y=80)

def call_details_C4():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC4).place(x=200,y=80)

def call_details_C5():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC5).place(x=200,y=80)

def call_details_C6():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC6).place(x=200,y=80)

def call_details_C7():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC7).place(x=200,y=80)

def call_details_C8():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC8).place(x=200,y=80)

def call_details_C9():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC9).place(x=200,y=80)

def call_details_C10():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_VC10).place(x=200,y=80)

#=================cast frame===================================
castframe=Frame(window,bd=6,relief='ridge',bg='grey')
castframe.place(x=460,y=90,width=900,height=610)


V1=Checkbutton(castframe,text=c1,font=("Times New Roman",15,'bold'),variable=cb1,bg='grey',activebackground='grey',height=2).place(x=200,y=130)
V2=Checkbutton(castframe,text=c2,font=("Times New Roman",15,'bold'),variable=cb2,bg='grey',activebackground='grey',height=2).place(x=200,y=170)
V3=Checkbutton(castframe,text=c3,font=("Times New Roman",15,'bold'),variable=cb3,bg='grey',activebackground='grey',height=2).place(x=200,y=210)
V4=Checkbutton(castframe,text=c4,font=("Times New Roman",15,'bold'),variable=cb4,bg='grey',activebackground='grey',height=2).place(x=200,y=250)
V5=Checkbutton(castframe,text=c5,font=("Times New Roman",15,'bold'),variable=cb5,bg='grey',activebackground='grey',height=2).place(x=200,y=290)
V6=Checkbutton(castframe,text=c6,font=("Times New Roman",15,'bold'),variable=cb6,bg='grey',activebackground='grey',height=2).place(x=200,y=330)
V7=Checkbutton(castframe,text=c7,font=("Times New Roman",15,'bold'),variable=cb7,bg='grey',activebackground='grey',height=2).place(x=200,y=370)
V8=Checkbutton(castframe,text=c8,font=("Times New Roman",15,'bold'),variable=cb8,bg='grey',activebackground='grey',height=2).place(x=200,y=410)
V9=Checkbutton(castframe,text=c9,font=("Times New Roman",15,'bold'),variable=cb9,bg='grey',activebackground='grey',height=2).place(x=200,y=450)
V10=Checkbutton(castframe,text=c10,font=("Times New Roman",15,'bold'),variable=cb10,bg='grey',activebackground='grey',height=2).place(x=200,y=490)



castbutton=Button(castframe,text="cast vote",font=("Times New Roman",15,'bold'),command=casting).pack(pady=10,padx=7)








framereveal()

window.resizable(False,False)
window.mainloop()