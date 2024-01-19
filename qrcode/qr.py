from tkinter import *
from tkinter import messagebox,filedialog
import qrcode
from PIL import ImageTk, Image


#the 1 screen
root = Tk()
root.geometry("300x400")
root.title("QR Code ")
root.config(bg='#4E4E4E')
welcome = Label(root,text="WELCOME TO QR Code :)",fg='white',bg='#4E4E4E',font=('Helvetica', 14))
welcome.pack(pady=40)


#the 2 screen
def home():
    root.destroy()
    app = Tk()
    app.geometry("300x400")
    app.title("QR Code ")
    app.config(bg='#4E4E4E')


    #for generate qr code
    def generate_qr_code():
            text = text_entry.get()

            qr = qrcode.QRCode(version=1, box_size=5, border=2)
            qr.add_data(text)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            img = img.resize((200,200))
            img_tk = ImageTk.PhotoImage(img)
            qr_label.configure(image=img_tk)
            qr_label.image = img_tk
     # for saving qr code
    def save_qr_code():
                img = qr_label.image
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
                if file_path:
                        img.save(file_path)
                        messagebox.showinfo("Save QR Code", f"QR Code saved as {file_path}")

    text_label = Label(app, text="Enter Text or URL:",bg='#4E4E4E',fg="white")
    text_label.pack(pady=10)
    text_entry =Entry(app, width=40 ,bg="#D9D9D9")
    text_entry.pack()

    generate_button = Button(app, text="Generate QR Code",
    command=generate_qr_code,bg='#9DFF50',width=15,font=('arial', 10,'bold'))
    generate_button.pack(pady=10)
    # for saving
    save_button = Button(app, text="Save QR Code",
    command=save_qr_code,bg='#9DFF50',width=15,font=('arial', 10,'bold'))
    save_button.pack(pady=10)
    #qr label
    qr_label = Label(app)
    qr_label.pack()
    app.mainloop()


#for sign in
def signin():
        root.destroy()
        sign = Tk()
        sign.geometry("300x400")
        sign.title("QR Code ")
        sign.config(bg='#4E4E4E')
        welcome = Label(sign,text="WELCOME TO SIGN IN ",bg='#9DFF50',font=('Helvetica', 14),width=20)
        welcome.pack(pady=40)
        #username
        user = Label(sign,text='Enter your username:',bg='#4E4E4E',fg='white')
        user.pack()
        #userentry
        user_entry = Entry(sign,width=30,bg='#D9D9D9')
        user_entry.pack(pady=10)
        #password
        password = Label(sign,text='Enter your password:',bg='#4E4E4E',fg='white')
        password.pack()
        #entrypassentry
        password_entry = Entry(sign,width=30,bg='#D9D9D9',show='*')
        password_entry.pack(pady=10)
        #confpass
        password_c = Label(sign,text='Password confirmation:',bg='#4E4E4E',fg='white')
        password_c.pack()
        #confpass
        password_ce = Entry(sign,width=30,bg='#D9D9D9',show='*')
        password_ce.pack(pady=10)

        #def check 
        def ons():
               #get all data 
               user=user_entry.get()
               pas = password_entry.get()
               pasc = password_ce.get()
               if not user or not pas or not pasc:
                      messagebox.showerror("Error", "Please fill in all fields.")
               elif pas != pasc :
                     messagebox.showerror("Error", "Password and Confirm Password do not match.") 
               else:
                  messagebox.showinfo("Registration Successful", "You are now registered!")
                  show(user)  
       #user screen
        def show(user):
               sign.destroy()
               homuser = Tk()
               homuser.geometry('400x400')
               homuser.title(F'wlcome {user} to QR code app')
               homuser.config(bg='#4E4E4E')
               #img 
              #  image_path = "pro.jpg"
              #  image = Image.open(image_path)
              #  resized_image = image.resize((40, 40))
              #  photo = ImageTk.PhotoImage(resized_image)
              #  im =Label(homuser,image=photo)
              #  im.place(x=4,y=4)
               usern = Label(homuser,text=f'{user}')
               usern.place(x=50,y=4)
               #link img with f
               welcome = Label(homuser,text=f'{user} WELCOME TO QR Code :)'.upper(),fg='white',bg='#4E4E4E',font=('Helvetica', 10,))
               welcome.pack(pady=40)
               
               homuser.mainloop()
        #button sing in 
        btns = Button(sign,text="Sign in",command=ons,bg='#9DFF50',width=20)
        btns.pack(pady=20)
        sign.mainloop()



#FOR BUTTON TO START
btn = Button(root,text="Start",command=home,bg='#9DFF50',width=20)
btn.pack(pady=20)
#for sing in
btns = Button(root,text="Sign in",command=signin,bg='#9DFF50',width=20)
btns.pack(pady=20)

info_label =Label(root, text="Sign in to unlock additional features:\n- Save your generated QR codes for future reference.\n- Scan and read QR codes effortlessly.",bg='#4E4E4E',width=60,fg='#9DFF50',font=('arial',8))
info_label.pack(pady=20)
footer_label = Label(root, text="© 2024 QR Code. All rights reserved YatSYatTech.", font=("Helvetica", 8), foreground="gray",bg='#4E4E4E')
footer_label.pack(side="bottom", pady=10)
root.mainloop()
