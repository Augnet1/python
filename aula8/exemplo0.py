"""
while / Else - Aula 8
Contadores
Acumuladores
"""
contador = 1
acumulador = 1

while contador <= 10:
    print(contador, ' ', acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:
    print('Hasta la vista, baby!')

print('Acabou!')
