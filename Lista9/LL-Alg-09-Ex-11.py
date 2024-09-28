import sys
import os
import string

def carregar_palavras_conhecidas(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            palavras = set(file.read().split())
        return palavras
    
    except FileNotFoundError:
        print(f"Erro: o arquivo '{filename}' com as palavras conhecidas não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo de palavras conhecidas: {e}")
        sys.exit(1)


def corretor_ortografico(nome_do_arquivo, palavras_conhecidas):
    if not os.path.exists(nome_do_arquivo):
        print("Erro: esse arquivo não existe")
        return
    
    try:
        with open(nome_do_arquivo, "r", encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            conteudo_limpo = conteudo.translate(str.maketrans("", "", string.punctuation))
            lista_de_palavras = conteudo_limpo.split()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    palavras_incorretas = set()

    for palavra in lista_de_palavras:
        if palavra not in palavras_conhecidas:
            palavras_incorretas.add(palavra)
            
    if palavras_incorretas:
        print("Palavras com erros ortográficos:")
        for palavra in palavras_incorretas:
            print(palavra)
    else:
        print("Não há nenhum erro ortográfico")

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    
    nome_do_arquivo = sys.argv[1]
    palavras_conhecidas = carregar_palavras_conhecidas("exemplo2.txt")

    corretor_ortografico(nome_do_arquivo, palavras_conhecidas)

if __name__ == "__main__":
    main()