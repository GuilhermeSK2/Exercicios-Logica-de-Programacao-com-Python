# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita ao usuário sua idade e retorna se ele pode ou não votar.


idade = int(input("Digite sua idade: "))

if idade >= 18 and idade < 65:
    print("Voto obrigatório!")
elif idade >= 16 or idade > 65:
    print("Voto opcional!")
else: 
    print("Não pode votar!")