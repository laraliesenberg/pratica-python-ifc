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
            conteudo_limpo = re.sub('[!,.?;:()""/]', '', conteudo)
            lista_de_palavras = conteudo_limpo.split()
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    contagem_de_palavras = {}
    frequencia = 0

    for palavra in lista_de_palavras:
        if palavra in contagem_de_palavras:
            contagem_de_palavras[palavra] = contagem_de_palavras[palavra] + 1
        else:
            contagem_de_palavras[palavra] = 1

        if contagem_de_palavras[palavra] > frequencia:
                frequencia = contagem_de_palavras[palavra]
    
    palavras_mais_frequentes = [palavra for palavra in contagem_de_palavras if contagem_de_palavras[palavra] == frequencia]
    
    print(f"A palavra mais frequente aparece {frequencia} vezes:")
    for palavra in palavras_mais_frequentes:
        print(palavra)

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    nome_do_arquivo = sys.argv[1]
    frequencia_de_palavras(nome_do_arquivo)

if __name__ == "__main__":
    main()