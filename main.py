#!/usr/bin/env python

from tkinter import *
import customtkinter

# Set the theme and color options
customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class FirstScreen(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Calculadora de investimentos')
        self.geometry('300x250')

        self.campo_texto_dinheiro = customtkinter.CTkLabel(self, text='Valor do investimento:')
        self.campo_texto_dinheiro.pack()

        self.campo_dinheiro_emprestado = customtkinter.CTkEntry(self, height=10)
        self.campo_dinheiro_emprestado.pack()

        self.campo_texto_juro = customtkinter.CTkLabel(self, text='Valor do juro (%):')
        self.campo_texto_juro.pack()

        self.campo_dinheiro_juro = customtkinter.CTkEntry(self, height=10)
        self.campo_dinheiro_juro.pack()

        self.campo_texto_tempo = customtkinter.CTkLabel(self, text='Tempo (anos):')
        self.campo_texto_tempo.pack()

        self.campo_dinheiro_tempo = customtkinter.CTkEntry(self, height=10)
        self.campo_dinheiro_tempo.pack()

        self.button = customtkinter.CTkButton(self, text="Calcular", command=self.Conta)
        self.button.pack(pady=10)

        # Create label for displaying result
        self.label = customtkinter.CTkLabel(self, text='')
        self.label.pack(pady=10)

    def Conta(self):
        valor_emprestimo = int(self.campo_dinheiro_emprestado.get())
        valor_juro = int(self.campo_dinheiro_juro.get()) / 100
        valor_tempo = int(self.campo_dinheiro_tempo.get())
        
        valor_emprestimo_total = valor_emprestimo * ((valor_juro + 1) ** valor_tempo)

        # Update label text
        self.label.configure(text=f'O investimento retornará R${int(valor_emprestimo_total)} em {valor_tempo} anos')

# Define app and Create our app's mainloop
if __name__ == '__main__':
    app = FirstScreen()
    app.mainloop()
