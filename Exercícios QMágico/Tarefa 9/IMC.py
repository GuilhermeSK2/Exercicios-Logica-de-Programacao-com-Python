# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que lê o peso e a altura de uma pessoa, calcula o IMC e informa a categoria.

peso = float(input("Digite o seu peso (kg): "))
altura = float(input("Digite a sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    categoria = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    categoria = "Peso normal"
elif 25 <= imc < 29.9:
    categoria = "Sobrepeso"
elif 30 <= imc < 34.9:
    categoria = "Obesidade grau I"
elif 35 <= imc < 39.9:
    categoria = "Obesidade grau II"
else:
    categoria = "Obesidade grau III"

print("O IMC é:", round(imc,2), "Categoria:", categoria)
