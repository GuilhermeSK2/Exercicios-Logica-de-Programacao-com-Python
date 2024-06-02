# Curso Básico de Python
# Nome do Desenvolvedor: Guilherme Freitas dos Santos
# Versão 1.0
# Excercicio de Lógica de programação com a Linguagem de Programação Python

''' Programa que recebe 4 notas de um aluno e retorna se foi aprovado ou não tendo em mente que para ser aprovado a média deve se maior ou igual a 7, se for menor que 7, o valor da nota de exame é solcitado
e se mesmo assim não for obtida a média de 5 então o programa retorna que o aluno não foi reprovado.
'''

nota1 = float(input("Digite o valor da primeira nota: "))
nota2 = float(input("Digite o valor da segunda nota: "))
nota3 = float(input("Digite o valor da terceira nota: "))
nota4 = float(input("Digite o valor da quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("O aluno foi aprovado com a média", media)
elif media < 7:
    exame = float(input("Insira nota de exame: "))
    novaMedia = (media + exame) / 2
    if novaMedia >= 5:
        print("Aluno aprovado com média", novaMedia)
    else:
        print("O aluno foi reprovado com a média", media)