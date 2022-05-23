from tkinter import*
from tkinter import ttk,messagebox
from tkinter.messagebox import QUESTION
from PIL import Image,ImageTk # pip install pillow
import pymysql # pip install pymysql

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #===Bg Image===
        self.bg=ImageTk.PhotoImage(file="images/bg5.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
        
         #===LEFT Image===
        self.left=ImageTk.PhotoImage(file="images/side11.jpg")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)
        
        #====Register Frame====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)
        
        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="brown").place(x=50,y=30)
        
        #-----------------------Row1
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)
        
        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)
        
        #-----------------------Row2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)
        
        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)
        
        #-----------------------Row3
        question=Label(frame1,text="Select security questions",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=240)
        
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your first Pet Name","Your Birth place","Your Best friend Name","Your favourite Colour",)
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Security answer",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)
        
        #-----------------------Row4
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)
        
        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)
        
        #------------terms----------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree to the Terms and Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)

        self.btn__img=ImageTk.PhotoImage(file="images/signin1.png")
        btn__img=Button(frame1,image=self.btn__img,bd=0,cursor="hand2",bg="white").place(x=50,y=420)
    
        self.btn_img=ImageTk.PhotoImage(file="images/register6.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=370,y=420)
        
    def clear(self):   
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)
    
    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():  
            messagebox.showerror("Error","Password and Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree to our Terms & Conditions",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="library2")
                cur=con.cursor()
                cur.execute("select * from register where email=%s",self.txt_email.get())
                row=cur.fetchone()
                # print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already exist,Please try with another email",parent=self.root)
                else:    
                    cur.execute("insert into register (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                     (self.txt_fname.get(),
                                      self.txt_lname.get(),
                                      self.txt_contact.get(),
                                      self.txt_email.get(),
                                      self.cmb_quest.get(),
                                      self.txt_answer.get(),
                                      self.txt_password.get()
                                     ))
                     
                     
                    con.commit()
                    con.close()
                    messagebox.showinfo("Sucess","Register Successful",parent=self.root)
                self.clear()
            except Exception as es: 
                  messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)   
            
            
           
        
root=Tk()
obj=Register(root)
root.mainloop()
        
        