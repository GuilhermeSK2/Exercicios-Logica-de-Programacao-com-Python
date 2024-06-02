# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa apresenta os resultados de uma tabuada de multiplicar (de 1 até 10) de um número qualquer.

numero = int(input("Digite um número para ver a tabuada: "))
for i in range(1, 11):
    resultado = numero * i
    print(numero,"x", i , "=" , resultado)

# C)

soma = 0
for i in range(1, 101):
    soma += i
print("A soma dos cem primeiros números inteiros é",soma)


# D)

soma_pares = 0
for i in range(1, 501):
    if i % 2 == 0:
        soma_pares += i
print("A soma dos valores pares de 1 até 500 é", soma_pares)
