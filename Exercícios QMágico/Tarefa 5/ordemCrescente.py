# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe 3 valores e retorna eles em ordem crescente.

A = int(input("Digite um valor para A: "))
B = int(input("Digite um valor para B: "))

if A == B:
    print("Valores iguais são invalidos")
elif A > B:
    print("Os valores em ordem crescente são", B, A)
else:
    print("Os valores em ordem crescente são", A, B)