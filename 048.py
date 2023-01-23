# Caroline da Silva Borges
# 22 de janeiro de 2023
# Soma entre números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2): # O dois, na terceira condição é para garantir que o número seja ímpar
    if c%3==0 :
        soma += c   # Acumulador
        cont += 1   # Contador
print("A soma entre os {} valores é de {}.".format(cont, soma))
