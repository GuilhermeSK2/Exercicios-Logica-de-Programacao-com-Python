# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe a quantidade de dias, horas, minutos, segundos e calcule o total em segundos.

print("Vamos transformar tudo em segundos!")

dias = int(input("Digite a quantidade de Dias:"))
horas = int(input("Digite a quantidade de Horas:"))
minutos = int(input("Digite a quantidade de Minutos"))
segundos = int(input("Digite a quantidade de Segundos"))

totalSegundos = (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

print("O total em segundos é:", totalSegundos)