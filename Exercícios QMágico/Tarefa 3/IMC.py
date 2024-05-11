# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita ao usuário sua altura e peso, e calcule seu índice de massa corporal (IMC).

altura = float(input("Digite a sua atura:"))
peso = float(input("Digite o seu peso:"))

imc = peso / altura ** 2

print("Seu IMC é de:", round(imc,2))