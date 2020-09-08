from tkinter import *
from tkinter.ttk import Frame, Button, Entry, Style

content = ''

# enters a key press to screen and content variable
def enter_val(val):
    global content
    content += val
    equation.set(content)


# clears the user's screen and content variable
def clear_screen():
    global content
    content = ''
    equation.set(content)


# uses python built in eval() function to evaluate the expression built up in content variable, displays to screen
def evaluate():
    global content
    try:
        result = str(eval(content))
        equation.set(result)
    except:
        content = ''
        equation.set('Error')


# program start and GUI creation
if __name__ == "__main__":
    root = Tk()

    root.title('Calculator')
    Style().configure("TButton", padding=(0, 5, 0, 5),
        font='serif 10')

    root.columnconfigure(0, pad=3)
    root.columnconfigure(1, pad=3)
    root.columnconfigure(2, pad=3)
    root.columnconfigure(3, pad=3)

    root.rowconfigure(0, pad=3)
    root.rowconfigure(1, pad=3)
    root.rowconfigure(2, pad=3)
    root.rowconfigure(3, pad=3)
    root.rowconfigure(4, pad=3)

    equation = StringVar()

    # Grid row:0
    screen = Entry(root, textvariable=equation)
    screen.grid(row=0, columnspan=4, sticky=W+E)
    equation.set(content)

    # Grid row:1
    b_7 = Button(root, text="7", command=lambda: enter_val('7'))
    b_7.grid(row=1, column=0)
    b_8 = Button(root, text="8", command=lambda: enter_val('8'))
    b_8.grid(row=1, column=1)
    b_9 = Button(root, text="9", command=lambda: enter_val('9'))
    b_9.grid(row=1, column=2)
    b_ce = Button(root, text="CE", command=clear_screen)
    b_ce.grid(row=1, column=3)

    # Grid row:2
    b_4 = Button(root, text="4", command=lambda: enter_val('4'))
    b_4.grid(row=2, column=0)
    b_5 = Button(root, text="5", command=lambda: enter_val('5'))
    b_5.grid(row=2, column=1)
    b_6 = Button(root, text="6", command=lambda: enter_val('6'))
    b_6.grid(row=2, column=2)
    b_div = Button(root, text="/", command=lambda: enter_val('/'))
    b_div.grid(row=2, column=3)

    # Grid row:3
    b_1 = Button(root, text="1", command=lambda: enter_val('1'))
    b_1.grid(row=3, column=0)
    b_2 = Button(root, text="2", command=lambda: enter_val('2'))
    b_2.grid(row=3, column=1)
    b_3 = Button(root, text="3", command=lambda: enter_val('3'))
    b_3.grid(row=3, column=2)
    b_mul = Button(root, text="*", command=lambda: enter_val('*'))
    b_mul.grid(row=3, column=3)

    # Grid row:4
    b_0 = Button(root, text="0", command=lambda: enter_val('0'))
    b_0.grid(row=4, column=0)
    b_equ = Button(root, text="=", command=evaluate)
    b_equ.grid(row=4, column=1)
    b_plu = Button(root, text="+", command=lambda: enter_val('+'))
    b_plu.grid(row=4, column=2)
    b_min = Button(root, text="-", command=lambda: enter_val('-'))
    b_min.grid(row=4, column=3)

    root.mainloop()
