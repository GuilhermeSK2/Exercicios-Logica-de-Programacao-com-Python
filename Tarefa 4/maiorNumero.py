# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que solicita ao usuário três números e verifica qual é maior entre eles.


numero1 = int(input("Digite um número:"))

numero2 = int(input("Digite um segundo número:")) 

numero3 = int(input("Digite um terceiro número:"))

if numero1 >= numero2 and numero1 >= numero3:
    print("O primeiro número é o maior dos três")
elif numero2 >= numero1 and numero2 >= numero3:
    print("O segundo número é o maior dos três")
else:
    print("O terceiro número é o maior dos três")