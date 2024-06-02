# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita ao usuário sua idade e retorna se ele é ou não é maior de idade.


idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Você é menor de idade!")
elif idade >= 18:
    print("Você é maior de idade!")