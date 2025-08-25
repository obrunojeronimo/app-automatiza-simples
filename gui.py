import os
import sys
import webbrowser
from PIL import Image
import customtkinter as ctk
from src.arquivos import organizar_arquivos, unificar_pdfs
from src.imagens import imagens_para_pdf
from src.qr_code import gerar_qrcode


# ---------------- Recursos do PyInstaller ---------------- #
def resource_path(relative_path):
    """Retorna o caminho absoluto para recursos, funciona com PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------- Funções ---------------- #
def enviar_sugestao():
    webbrowser.open("https://forms.gle/6YSQ4UKysb5sLa8v9")


# ---------------- Interface ---------------- #
def criar_interface():
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Automatiza Simples")
    root.geometry("450x600")
    root.resizable(False, False)

    # Centralizar janela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width // 2) - (450 // 2)
    y = (screen_height // 2) - (600 // 2)
    root.geometry(f"450x600+{x}+{y}")

    # Ícone da janela
    try:
        root.iconbitmap(resource_path("assets/icone_ico.ico"))
    except:
        pass

    # Títulos
    titulo = ctk.CTkLabel(root, text="Automatiza Simples", font=("Arial", 18, "bold"))
    titulo.pack(pady=20)
    subtitulo = ctk.CTkLabel(root, text="Escolha uma opção:", font=("Arial", 13))
    subtitulo.pack(pady=10)

    # Botões principais
    botoes = [
        ("Organizar Arquivos", organizar_arquivos),
        ("Converter Imagens em PDF", imagens_para_pdf),
        ("Unificar PDFs", unificar_pdfs),
        ("Gerar QR Code", lambda: gerar_qrcode(root)),
        ("Enviar Sugestão", enviar_sugestao),
        ("Sair", root.destroy),
    ]

    for texto, comando in botoes:
        cor_fundo = "#008000" if texto != "Sair" else "#b81414"
        btn = ctk.CTkButton(
            root,
            text=texto,
            command=comando,
            width=300,
            height=40,
            fg_color=cor_fundo,
            text_color="white",
            font=("Arial", 11, "bold"),
        )
        btn.pack(pady=10)

    # Botão de alternar tema com ícones
    img_sol = ctk.CTkImage(Image.open(resource_path("assets/sol.png")), size=(30, 30))
    img_lua = ctk.CTkImage(Image.open(resource_path("assets/lua.png")), size=(30, 30))

    def alternar_tema():
        modo = ctk.get_appearance_mode()
        if modo == "Light":
            ctk.set_appearance_mode("Dark")
            btn_tema.configure(image=img_sol)
        else:
            ctk.set_appearance_mode("Light")
            btn_tema.configure(image=img_lua)

    btn_tema = ctk.CTkButton(
        root, text="", image=img_sol, command=alternar_tema, width=50, height=50
    )
    btn_tema.pack(pady=10)

    # Rodapé
    rodape = ctk.CTkLabel(
        root,
        text="Desenvolvido por Bruno Jerônimo para automatizar tarefas simples do dia a dia",
        font=("Arial", 10),
    )
    rodape.pack(side="bottom", pady=15)

    root.mainloop()
