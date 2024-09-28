#data de feriado 
dia = int(input("Informe o dia:"))
mes = str(input("Informe o mês:"))
if dia == 1 and mes == "janeiro":
    print("A data corresponde ao feriado de confraternização universal")
elif dia == 21 and mes == "abril":
    print("A data corresponde ao feriado de tiradentes")
elif dia == 1 and mes == "maio":
    print("A data corresponde ao feriado do dia do trabalho")
elif dia == 7 and mes == "setembro":
    print("A data corresponde ao feriado da independência do Brasil")
elif dia == 12 and mes == "outubro":
    print("A data corresponde ao feriado de Nossa Senhora Aparecida")
elif dia == 2 and mes =="novembro":
    print("A data corresponde ao feriado de finados")
elif dia == 15 and mes == "novembro":
    print("A data corresponde ao feriado da Proclamação da República")
elif dia == 25 and mes == "dezembro":
    print("A data corresponde ao feriado de Natal")
elif dia != 1 or 21 or 7 or 12 or 2 or 15 or 25 and mes != "janeiro" or "abril" or "maio" or "setembro" or "outubro" or "novembro" or "dezembro":
    print("O dia e o mês informados não correspondem a um feriado nacional.")