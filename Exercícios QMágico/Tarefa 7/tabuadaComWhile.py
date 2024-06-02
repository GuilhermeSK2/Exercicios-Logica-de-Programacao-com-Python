# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que gera a tabuada de multiplicação de um número fornecido pelo usuário, exibindo os resultados de 1 até 10.

numero = int(input("Digite um número para ver sua tabuada: "))
contador = 1

while contador <= 10:
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)
    contador += 1
