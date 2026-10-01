
import funcoes


# Carrega as solicitações salvas no JSON
lista_de_solicitacoes = funcoes.carregar_dados()


while True:

    escolha = funcoes.exibir_menu()

    if escolha is None:
        continue

    elif escolha == 1:
        funcoes.cadastrar_solicitacao(lista_de_solicitacoes)

    elif escolha == 2:
        funcoes.consultar_solicitacao(lista_de_solicitacoes)

    elif escolha == 3:
        funcoes.listar_todas_solicitacoes(lista_de_solicitacoes)

    elif escolha == 4:
        funcoes.mostrar_estatisticas(lista_de_solicitacoes)

    elif escolha == 0:
        print("\nAté logo!")
        break

    else:
        print("\nOpção inválida.")

