# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa que apresenta os valores de conversão de graus Celsius em Fahrenheit, de 10 em 10 graus, iniciando a contagem em 10 graus Celsius e finalizando em 100 graus Celsius.

for celsius in range(10, 101, 10):
    fahrenheit = (9 * celsius + 160) / 5
    print(celsius,"graus Celsius é igual a", fahrenheit, "graus Fahrenheit")