'''Crie um arquivo chamado:

text
utilidades.py


Dentro dele, crie três funções:

python
def dobro(numero):
    ...

def triplo(numero):
    ...

def maior(numero1, numero2):
    ...


Depois, crie outro arquivo chamado:

text
main.py


Importe as funções do módulo utilidades e utilize-as.

O programa deverá apresentar:

text
Dobro de 5: 10
Triplo de 5: 15
Maior entre 8 e 12: 12


Coloque as funções dentro de calculos.py e faça a importação no main.py.'''
import Pacotes.utilidades

numero1 = int(input("digite um numero: "))
numero2 = int(input("digite um numero: "))

print(f"O dobro de {numero1} é: {Pacotes.utilidades.dobro(numero1)}")
print(f"O triplo de {numero1} é: {Pacotes.utilidades.triplo(numero1)}")
print(f"O maior entre {numero1} e {numero2} é: {Pacotes.utilidades.maior(numero1, numero2)}")