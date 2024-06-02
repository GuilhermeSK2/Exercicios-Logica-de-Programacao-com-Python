# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

nome = (input("Insira o seu nome:"))
sexo = (input("insira seu sexo ('M' para Masculino e 'F' para Feminino)"))

if sexo == "M" or "m":
    print("Olá Sr.", nome, "!")
elif sexo == "F" or "f":
    print("Olá Sra.", nome,"!")
else:
    print("Sexo inválido")