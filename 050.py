# Caroline da Silva Borges
# 22 de janeiro de 2023
# Ler seis números inteiros e mostrar a soma apenas daqueles que forem pares. Se o valor digitado por ímpar, desconsidere-o
soma = 0
for c in range(6):
    x = int(input("Digite um número inteiro: "))
    if x%2==0 :
        soma += x
print("A soma dos valores pares é ", soma)
