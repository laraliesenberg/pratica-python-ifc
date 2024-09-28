import sys
import os
import re

def frequencia_de_palavras(nome_do_arquivo):

    if not os.path.exists(nome_do_arquivo):
        print("Erro: esse arquivo não existe")
        return
    
    try:     
        with open(nome_do_arquivo, "r") as arquivo:
            conteudo = (arquivo.read()).lower()
            conteudo_limpo = re.sub(r'[^a-z\s]', '', conteudo)
            lista_de_palavras = conteudo_limpo.split()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    
    contagem_de_letras = {}
    total_letras = 0

    for palavra in lista_de_palavras:
        for letra in palavra:
            if letra in contagem_de_letras:
                contagem_de_letras[letra] += 1
            else:
                contagem_de_letras[letra] = 1
            total_letras += 1

    print("\nFrequência de letras no arquivo:")
    for letra in sorted(contagem_de_letras):
        porcentagem1 = (contagem_de_letras[letra] / total_letras) * 100
        print(f"{letra}: {porcentagem1:.2f}%")


    contagem_de_palavras = {}
    total_palavras = len(lista_de_palavras)

    for palavra in lista_de_palavras:
        letras_sem_repeticao = set(palavra)
        for letra in letras_sem_repeticao:
            if letra in contagem_de_palavras:
                contagem_de_palavras[letra] += 1
            else:
                contagem_de_palavras[letra] = 1
            

    print("\nQuantidade de palavras que contêm cada letra:")
    for letra in sorted(contagem_de_palavras):
        porcentagem2 = (contagem_de_palavras[letra] / total_palavras) * 100
        print(f"{letra}: {porcentagem2:.2f}%")

    print("\nLetra com menor quantidade de palavras:")
    letra_com_menor_frequencia = min(contagem_de_palavras, key=contagem_de_palavras.get)
    print(f"{letra_com_menor_frequencia}: {contagem_de_palavras[letra_com_menor_frequencia]}")

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    nome_do_arquivo = sys.argv[1]
    frequencia_de_palavras(nome_do_arquivo)

if __name__ == "__main__":
    main()