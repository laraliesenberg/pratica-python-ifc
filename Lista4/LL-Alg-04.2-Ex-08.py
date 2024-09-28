mensagem = str(input("Digite a mensagem que você deseja criptografar: "))
distancia = int(input("Digite a distância de deslocamento das letras: "))
mensagem = str(mensagem.replace(" ", ""))
mensagem = str(mensagem.lower())

mensagem_criptografada = ""
for i in mensagem:
   troca = ord(i) + distancia
   if troca > 122:
      troca = ord(i) - 26 + distancia
   mensagem_criptografada = mensagem_criptografada + chr(troca)
print(mensagem_criptografada)