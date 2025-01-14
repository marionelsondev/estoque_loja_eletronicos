from crud import system_actions


while True:
    print(
    """
    SISTEMA - LOJA DE ELETRÔNICOS
    -----------------------------
    [1] - Adicionar produto
    [2] - Atualizar produto
    [3] - Excluir produto
    [4] - Visualizar estoque
    [5] - Realizar venda
    [6] - Visualizar vendas
    [7] - Sair do sistema
    """
    )

    while True:
        try:
            option = int(input("Digite o número de opção: "))
            if option in [1, 2, 3, 4, 5, 6, 7]:
                break
        except ValueError:
            print("Você escolheu uma opção inválida!")

    if option == 7:
        print("Saindo do sistema...")
        break
    system_actions(option)
