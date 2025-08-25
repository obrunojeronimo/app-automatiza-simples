import qrcode
from tkinter import filedialog, messagebox, simpledialog


def gerar_qrcode(parent):
    try:
        texto = simpledialog.askstring(
            "QR Code",
            "Digite ou cole o link/texto para gerar o QR Code:",
            parent=parent,
        )
        if not texto:
            return

        nome = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("Imagens PNG", "*.png"), ("Todos os arquivos", "*.*")],
            title="Salvar QR Code como",
            initialfile="qrcode.png",
        )
        if not nome:
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(texto)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(nome)
        messagebox.showinfo("Sucesso", f"QR Code salvo em:\n{nome}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um problema ao gerar o QR Code:\n{e}")
