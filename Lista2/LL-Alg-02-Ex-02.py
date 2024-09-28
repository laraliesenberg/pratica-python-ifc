#unidade de tempo 2
segundos = int(input("Digite o número de segundos que deseja reverter:"))
dias = segundos//86400
restantes = segundos%86400
horas = restantes//3600
segundos_restantes = restantes%3600
minutos = segundos_restantes//60
segundos_restantes_final = segundos_restantes%60
print("Dias:", dias, "horas:", horas, "minutos:", minutos, "segundos:", segundos_restantes_final)