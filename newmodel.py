from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector as pysql


window = Tk()
window.geometry('1360x700+0+0')
window.title("ELECTION")
window.config(bg="grey")




#===============functions===========================
def show_title_frame(frame):
    if frame in (title_frame_veri,title_frame_cap,title_frame_vcap):
        frame.pack(side=TOP,fill=X)
    frame.tkraise()
    
def new_title(frame):
    title_frame_veri.pack_forget()
    title_frame_cap.pack_forget()
    title_frame_vcap.pack_forget()
    show_title_frame(frame)

def cast_vote_cap(a,b,c):
    title_frame_veri.pack_forget()
    title_frame_cap.pack_forget()
    title_frame_vcap.pack_forget()
    verification_frame.place_forget()
    castframe_cap.place_forget()
    detailframe_cap.place_forget()


    
#================title frame's================================
title_frame_veri=Frame(window,bd=6,relief='ridge',bg='grey')

Button(title_frame_veri,text='veri',font=("Times New Roman",15,'bold'),command=lambda:new_title(title_frame_cap)).pack(fill='x',pady=10,padx=7)

verification_frame=Frame(window,bd=6,relief='ridge',bg='grey').place(x=450,y=150,height=500,width=500)


title_frame_cap=Frame(window,bd=6,relief='ridge',bg='grey')
Button(title_frame_cap,text='cap',font=("Times New Roman",15,'bold'),command=lambda:new_title(title_frame_vcap)).pack(fill='x',pady=10,padx=7)
castframe=Frame(window,bd=6,relief='ridge',bg='grey').place(x=460,y=90,width=900,height=610)
detailframe=Frame(window,bd=6,relief='ridge',bg='grey').place(x=460,y=90,width=900,height=610)


title_frame_vcap=Frame(window,bd=6,relief='ridge',bg='grey')

Button(title_frame_vcap,text='vcap',font=("Times New Roman",15,'bold'),command=lambda:new_title(title_frame_veri)).pack(fill='x',pady=10,padx=7)



#==============main code==================
for i in (title_frame_veri,title_frame_cap,title_frame_vcap):
    i.pack_forget()
show_title_frame(title_frame_veri)

for a in (verification_frame,castframe,detailframe):
    i.place_forget()
show_title_frame(verification_frame)


window.mainloop()