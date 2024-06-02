# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

# Programa para converter temperatura de celsius para fahrenheit e vice versa

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcoes = ["Celsius para Fahrenheit", "Fahrenheit para Celsius"]
print("Escolha uma opção:")

for i, opcao in enumerate(opcoes, start=1):
    print(f"{i}. {opcao}")

escolha = int(input("Digite o número correspondente à opção desejada: "))

if escolha == 1:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius}°C = {fahrenheit:.1f}°F")

elif escolha == 2:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit}°F = {celsius:.1f}°C")
else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
