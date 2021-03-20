# bad coding
import datetime
# importing tkinter
from tkinter import *
# importing calendar module
import calendar
# initializing tkinter
root = Tk()
# setting title of our Gui
root.title("CALENDÁRIO SIMPLES - 2021")
# year for which we want the calendar to e shown on our Gui
year = 2021
# starting 2021 year calendar data inside myCal
myCal = calendar.calendar(year)
# showing caldendar data using label widget
call_year = Label(root, text=myCal, font="Consolas 10 bold")
# packing the Label widget
call_year.pack()
# running the program in ready state
root.mainloop()

