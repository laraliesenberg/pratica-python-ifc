import sys
import os

def palavra_longa_arquivo(nome_do_arquivo):
    if not os.path.exists(nome_do_arquivo):
        print("Erro: esse arquivo não existe")
        return
    
    try:     
        with open(nome_do_arquivo, "r") as arquivo:
            linha = arquivo.read()
            palavras = linha.split()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    dicionario = {}

    for palavra in palavras:
        tamanho = len(palavra)
        if tamanho not in dicionario:
            dicionario[tamanho] = []
        dicionario[tamanho].append(palavra)
    
    tamanho_mais_longo = max(dicionario.keys())
    palavras_mais_longas = dicionario[tamanho_mais_longo]

    print(f"A palavra mais longa tem {tamanho_mais_longo} caracteres:")
    for palavra in palavras_mais_longas:
        print(palavra)

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    nome_do_arquivo = sys.argv[1]
    palavra_longa_arquivo(nome_do_arquivo)

if __name__ == "__main__":
    main()