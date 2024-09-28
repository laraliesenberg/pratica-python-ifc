import sys
import os

def concatenar_arquivos(nomes_dos_arquivos):
    for nome_do_arquivo in nomes_dos_arquivos:
        if not os.path.exists(nome_do_arquivo):
            print(f"Erro: o arquivo '{nome_do_arquivo}' não existe")
            continue

        try:
            with open(nome_do_arquivo, "r") as arquivo:
                conteudo = arquivo.read()
                print(conteudo, end='')  
        except Exception as e:
            print(f"Erro ao ler o arquivo '{nome_do_arquivo}': {e}")
            continue

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    
    nomes_dos_arquivos = sys.argv[1:]  
    concatenar_arquivos(nomes_dos_arquivos)

if __name__ == "__main__":
    main()
