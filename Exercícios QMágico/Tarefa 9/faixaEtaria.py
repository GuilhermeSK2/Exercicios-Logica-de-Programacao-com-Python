# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê a idade de uma pessoa e informa a faixa etária.

idade = int(input("Digite a idade: "))
if idade >= 0 and idade <= 12:
    print("Criança.")
elif idade >= 13 and idade <= 17:
    print("Adolescente.")
elif idade >= 18 and idade <= 59:
    print("Adulto.")
else:
    print("Idoso.")
