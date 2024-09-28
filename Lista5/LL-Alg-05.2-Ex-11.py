import random
def senha_aleatória():
    i = 0
    senha_oficial = ""
    while i < 10:
        sorteio = random.randint(33, 126)
        senha_aleatoria = chr(sorteio)
        senha_oficial = senha_oficial + senha_aleatoria
        i = i + 1
    return senha_oficial

def main():
    senha = senha_aleatória()
    print(senha)
if __name__ == "__main__":
    main()