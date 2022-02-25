import tkinter as t
from PIL import Image,ImageTk
import mysql.connector as c
from tkinter import messagebox 

class party:
    
    def dblogin(self,event,p):
        
        con=c.connect(host="localhost",user="root",password="root@123",database="voting")
        cor=con.cursor()
        cor.execute("update registration set status=1 ,party=%s where aadhar=%s ",(p,self.aid))
        con.commit()
        con.close()
        messagebox.showwarning("Thanks","Thanks")
        self.window.destroy()
        
    def __init__(self,aid):
        self.window=t.Tk()
        self.aid=aid

        positionRight = int(self.window.winfo_screenwidth()/2 - 900/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 750/2)

        self.window.geometry("+{}+{}".format(positionRight, positionDown))

        self.window.overrideredirect(1)

        img=Image.open("flgg.jpg")
        new_img=img.resize((750,820))
        new_img.save("flgg.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.place(x=0,y=0)


        head=t.Label(text="PARTIES",fg="green",bg="white",font=("Arial Bold", 30))
        head.grid(row="1",column="0",pady=20,padx=200,ipadx=80,ipady=20,columnspan=2)
        



        self.b=t.StringVar()
        self.c=t.StringVar()
        self.a=t.StringVar()
        self.cp=t.StringVar()
        self.i=t.StringVar()
        self.n=t.StringVar()

        img1=Image.open("bjp.png")
        new_img1=img1.resize((100,70))
        new_img1.save("bjp.png")
        act_img1=ImageTk.PhotoImage(new_img1)

        bjp=t.Button(text="BJP",textvariable=self.b,image=act_img1,bg="white")
        bjp.grid(row="2",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img2=Image.open("Cong.jpg")
        new_img2=img2.resize((100,70))
        new_img2.save("Cong.jpg")
        act_img2=ImageTk.PhotoImage(new_img2)

        cong=t.Button(text="CONGRESS",textvariable=self.c,image=act_img2,bg="white")
        cong.grid(row="2",column="1",pady=10,padx=0,ipadx=50,ipady=50)

        img3=Image.open("aap.jpg")
        new_img3=img3.resize((100,70))
        new_img3.save("aap.jpg")
        act_img3=ImageTk.PhotoImage(new_img3)

        aap=t.Button(text="AAP",textvariable=self.a,image=act_img3,bg="white")
        aap.grid(row="3",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img4=Image.open("jjp.png")
        new_img4=img4.resize((100,70))
        new_img4.save("jjp.png")
        act_img4=ImageTk.PhotoImage(new_img4)
        
        jjp=t.Button(text="CPI",textvariable=self.cp,image=act_img4,bg="white")
        jjp.grid(row="3",column="1",pady=10,padx=0,ipadx=50,ipady=50,columnspan=1)


        img5=Image.open("inld.jpg")
        new_img5=img5.resize((100,70))
        new_img5.save("inld.jpg")
        act_img5=ImageTk.PhotoImage(new_img5)

        inld=t.Button(text="INLD",textvariable=self.i,image=act_img5,bg="white")
        inld.grid(row="4",column="0",pady=10,padx=20,ipadx=50,ipady=50)

        img6=Image.open("nota.webp")
        new_img6=img6.resize((100,70))
        new_img6.save("nota.webp")
        act_img6=ImageTk.PhotoImage(new_img6)

        nota=t.Button(text="NOTA",textvariable=self.n,image=act_img6,bg="white")
        nota.grid(row="4",column="1",pady=10,padx=0,ipadx=50,ipady=50)

        #cnfrm=t.Button(text="Submit",fg="green",bg="white",font=("Arial Bold", 17))
        #cnfrm.grid(row="5",column="0",pady=20,padx=200,ipadx=80,ipady=20,columnspan=2)




        bjp.bind("<Button-1>",lambda event,p="bjp":self.dblogin(event,p))
        cong.bind("<Button-1>",lambda event,p="cong":self.dblogin(event,p))
        aap.bind("<Button-1>",lambda event,p="aap":self.dblogin(event,p))
        jjp.bind("<Button-1>",lambda event,p="jjp":self.dblogin(event,p))
        inld.bind("<Button-1>",lambda event,p="inld":self.dblogin(event,p))
        nota.bind("<Button-1>",lambda event,p="nota":self.dblogin(event,p))

        #cnfrm.bind("<Button-1>",lambda event:self.setparty(event))
        t.mainloop()

        
        

     

        


