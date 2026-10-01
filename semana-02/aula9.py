#fatiamento formas
#frase: Curso em Video Python
#frase[9:14] - não conta o ultimo número, só ate o anterior ! nesse caso até 0 13
#frase[9:21:2] - Pulando de 2 em 2
#frase[:5] - Vai do inicio até o anterior do numero escolhido, neses caso ate o "4"
#frase[15:] - Vai do numero escolhido ate o final, nesse caso iria do 15 ate o fim da frase
#frase[9::3] - Começará do caractere 9 até o final, cortando de 3 em 3
#caracteres começão a serem contados do "0"

#// ANÁLISE //
#len(frase) - len = qual o tamanho (frase)

#.count
#frase.count('o') = quantas vezes tem a letra "o"
#frase.count('o,0,13') = quantas vezes tem a letra "o" de 0 até o 13

#.find
#frase.find('deo') = quantas vezes ele encontrou DEO, começou na posição...
#frase.find('android') = -1, mesma coisa do que não existe. 

#'curso' in frase = True
#'java' in frase = False


#//TRANSFORMAÇÃO//

#frase,replace('python','android') - Trocar o nome python por Andoid
#frase.upper() = Pra cima, tudo que for minusculo trocar por maisculo
#frase.lower() = Pra baixo, tudo que for maiusculo trocar por minusculo
#frase.capitalize() = tudo minusculo, e a primeira letra maiuscula
#frase.title() = Inicial de cada palavra maiuscula

#frase.strip() = remover todos os espaços inuteis, no inicio e no fim da string.
#frase.rstrip() = da foco ao lado direito: no caso do fim da frase os espaços seram removidos.
#frase.lstrip() = da foco ao lado esquerdo: no caso do inicio da frase os espaços seram removidos.

#// DIVISÃO DE STRING //

#frase.split() - onde estiver espaço ele vai dividir 

#// JUNÇÃO //

#'-'.join(frase)- Juntar a frase e separar palavras por esse traço

import datetime
ano = datetime.datetime.now().year
nome = input('Qual o seu nome ? ').upper().split()
num_inscricao= int(input('Qual o numero da sua inscrição ? '))
iniciais = "".join([e[0] for e in nome])
print(f"Protocolo {ano}-{num_inscricao}-{iniciais}")

