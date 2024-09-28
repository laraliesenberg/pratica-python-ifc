import sys
import os

def cauda_arquivo_texto(nome_do_arquivo):
    if not os.path.exists(nome_do_arquivo):
        print("Erro: esse arquivo não existe")
        return
        
    with open(nome_do_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()
        ultimas_linhas = linhas[-10:]

    for i, linha in enumerate(ultimas_linhas):
        print(f'{i + 1}: {linha}', end='')
           

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    
    nome_do_arquivo = sys.argv[1]
    cauda_arquivo_texto(nome_do_arquivo)

if __name__ == "__main__":
    main()