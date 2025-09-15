import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image
import os


def selecionar_arquivo_imagem():

    root = tk.Tk()
    root.withdraw()


    tipos_de_arquivo = (
        ("Imagens", "*.png *.jpg *.jpeg *.webp"),
        ("Todos os arquivos", "*.*")
    )

  
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione a imagem para remover o fundo",
        filetypes=tipos_de_arquivo
    )

    return caminho_arquivo

def remover_fundo_e_salvar(caminho_entrada):
  
    if not caminho_entrada:
        print("Nenhum arquivo foi selecionado. Operação cancelada.")
        return

    print(f"-> Processando imagem: {os.path.basename(caminho_entrada)}")

    try:
        imagem_entrada = Image.open(caminho_entrada)
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado em '{caminho_entrada}'")
        return
    except Exception as e:
        print(f"Erro ao abrir a imagem: {e}")
        return

    diretorio = os.path.dirname(caminho_entrada)
    nome_base, _ = os.path.splitext(os.path.basename(caminho_entrada))
    caminho_saida = os.path.join(diretorio, f"{nome_base}_nobg.png")

    try:
       
        imagem_saida = remove(imagem_entrada)

        imagem_saida.save(caminho_saida)
        print(f"Sucesso! Imagem sem fundo salva em: {caminho_saida}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante o processamento: {e}")


if __name__ == "__main__":
    print("--- Removedor de Background de Imagem ---")
    print("Uma janela se abrirá para você escolher o arquivo.")
    caminho_do_arquivo = selecionar_arquivo_imagem()
    remover_fundo_e_salvar(caminho_do_arquivo)
    print("\nProcesso concluído!")