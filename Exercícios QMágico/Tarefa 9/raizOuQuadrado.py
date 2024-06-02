# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê um número e informa se ele é positivo ou negativo. Se for positivo, calcula a raiz quadrada; se for negativo, informa o número ao quadrado.

num = float(input("Digite um número: "))

if num >= 0:
    raiz = num
    for x in range(20):
        raiz = (raiz + num / raiz) / 2
    print("A raiz quadrada do número é:", raiz)
else:
    print("O quadrado do número é:", num ** 2)