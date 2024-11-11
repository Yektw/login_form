from tkinter import * 
from tkinter import messagebox
from mydb1 import Database

db = Database("c:/module/users_info.db")

root = Tk()
root.geometry("500x300")
root.title("Login Form")
root.configure(bg="white")
#funcs==========================================
def signup():
    if not ent_email.get() and not ent_pass.get():
        messagebox.showerror("Error","Email and Password must be filled!!!")
        return
    if db.search(ent_email.get(),ent_pass.get()):
        messagebox.showerror("Incorrect login","You have already signed up.")
        return
    db.insert(ent_fname.get(),ent_lname.get(),ent_email.get(),ent_pass.get())
    messagebox.showinfo("Success","Sign Up was successful.")
    
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_email.delete(0,END)
    ent_pass.delete(0,END)
    ent_fname.focus_set()

def signin():
    if not ent_email.get() and not ent_pass.get():
        messagebox.showerror("Error","Email and Password must be filled!!!")
        return
    result = db.search(ent_email.get(),ent_pass.get())

    if result:
        root.destroy()
        win1 = Tk()
        win1.geometry("300x300")
        win1.title("Welcome")
        win1.configure(bg="#9caf88")
        for rec in result:
         lbl_welcome = Label(win1,text=f'Welcome {rec[1]} {rec[2]}',font="arial 15 bold",fg="white",bg="#9caf88").pack(pady=50)
    else:
        messagebox.showerror("Error","Invalid email or password.")
#labels=========================================
lbl_fname = Label(root,text="Fname:",font="arial 12 bold",bg="white")
lbl_fname.place(x=100,y=20)

lbl_lname = Label(root,text="Lname:",font="arial 12 bold",bg="white")
lbl_lname.place(x=100,y=60)

lbl_email = Label(root,text="Email:",font="arial 12 bold",bg="white")
lbl_email.place(x=100,y=100)
lbl_star = Label(root,text='*',font="arial 16 bold",fg="red",bg="white").place(x=195,y=102)

lbl_pass = Label(root,text="Password:",font="arial 12 bold",bg="white")
lbl_pass.place(x=100,y=140)
lbl_star = Label(root,text='*',font="arial 16 bold",fg="red",bg="white").place(x=195,y=142)

#entries========================================
ent_fname = Entry(root,font="arial 10 bold",width=25)
ent_fname.place(x=220,y=22)
ent_lname = Entry(root,font="arial 10 bold",width=25)
ent_lname.place(x=220,y=62)
ent_email = Entry(root,font="arial 10 bold",width=25)
ent_email.place(x=220,y=102)
ent_pass = Entry(root,font="arial 10 bold",show="*",width=25)
ent_pass.place(x=220,y=142)
#buttons========================================
btn_up = Button(root,text="Sign Up",font="arial 12 bold",bg="blue",fg="white",width=12,command=signup)
btn_up.place(x=110,y=210)

btn_in = Button(root,text="Sign In",font="arial 12 bold",bg="green",fg="white",width=12,command=signin)
btn_in.place(x=270,y=210)

root.mainloop()
