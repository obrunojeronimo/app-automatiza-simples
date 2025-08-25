import os, shutil, glob
from tkinter import filedialog, messagebox
from natsort import natsorted
from PyPDF2 import PdfMerger


def organizar_arquivos():
    try:
        pasta = filedialog.askdirectory(title="Selecione a pasta para organizar")
        if not pasta:
            return

        extensoes = {
            ".pdf": "PDFs",
            ".jpg": "Imagens",
            ".jpeg": "Imagens",
            ".png": "Imagens",
            ".gif": "Imagens",
            ".bmp": "Imagens",
            ".svg": "Imagens",
            ".webp": "Imagens",
            ".tiff": "Imagens",
            ".jfif": "Imagens",
            ".xlsx": "Planilhas",
            ".xls": "Planilhas",
            ".csv": "Planilhas",
            ".ods": "Planilhas",
            ".docx": "Documentos",
            ".doc": "Documentos",
            ".txt": "Textos",
            ".pptx": "Apresentações",
            ".ppt": "Apresentações",
            ".mp4": "Videos",
            ".mov": "Videos",
            ".mp3": "Audios",
            ".wav": "Audios",
            ".flac": "Audios",
            ".m4a": "Audios",
            ".aac": "Audios",
            ".zip": "Compactados",
            ".rar": "Compactados",
        }

        for arquivo in os.listdir(pasta):
            caminho_arquivo = os.path.join(pasta, arquivo)
            if not os.path.isfile(caminho_arquivo):
                continue

            nome, ext = os.path.splitext(arquivo)
            ext = ext.lower()
            if ext not in extensoes:
                continue

            destino = os.path.join(pasta, extensoes[ext])
            os.makedirs(destino, exist_ok=True)

            contador = 1
            novo_nome = arquivo
            while os.path.exists(os.path.join(destino, novo_nome)):
                novo_nome = f"{nome}_{contador}{ext}"
                contador += 1

            shutil.move(caminho_arquivo, os.path.join(destino, novo_nome))

        messagebox.showinfo("Sucesso", "Arquivos organizados com sucesso!")
    except:
        messagebox.showerror("Erro", "Ocorreu um problema ao organizar os arquivos.")


def unificar_pdfs():
    try:
        pasta = filedialog.askdirectory(title="Selecione a pasta com PDFs")
        if not pasta:
            return

        pdfs = natsorted(glob.glob(os.path.join(pasta, "*.pdf")))
        if not pdfs:
            messagebox.showwarning("Aviso", "Nenhum PDF encontrado!")
            return

        merger = PdfMerger()
        for pdf in pdfs:
            try:
                merger.append(pdf)
            except:
                continue

        saida = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF", "*.pdf")],
            title="Salvar PDF unificado como",
            initialdir=pasta,
            initialfile="pdf_unificado.pdf",
        )
        if not saida:
            merger.close()
            return

        merger.write(saida)
        merger.close()
        messagebox.showinfo("Sucesso", f"PDF unificado salvo em:\n{saida}")
    except:
        messagebox.showerror("Erro", "Ocorreu um problema ao unificar os PDFs.")
