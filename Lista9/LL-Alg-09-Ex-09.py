import sys
import os

def remocao_de_comentarios(arquivo_entrada, arquivo_saida):
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: o arquivo '{arquivo_entrada}' não existe")
        return

    try:
        with open(arquivo_entrada, "r") as entrada, open(arquivo_saida, "w") as saida:
            linhas = entrada.readlines()
            for linha in linhas:
                linha_sem_comentario = linha.split("#")[0]
                saida.write(linha_sem_comentario.rstrip() + '\n')
            
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return

def main():
    if len(sys.argv) < 3:
        print("Erro: nenhum argumento foi fornecido")
        return
    
    arquivo_entrada = sys.argv[1] 
    arquivo_saida = sys.argv[2] 
    remocao_de_comentarios(arquivo_entrada, arquivo_saida)

if __name__ == "__main__":
    main()
