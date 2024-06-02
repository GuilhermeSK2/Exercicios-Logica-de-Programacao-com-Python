# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita ao usuário dois números e verifica qual é maior entre eles.

numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite um segundo número:")) 

if numero1 == numero2:
    print("Os números são iguais")
elif numero1 >= numero2:
    print("O primeiro número é o maior entre os dois")
else:
    print("O segundo número é o maior entre os dois")