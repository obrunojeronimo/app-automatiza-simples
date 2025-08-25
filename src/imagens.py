from tkinter import filedialog, messagebox
from PIL import Image
from natsort import natsorted


def imagens_para_pdf():
    try:
        pasta = filedialog.askdirectory(title="Selecione a pasta com imagens")
        if not pasta:
            return

        tipos_imagem = (
            ".jpg",
            ".png",
            ".jpeg",
            ".gif",
            ".bmp",
            ".tiff",
            ".webp",
            ".jfif",
        )
        arquivos = [f for f in os.listdir(pasta) if f.lower().endswith(tipos_imagem)]
        if not arquivos:
            messagebox.showwarning("Aviso", "Nenhuma imagem encontrada!")
            return

        arquivos = natsorted(arquivos)
        imagens = []
        for arquivo in arquivos:
            try:
                img = Image.open(os.path.join(pasta, arquivo)).convert("RGB")
                imagens.append(img)
            except:
                continue

        if not imagens:
            messagebox.showerror("Erro", "Nenhuma imagem pôde ser processada!")
            return

        saida_pdf = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")],
            title="Salvar PDF como",
            initialdir=pasta,
            initialfile="imagens_convertidas.pdf",
        )
        if not saida_pdf:
            return

        imagens[0].save(saida_pdf, save_all=True, append_images=imagens[1:])
        messagebox.showinfo("Sucesso", f"PDF gerado em:\n{saida_pdf}")
    except:
        messagebox.showerror("Erro", "Ocorreu um problema ao gerar o PDF.")
