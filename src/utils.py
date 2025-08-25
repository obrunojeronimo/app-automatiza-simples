import tkinter as tk
from tkinter import ttk
import time


def centralizar_janela(window, largura, altura):
    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (largura // 2)
    y = (window.winfo_screenheight() // 2) - (altura // 2)
    window.geometry(f"{largura}x{altura}+{x}+{y}")


def mostrar_barra_progresso():
    progresso = tk.Tk()
    progresso.title("Preparando Aplicativo")
    progresso.geometry("400x120")
    progresso.resizable(False, False)
    centralizar_janela(progresso, 400, 120)

    tk.Label(progresso, text="Preparando o aplicativo...", font=("Arial", 11)).pack(
        pady=10
    )
    barra = ttk.Progressbar(
        progresso, orient="horizontal", length=350, mode="determinate"
    )
    barra.pack(pady=20)
    progresso.update()

    for i in range(101):
        barra["value"] = i
        progresso.update()
        time.sleep(0.01)

    progresso.destroy()
