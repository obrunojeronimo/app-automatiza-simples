# Automatiza Simples

**Automatiza Simples** é uma aplicação desktop desenvolvida em Python com **CustomTkinter**, criada para automatizar tarefas básicas do dia a dia, como organizar arquivos, converter imagens em PDF, unificar PDFs e gerar QR Codes.

O aplicativo é modular, fácil de instalar e não exige privilégios de administrador. Inclui modos de interface **Light** e **Dark**, com alternância por botão e ícones intuitivos de Sol e Lua.

---

## Funcionalidades

- **Organizar Arquivos**: organiza arquivos da pasta escolhida por tipo (PDFs, Imagens, Planilhas, Documentos, Vídeos, Áudios, Compactados).  
- **Converter Imagens em PDF**: transforma todas as imagens de uma pasta em um único PDF, mantendo a ordem natural dos arquivos.  
- **Unificar PDFs**: junta todos os PDFs de uma pasta em um único arquivo.  
- **Gerar QR Code**: cria QR Codes a partir de links ou textos.  
- **Alternar Tema**: botão com ícones de Sol (Light) e Lua (Dark).  
- **Enviar Sugestão**: abre o cliente de e-mail com destinatário pronto para enviar sugestões de melhoria.  

---

## Pré-requisitos

- Windows 10 ou 11  
- Nenhuma instalação de Python necessária (executável standalone gerado com PyInstaller)  

---

## Instalação

1. Baixe o instalador: `AutomatizaSimples_Setup.exe`.  
2. Abra o instalador.  
3. Escolha a pasta de instalação (ou use a padrão).  
4. Opcional: marque para criar um atalho na Área de Trabalho.  
5. Clique em **Instalar**.  

> O instalador não requer privilégios de administrador.  

---

## Estrutura da instalação
C:\Users\<Usuário>\AppData\Roaming\Automatiza Simples
│
├── main.exe               # Executável principal
├── assets\                # Ícones e imagens do aplicativo
│   ├── icone_ico.ico
│   ├── sol.png
│   └── lua.png


---

## Uso

1. Abra o aplicativo pelo atalho ou `main.exe`.  
2. Escolha a funcionalidade desejada: organizar arquivos, gerar PDFs, unificar PDFs ou criar QR Codes.  
3. Para alternar o tema, clique no botão com ícone de **Sol** (modo Light) ou **Lua** (modo Dark).  
4. Para enviar sugestões de melhoria, clique em **Enviar Sugestão**.  

---

## Dicas de segurança

- O executável é standalone e não precisa de Python.  
- Caso o antivírus alerte, adicione a pasta de instalação como exceção.  
- Sempre baixe o instalador a partir de fontes confiáveis (como este repositório).  

---

## Desinstalação

- Vá em **Painel de Controle > Programas e Recursos** ou **Configurações > Aplicativos**.  
- Selecione **Automatiza Simples** e clique em **Desinstalar**.  
- Todos os arquivos, incluindo a pasta `assets`, serão removidos automaticamente.  

---

## Capturas de Tela

**Modo Light**  
![Light Theme](assets/sol.png)  

**Modo Dark**  
![Dark Theme](assets/lua.png)  

---

## Estrutura Modular

- `main.py` → inicia a interface  
- `gui.py` → interface CustomTkinter e botões  
- `src/arquivos.py` → funções de organização de arquivos  
- `src/imagens.py` → conversão de imagens em PDF  
- `src/pdfs.py` → unificação de PDFs  
- `src/qrcode_module.py` → geração de QR Code  
- `src/utils.py` → funções auxiliares (caminho de recursos para PyInstaller)  
- `assets/` → ícones e imagens  

---

## Autor

**Bruno Jerônimo**
[LinkedIn](https://www.linkedin.com/in/bruno-jeronimo/)
