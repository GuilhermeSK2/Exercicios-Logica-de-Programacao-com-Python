# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe 3 valores e retorna eles em ordem crescente.

A = int(input("Digite um valor para A:"))
B = int(input("Digite um valor para B:"))
C = int(input("Digite um valor para C:"))

if A > B and A > C and B > C:
    print("Os valores em ordem crescente são", C, B, A)
elif B > A and B > C and A > C:
    print("Os valores em ordem crescente são", C, A, B)
elif C > A and C > B and B > A:
    print("Os valores em ordem crescente são", A, B, C)
