import sys
import os

def numerar_linhas_arquivo(arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: o arquivo '{arquivo_entrada}' não existe")
        return

    try:
        with open(arquivo_entrada, "r") as entrada, open(arquivo_saida, "w") as saida:
            i = 0
            for i, linha in enumerate(entrada):
                saida.write(f'{i + 1}: {linha}')
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

def main():
    if len(sys.argv) < 3:
        print("Erro: nenhum argumento foi fornecido")
        return
    
    arquivo_entrada = sys.argv[1] 
    arquivo_saida = sys.argv[2] 
    numerar_linhas_arquivo(arquivo_entrada, arquivo_saida)

if __name__ == "__main__":
    main()
