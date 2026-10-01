'''RSOR DE NÚMEROS

Crie um programa que peça ao usuário dois números e realize uma divisão.

Exemplo:

Digite o primeiro número: 10
Digite o segundo número: 2

Resultado: 5.0

Porém, o programa precisa tratar situações em que o usuário digite algo inválido.

Utilize try e except para tratar:

1. Entrada que não seja número

Exemplo:

Digite o primeiro número: abc

O programa deverá informar:

Erro: digite apenas números.
2. Divisão por zero
Exemplo:

Digite o primeiro número: 10
Digite o segundo número: 0

O programa deverá informar:

Erro: não é possível dividir por zero.'''
def ler_numeros():
    while True:
        try:
            numero1 = int(input("Digite o primeiro número: "))
            numero2 = int(input("Digite o segundo número: "))
            calculo = numero1 / numero2
        except (ValueError, TypeError):
            print("Tivemos um erro, os tipos de dados relacionados não são compativeis com o sistema (digite apenas números). Tente novamente. \n")
        except (ZeroDivisionError):
            print("Tivemos um erro, não é possivel dividir por 0 \n")
        else:
            print(f"\nNúmeros aceitos com sucesso: {numero1} e {numero2}")
            print(f"\nO {numero1} divido por {numero2} é {calculo}")
            return numero1, numero2, calculo

numero1, numero2, calculo = ler_numeros()


