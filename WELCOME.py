import tkinter as t
from PIL import Image,ImageTk
import Mainpage as ma
import time
class Welcome:
    def __init__(self):
        self.window=t.Tk()
        
        positionRight = int(self.window.winfo_screenwidth()/2 - 500/2)
        positionDown = int(self.window.winfo_screenheight()/2 - 300/2)

        self.window.geometry("+{}+{}".format(positionRight, positionDown))

        self.window.overrideredirect(1)

        img=Image.open("india.jpg")
        new_img=img.resize((500,300))
        new_img.save("india.jpg")
        act_img=ImageTk.PhotoImage(new_img)

        label=t.Label(image=act_img)
        label.pack()
        self.window.after(3000,self.demo)

        t.mainloop()
    def demo(self):
        self.window.destroy()
        tt=ma.main()
    


if __name__=="__main__":
    w=Welcome()

     

