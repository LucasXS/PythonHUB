from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry("600x600")
Label(root, text="Qual páis você deseja viajar? ",
      font="lucidia 16 bold").pack()

country = ["Australia", "EUA", "Japão", "Espanha", "Italia", "Argentina"]
var = StringVar()
new_var = var.set(" nonewhere")


def travel():
    tmsg.showinfo("Vamos viajar", f"Então, estamos reservando seu voou para {var.get()}"
                                  f"\nNós desejamos a você uma boa jornada. Obrigado por viajar conosco!")

    for x in range(6):
        Radiobutton(root, text=country[x], variable=var,
                    value=country[x]).pack()


Button(root, text="Vamos viajar", command=travel).pack()
root.mainloop()
