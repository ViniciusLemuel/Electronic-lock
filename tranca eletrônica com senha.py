import os
from tkinter import *
from playsound import playsound

def click_button(numero):
    #função botão
    visor.insert(END,(numero))

def click_ok():
    #função ok
    numero = visor.get()
    visor.delete(0,END)

    if numero == "177": #senha 177
        #abre arquivo e reproduz som de acerto
        os.startfile(r"C:\Users\Lemuel\Desktop\Lemuel")
        playsound(r'C:\Users\Lemuel\Desktop\Projetos\somAcerto.WAV')
    else:
        #apresenta erro e reproduz alarme de erro
        os.startfile(r"C:\Users\Lemuel\Desktop\Projetos\imagemFalha.jpg")
        playsound(r'C:\Users\Lemuel\Desktop\Projetos\somAlarme.WAV')
janela = Tk()
janela.Title = "Senha"

lb1=Label(janela, text="", font= ("arial", 20, "bold"), pady=10)
lb1.pack()

visor = Entry(janela, bg="lightblue")
visor.pack()

#fileira 1
bt0 = Button(janela, text="1", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(1))
bt0.place(x=10, y=100)

bt1 = Button(janela, text="4", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(4))
bt1.place(x=10, y=155)

bt2 = Button(janela, text="7", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(7))
bt2.place(x=10, y=210)

bt3 = Button(janela, text="*", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button("*"))
bt3.place(x=10, y=265)

#fileira 2
bt4 = Button(janela, text="2", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(2))
bt4.place(x=65, y=100)

bt5 = Button(janela, text="5", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(5))
bt5.place(x=65, y=155)

bt6 = Button(janela, text="8", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(8))
bt6.place(x=65, y=210)

bt7 = Button(janela, text="0", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(0))
bt7.place(x=65, y=265)


#fileira 3
bt8 = Button(janela, text="3", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(3))
bt8.place(x=120, y=100)

bt9 = Button(janela, text="6", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(6))
bt9.place(x=120, y=155)

bt10 = Button(janela, text="9", bg="lightblue", pady=14, padx=14, bd=4, command= lambda: click_button(9))
bt10.place(x=120, y=210)

#botão ok
bt11 = Button(janela, text="#", bg="lightblue", pady=14, padx=14, bd=4, command= click_ok)
bt11.place(x=120, y=265)

janela.resizable(False, False)
janela.geometry('180x330')
janela.mainloop()