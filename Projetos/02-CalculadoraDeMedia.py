# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicitará ao usuário 2 notas e retornará a média.

num_notas = int(input("Quantas notas deseja inserir? "))

soma = 0

for i in range(num_notas):
    nota = float(input(f"Digite a nota {i+1}: "))
    soma += nota
    media = soma / num_notas

print(f"A média das {num_notas} notas é: {media:.2f}")