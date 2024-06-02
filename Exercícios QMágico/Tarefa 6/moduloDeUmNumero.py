# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe um número inteiro positivo ou negativo e retorna como se fosse positivo.

numero = int(input("Digite o valor: "))

if numero > 0:
    print("O número fonecido é:", numero)
elif numero < 0:
    positivo = numero * -1
    print("O número fonecido é:", positivo)