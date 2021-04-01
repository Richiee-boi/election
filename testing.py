from tkinter import *
from tkinter import messagebox


def show_frame(frame):
    frame.tkraise()


def frame3_btncmd():
    show_frame(frame1)
    messagebox.showinfo('success','your vote has been casted')

#====================candidate names=========================
c1_name="gopi"

root=Tk()
root.title("SMC Election")
root.state('zoomed')
root.resizable(False,False)

root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

frame1=Frame(root,bg="violet")
frame2=Frame(root,bg="grey")
frame3=Frame(root,bg="red")

for frame in (frame1,frame2,frame3):
    frame.grid(row=0,column=0,sticky='news')

show_frame(frame1)

#==================frame1==================================

frame1_title=Label(frame1,text='VERIFICATON',font=("Copperplate Gothic Bold",50),bg='violet')
frame1_title.pack(fill='x')


frame1_entry=Entry(frame1,width=30,font=("Times New Roman",26)).pack(pady=50)

frame1_btn=Button(frame1,text='Enter Election',font=("Times New Roman",20),command=lambda:show_frame(frame2))
frame1_btn.pack()

#==================frame2==================================

frame2_title=Label(frame2,text='VOTE FOR CAPTIANS',font=("Copperplate Gothic Bold",50),bg='grey')
frame2_title.pack(fill='x')

frame2_C1=Label(frame2,text="1> "+c1_name,font=("Times New Roman",15)).place(x=100,y=100)

frame2_btn=Button(frame2,text='Cast Vote',font=("Times New Roman",15),command=lambda:show_frame(frame3))
frame2_btn.place(x=640,y=700)

#==================frame3==================================

frame3_title=Label(frame3,text='VOTE FOR VICE CAPTAINS',font=("Copperplate Gothic Bold",50),bg='red')
frame3_title.pack(fill='x')

frame3_btn=Button(frame3,text='Cast Vote',font=("Times New Roman",15),command=lambda:frame3_btncmd())
frame3_btn.place(x=640,y=700)









root.mainloop()