# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que converte temperaturas de graus Celsius para Fahrenheit de 10 em 10 graus, exibindo os valores das duas escalas.

celsius = 10

while celsius <= 100:
    fahrenheit = (9 * celsius + 160) / 5
    print("Celsius:", celsius, " | Fahrenheit:", round(fahrenheit, 2))
    celsius += 10