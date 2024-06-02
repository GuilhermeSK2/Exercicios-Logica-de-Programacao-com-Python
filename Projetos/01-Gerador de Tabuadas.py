# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que gera uma tabuada do número que o usuário inserir

numero = int(input("Digite um número para gerar a tabuada: "))

print("Tabuada do", numero, ":")

for i in range(1, 11):
    resultado = numero * i
    print(numero ,"x", i ,"=", resultado)