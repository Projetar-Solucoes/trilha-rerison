#Criar um protocolo no formato ANO-NÚMERO-INICIAIS e testar textos com acentos, maiúsculas e espaços extras.

#import doces - todos os doces "cadastrados".
#from doces importe - um doce especifico.
#math - ceil: arredonda um numero pra cima
#math - floor: arredonda um numero pra baixo
#math - trunc: eliminar da virgula pra frente, sem arredondar
#math - pow: potência
#math - sqrt: raises quadradas
#math - factorial: fatorial 

# import math - todas as operações acima
#from math import sqrt - Só raises quadradas 

import math 
num= int(input("digite um numero: "))
raiz = math.sqrt(num)
print(f"a raiz do numero {num} é {raiz:.2f}: ")


#// SELECIONAR UMA FUNÇÃO ESPECÍFICA DA BIBLIOTECA //
#from

#from math import factorial, ceil 
#num= int(input("digite um numero: "))
#raiz = factorial(num)
#print(f"a raiz do numero {num} é {raiz:.2f}: ")