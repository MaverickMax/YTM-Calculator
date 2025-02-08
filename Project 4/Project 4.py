import tkinter as tk
import pandas as pd
import numpy as np
#from YTMCalculator import*

def answer():
    print(fv,pv,r,t)

window = tk.Tk()

window.geometry("500x300")
window.title("YTM CALCULATOR")
window.config(background="white")
label = tk.Label (window, text="YTM CALCULATOR")
label.grid(row=0,column=0)

label = tk.Label(window,text='Face Value:')
fv = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=1,column=1)
fv.grid(row=1,column=2)
button.grid(row=1,column=3)

label = tk.Label(window,text='Market Price:')
pv = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=2,column=1)
pv.grid(row=2,column=2)
button.grid(row=2,column=3)

label = tk.Label(window,text='Coupon Rate:')
c = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=3,column=1)
c.grid(row=3,column=2)
button.grid(row=3,column=3)

label = tk.Label(window,text='Years:')
t = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=4,column=1)
t.grid(row=4,column=2)
button.grid(row=4,column=3)

label = tk.Label(window,text='payments per year:')
r = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=5,column=1)
r.grid(row=5,column=2)
button.grid(row=5,column=3)



label = tk.Label(window,text='Yield to Maturity:')
ytm = tk.Entry(window,)
button = tk.Button(window,text="Enter")
label.grid(row=6,column=1)
fv.grid(row=6,column=2)
button.grid(row=6,column=3)

button = tk.Button(window,text='Enter')
button.config(command=answer)
button.grid(row=7,column=2)

coupon = tk.Label(window)
print(pv,fv,c,r,t)
window.mainloop()






