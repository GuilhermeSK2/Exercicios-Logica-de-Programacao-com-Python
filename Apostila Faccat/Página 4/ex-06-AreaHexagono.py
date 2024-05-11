# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Algoritmo  para  ler  as  dimensões  de  um  hexagono  (lado),  calcular  e  escrever  a área do hexagono.
import math

print("Vamos calcular a área de um hexagono!")
lado = float(input("Digite o cumprimento de um dos lados do hexagono:"))

area = ((3 * pow (lado,2) * math.sqrt(3)) / 2)

print("A área do hexagono é", round(area,2), " m²")
