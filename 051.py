# Caroline da Silva Borges
# 22 de janeiro de 2023
# Ler o primeiro termo e a razão de uma PA. No final, mostre os dez primeiros termos dessa progressão
a = int(input("Digite o primeiro termo da PA: "))
r = int(input("Qual a razão da PA: "))
an = a + (10-1)*r
for c in range(a, an + r, r):
    print(c, end=' -> ')
print("Acabou!")
   