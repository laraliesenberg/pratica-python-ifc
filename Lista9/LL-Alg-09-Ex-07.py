import sys
import os
import re

def frequencia_de_letras(nome_do_arquivo):
    if not os.path.exists(nome_do_arquivo):
        print("Erro: esse arquivo não existe")
        return
    
    try:     
        with open(nome_do_arquivo, "r") as arquivo:
            conteudo = (arquivo.read()).lower()
            conteudo_limpo = re.sub('[^a-z]', '', conteudo)
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    contagem_de_letras = {}
    total = 0

    for caractere in conteudo_limpo:
        if caractere in contagem_de_letras:
            contagem_de_letras[caractere] = contagem_de_letras[caractere] + 1
        else:
            contagem_de_letras[caractere] = 1
        total = total + 1

    if total == 0:
        print("Não há nenhuma letra nesse arquivo")
    
    print("Frequência de letras no arquivo:")
    for letra in sorted(contagem_de_letras):
        porcentagem = (contagem_de_letras[letra] / total) * 100
        print(f"{letra}: {porcentagem:.2f}%")

def main():
    if len(sys.argv) < 2:
        print("Erro: nenhum argumento foi fornecido")
        return
    nome_do_arquivo = sys.argv[1]
    frequencia_de_letras(nome_do_arquivo)

if __name__ == "__main__":
    main()