from tkinter import *
from main import *
from tkintermapview import TkinterMapView
from Twilio import *

def raise_frame(frame):
    frame.tkraise()

root = Tk()
root.geometry("850x600")

home = Frame(root)
result = Frame(root)

for frame in (home, result):
    frame.grid(row=0, column=0, sticky='news')

# Making Home frame
raise_frame(home)

label = Label(home, text="Welcome", font='Arial 12 bold')
label.grid(row=0, column=0, padx=10, pady=10)

coordinates = Entry(home)
coordinates.grid(row=1, column=0, padx=10, pady=10)

label2 = Label(home, text="Enter coordinates: latitude, longitude").grid(row=1, column=1, padx=5, pady=10)

map_view = TkinterMapView(home, width=600, height=400)
map_view.grid(row=2, column=0, padx=10, pady=10)

phno = Entry(home)
phno.grid(row=3, column=0, padx=10, pady=10)
var1 = IntVar()
c1 = Checkbutton(home, text='Get Updates',variable=var1, onvalue=1, offvalue=0)
c1.grid(row=3, column=1, padx=10, pady=10)

Button(home, text="Submit", command=lambda:submit_home()).grid(row=4, column=0, padx=10, pady=10)

def submit_home():
    coordinate = coordinates.get().split(" ")
    json = main(float(coordinate[0]), float(coordinate[1]))
    if var1.get()==1:
        print('in here')
        main_messaging(float(coordinate[0]), float(coordinate[1]), phno.get())    
    raise_frame(result)
    print(json)
    coordinates.delete(0, END)
    setup_result(json)

# Making result frame

def setup_result(json):
    Label(result, wraplength=400, text=json['rotationTxt']).grid(row=0, column=0, padx=10, pady=10)
    '''
    text= Text(result, wrap=WORD)
    text.insert(INSERT, json['rotationTxt'])
    text.grid(row=0, column=0, padx=10, pady=10)
    '''
    crops = json['cropSpecific']
    row=1
    for i in crops:
        Label(result, text=i).grid(row=row, column=0, padx=10, pady=10)
        Label(result, wraplength=400, text=crops[i]).grid(row=row, column=1, padx=10, pady=10)
        row += 1

    Button(result, text='Back', command=lambda:back_result()).grid(row=row+1, column=0, padx=10, pady=10)

def back_result():
    raise_frame(home)
    for widget in result.winfo_children():
        widget.destroy()
    
root.mainloop()