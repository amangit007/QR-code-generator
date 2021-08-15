from tkinter import *
from tkinter import messagebox
import pyqrcode
import qrcode

from PIL import Image, ImageTk



window = Tk()
window.title("QR CODE GENERATOR")
window.config(bg='#F25252')
window.geometry('500x750')


def save_qr():


    img = qrcode.make(user_input.get())
    type(img)
    img.save(f'{user_input2.get()}.png')
    output.config(text='File saved with logo')
    generate_QR()

def generate_QR() :
    global qr, img
    if len(user_input.get()) != 0 :

        qr = pyqrcode.create(user_input.get())
        img = BitmapImage(data=qr.xbm(scale=8))
    else :
        messagebox.showwarning('warning', 'All Fields are Required!')
    try :
        display_code(img)
    except :
        pass


def display_code(img) :
    img_lbl.config(image=img)
    output.config(text="QR code of " + user_input.get())




def logo_qr():
    logo = Image.open(user_input3.get())
    basic = 100
    width_percentage = (basic/float(logo.size[0]))
    height_size = int((float(logo.size[1])*float(width_percentage)))
    logo = logo.resize((basic, height_size), Image.ANTIALIAS)
    qrc = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

    qrc.add_data(user_input.get())
    qrc.make()
    gen_img = qrc.make_image(
        fill_color='black',
        bg_color="#fff"
        ).convert('RGBA')

    position = ((gen_img.size[0] - logo.size[0]) // 2, (gen_img.size[1] - logo.size[1]) // 2)

    gen_img.paste(logo, position)
    pin=user_input2.get()+'.png'
    gen_img.save(pin)

    image1 = Image.open(pin)
    new = (200, 200)
    image1 = image1.resize(new)
    test = ImageTk.PhotoImage(image1)

    label1 = Label(image=test)
    label1.image = test
    label1.pack(pady=10)



    output.config(text='File saved with logo')



lbl = Label(window,text="QR Code Generator",bg='#F25252',font=('serif',20,'bold'))
lbl.pack()

lbl = Label(window,text="Enter Message or URL",bg='#F25252',font=('serif',12,'bold'))
lbl.pack()

user_input = StringVar()
entry = Entry(window,textvariable=user_input,font=('serif',16,'bold'))
entry.pack(padx=10)

button = Button(window,text="Generate QR",width=20,command=generate_QR,font=('serif',16,'bold'))
button.pack(pady=10)


lbl = Label(window,text="Enter filename",bg='#F25252',font=('serif',12,'bold'))
lbl.pack()

user_input2 = StringVar()
entry1 = Entry(window,textvariable=user_input2,font=('serif',16,'bold'))
entry1.pack(padx=10)

button1 = Button(window,text="Generate and save QR",width=20,command=save_qr,font=('serif',16,'bold'))
button1.pack(pady=10)

lbl = Label(window,text="Enter logo file path",bg='#F25252',font=('serif',12,'bold'))
lbl.pack()

user_input3 = StringVar()
entry2 = Entry(window,textvariable=user_input3,font=('serif',16,'bold'))
entry2.pack(padx=10)

button2 = Button(window,text="Generate logo QR",width=20,command=logo_qr,font=('serif',16,'bold'))
button2.pack(pady=10)

img_lbl = Label( window, bg='#F25252')
img_lbl.pack()

output = Label( window, text="",bg='#F25252',font=('serif',16,'bold'))
output.pack()

window.mainloop()
