# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe um frase e conta o número de vogais

frase = input("Digite uma frase: ")

contadorDeVogais = 0

vogais = "aeiouAEIOU"

for letra in frase:
    if letra in vogais:
        contadorDeVogais += 1

print("A frase contem ", contadorDeVogais, " vogais")