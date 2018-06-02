from tkinter import *
from turtle import *
root=Tk()

root.geometry('400x600')
var1 = IntVar()
var2=IntVar()
var3=IntVar()

def blue_click():
   selection = str(var1.get())
   for key in blue_color1:
       if key==selection:
           screen=Screen()
           screen.setup(300,300)
           screen.bgcolor(blue_color1[key])
           selection = "You selected the option " + blue_color1[key]
           label.config(text = selection)

def red_click():
   selection = str(var2.get())
   for key in red_color1:
       if key==selection:
           screen=Screen()
           screen.setup(300,300)
           screen.bgcolor(red_color1[key])
           selection = "You selected the option " + red_color1[key]
           label.config(text = selection)

def green_click():
   selection = str(var3.get())
   for key in green_color1:
       if key==selection:
           screen=Screen()
           screen.setup(300,300)
           screen.bgcolor(green_color1[key])
           selection = "You selected the option " + green_color1[key]
           label.config(text = selection)


blue_color1={'0':'#388E8E',
            '1':'#37FDFC',
            '2':'#97FFFF',
            '3':'#05B8CC',
            '4':'#C1F0F6',
            '5':'#00BFFF',
            '6':'#236B8E',
            '7':'#1D7CF2',
            '8':'#003EFF',
            '9':'#8968CD',
            '10':'#6600FF'
    }

blue_color={'sgiteal': '#388E8E',
            'metallic mint':'#37FDFC',
            'darkslategray1':'#97FFFF',
            'cerulean':'#05B8CC',
            'pastel blue':'#C1F0F6',
            'deepskyblue':'#00BFFF',
            'steelblue': '#236B8E',
            'peafowl':'#1D7CF2',
            'cichlid':'#003EFF',
            'medium purple3':'#8968CD',
            'blue safe':'#6600FF'}

red_color=['lightsalmon','salmon','darksalmon','lightcoral','indianred'
           ,'crimson','firebrick','red','darkred','maroon','tomato','orangered',
           'palevioletred']

red_color1={'0':'#FFA07A','1':'#FA8072','2':'#E9967A',
            '3':'#F08080','4':'#CD5C5C','5':'#DC143C',
            '6':'#B22222','7':'#FF0000','8':'#8B0000','9':
            '#800000','10':'#FF6347','11':'#FF4500','12':
            '#DB7093'}

green_color=['lawngreen','limegreen','lime','forestgreen','green','darkgreen','greenyellow','yellowgreen','springgreen','mediumspringgreen','lightgreen','palegreen','mediumseagreen',
             'lightseagreen','seagreen','olive','darkolivegreen','olivedrab']

green_color1={'0':'#7CFC00','1':'#32CD32','2':'#00FF00','3':'#228B22','4':'#008000','5':'#006400','6':'#ADFF2F','7':'#9ACD32','8':'#00FF7F','9':'#00FA9A','10':'#90EE90','11':'#98FB98',
              '12':'#3CB371','13':'#20B2AA','14':'#2E8B57','15':'#808000','16':'#556B2F','17':'#6B8E23'}


colors = [
"blue",
"red",
"green"
]

variable = StringVar(root)
variable.set(colors[0]) # default value

w = OptionMenu(root, variable, *colors)
w.grid(row=0,column=4)

def ok():
    choice=variable.get()
    if choice=='blue':
        x=0
        j=3
        for key in blue_color:
            R1 = Radiobutton(root, text=key, variable=var1, value=x,command=blue_click).grid(row=j,column=0,sticky=W,columnspan=3)
            x=x+1
            j=j+1
            
    elif choice=='red':
        x=0
        j=3
        for i in red_color:
            R2 = Radiobutton(root, text=i, variable=var2, value=x,command=red_click).grid(row=j,column=3,sticky=W,columnspan=3)
            x=x+1
            j=j+1

    elif choice=='green':
        x=0
        j=3
        for i in green_color:
            R2 = Radiobutton(root, text=i, variable=var3, value=x,command=green_click).grid(row=j,column=6,sticky=W,columnspan=3)
            x=x+1
            j=j+1

b1=Button(root,text='Submit',command=ok).grid(row=1,column=4)

label = Label(root)
label.grid(row=2,column=1,columnspan=10)

root.mainloop()
