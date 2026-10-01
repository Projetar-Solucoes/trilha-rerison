#// CONDIÇÕES ANINHADAS //

#IF - SE
#ELIF - SENÃO-SE
#ELSE - SENÃO


from time import sleep
print("Para começar o imprestimo deverá inserir os dados pedidos pelo sistema a seguir.")
sleep (5)
Nome_completo= str(input("Qual seu nome completo ? "))
sleep (2)
idade= int(input(f"Olá, {Nome_completo} Qual a sua idade ? "))
sleep (2)
cfp= int(input(f"Por favor {Nome_completo} me informe seu CPF ? "))
sleep (2)
renda= int(input(f"{Nome_completo} qual sua renda (MENSAL) ? "))
sleep (2)
valor_emprestimo= int(input(f"E por último {Nome_completo} qual o valor do emprestimo desejado ? "))


print("RECOLHENDO DADOS..")
sleep (5)

if idade <18:
    print("Infelizmente pessoas com idade menor de 18 anos não é permitido fazer emprestimo.")

else:
    if renda < 1500:
        print(f"Emprestimo bloqueado, {Nome_completo} infelizmente você não tem renda suficiente. ")

    elif renda >1500 and renda <5.000:
        print(f" {Nome_completo} estamos analisando o valor do emprestimo que você tem interresse.  ")
        print("Aguarde alguns instantes.")
        sleep (5)

    elif valor_emprestimo >=1000 and valor_emprestimo <=9999:
        print(f"Emprestimo aprovado {Nome_completo}, use-o com conciencia")

    elif valor_emprestimo >=10000 and valor_emprestimo <50000:
        print(f"{Nome_completo} você precisará por o processo de RH - revisão humana.")

    elif valor_emprestimo >50001:
        print("O emprestimo não foi aprovado, pois o limite do nosso banco é 50.000R$ ")
        
    else:
        print("EMPRESTIMO BLOQUEADO")