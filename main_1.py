from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as pysql


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

counting1=0
counting2=0
counting3=0
counting4=0
counting5=0
counting6=0
counting7=0
counting8=0
counting9=0
counting10=0

namelst=[]

c1=''
c2=''
c3=''
c4=''
c5=''
c6=''
c7=''
c8=''
c9=''
c10=''
#================Pictures=====================
PIC_C1=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C1.jpg'))
PIC_C2=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C2.jpg'))
PIC_C3=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C3.jpg'))
PIC_C4=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C4.jpg'))
PIC_C5=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C5.jpg'))
PIC_C6=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C6.jpg'))
PIC_C7=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C7.jpg'))
PIC_C8=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C8.jpg'))
PIC_C9=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C9.jpg'))
PIC_C10=ImageTk.PhotoImage(Image.open(r'D:\usb\current[_project\election\C\C10.jpg'))



#================functions====================

def show_frame(frame):
    frame.tkraise()

def framereveal():
    for i in (detailframe,castframe):
        i.place(x=460,y=90,width=900,height=610)


    show_frame(castframe)

def casting():
    global counting1
    global counting2
    global counting3
    global counting4
    global counting5
    global counting6
    global counting7
    global counting8
    global counting9
    global counting10
    if cb1.get()==1:
        counting1+=1
    
    
    if cb2.get()==1:
        counting2+=1


    if cb3.get()==1:
        counting3+=1
    

    if cb4.get()==1:
        counting4+=1

    
    if cb5.get()==1:
        counting5+=1


    if cb6.get()==1:
        counting6+=1
    

    if cb7.get()==1:
        counting7+=1

    
    if cb8.get()==1:
        counting8+=1


    if cb9.get()==1:
        counting9+=1


    if cb10.get()==1:
        counting10+=1


    if (counting1+counting2+counting3+counting4+counting5+counting6+counting7+counting8+counting9+counting10)!=4:
        if (counting1+counting2+counting3+counting4+counting5+counting6+counting7+counting8+counting9+counting10)>=4:
            messagebox.showerror('error','only select 4 members')
            counting1=0
            counting2=0
            counting3=0
            counting4=0
            counting5=0
            counting6=0
            counting7=0
            counting8=0
            counting9=0
            counting10=0
        elif (counting1+counting2+counting3+counting4+counting5+counting6+counting7+counting8+counting9+counting10)<=4:
            messagebox.showerror('error','plz select 4 members')

    else:
        messagebox.showinfo('success','vote casted successfully')
        window.destroy()
        import main_2

#====================geting candidate picture========================
def call_details_C1():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C1).place(x=200,y=80)

def call_details_C2():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C2).place(x=200,y=80)

def call_details_C3():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C3).place(x=200,y=80)

def call_details_C4():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C4).place(x=200,y=80)

def call_details_C5():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C5).place(x=200,y=80)

def call_details_C6():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C6).place(x=200,y=80)

def call_details_C7():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C7).place(x=200,y=80)

def call_details_C8():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C8).place(x=200,y=80)

def call_details_C9():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C9).place(x=200,y=80)

def call_details_C10():
    show_frame(detailframe)
    picture=Label(detailframe,image=PIC_C10).place(x=200,y=80)


def Fetching_name():
    db=pysql.connect(host='localhost',user='root',passwd='2234841',database='election')
    cur=db.cursor()
    cur.execute('select Name from captains Order By Name ASC')

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

frame1_title=Label(title_frame,text='VOTE FOR CAPTIANS',font=("Copperplate Gothic Bold",50),bg='grey',fg='white')
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


close=Button(detailframe,text='CLOSE',font=("Times New Roman",15,'bold'),command=lambda:show_frame(castframe)).pack()
#=================cast frame===================================
castframe=Frame(window,bd=6,relief='ridge',bg='grey')
castframe.place(x=460,y=90,width=900,height=610)

V1=Checkbutton(castframe,text=c1,variable=cb1,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=130)
V2=Checkbutton(castframe,text=c2,variable=cb2,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=170)
V3=Checkbutton(castframe,text=c3,variable=cb3,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=210)
V4=Checkbutton(castframe,text=c4,variable=cb4,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=250)
V5=Checkbutton(castframe,text=c5,variable=cb5,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=290)
V6=Checkbutton(castframe,text=c6,variable=cb6,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=330)
V7=Checkbutton(castframe,text=c7,variable=cb7,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=370)
V8=Checkbutton(castframe,text=c8,variable=cb8,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=410)
V9=Checkbutton(castframe,text=c9,variable=cb9,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=450)
V10=Checkbutton(castframe,text=c10,variable=cb10,font=("Times New Roman",15,'bold'),bg='grey',activebackground='grey',height=2).place(x=200,y=490)



castbutton=Button(castframe,text="cast vote",font=("Times New Roman",15,'bold'),command=casting).pack(pady=10,padx=7)








framereveal()

window.resizable(False,False)
window.mainloop()