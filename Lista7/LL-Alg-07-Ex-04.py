codigo_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 
'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
'5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def código_morse(mensagem):
    mensagem = mensagem.upper()
    traducao = ""

    for caractere in mensagem:
        if caractere in codigo_morse:
            traducao = traducao + codigo_morse[caractere] + " " 
    return traducao

def main():
    mensagem = str(input("Digite uma mensagem (traduzir para código Morse): "))
    resposta = código_morse(mensagem)
    print("Mensagem em código Morse: ", resposta)

if __name__ == "__main__":
    main()
