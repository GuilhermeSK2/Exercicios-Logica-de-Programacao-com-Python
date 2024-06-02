# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que recebe o número de total de eleitores, votos nulos, votos brancos e votos válidos para calcular percentuais de votos em um município.

total_eleitores = int(input("Digite o número total de eleitores do município: "))

votos_brancos = int(input("Digite o número de votos brancos: "))
votos_nulos = int(input("Digite o número de votos nulos: "))
votos_validos = int(input("Digite o número de votos válidos: "))

percentual_brancos = (votos_brancos / total_eleitores) * 100
percentual_nulos = (votos_nulos / total_eleitores) * 100
percentual_validos = (votos_validos / total_eleitores) * 100

print("Percentual de votos brancos:", round(percentual_brancos,2),"%")
print("Percentual de votos nulos:", round(percentual_nulos,2),"%")
print("Percentual de votos válidos:", round(percentual_validos,2),"%")
