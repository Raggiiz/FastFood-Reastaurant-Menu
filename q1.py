"""
Questão 01
Autor: Raggi Izar Neto
"""


def pedidos(estoque, cardapio, lanche):
    """
    Carrinho onde você pode comprar um produto

    :param estoque: Dicionário onde armazena os dados do estoque
    :param cardapio: Dicionário que armazena os dados do cardapio
    :param lanche: Armazena a escolha do lanche do cliente
    :return: mensagem com sucesso ou fracasso da compra
    """
    if lanche in cardapio:
        print(f"Seu {lanche} está sendo preparado")
        ingrediente = cardapio[lanche]
        for ingre in range(len(ingrediente)):
            if estoque[ingrediente[-1]] >= 1:
                estoque[ingrediente[-1]] = estoque[ingrediente[-1]] - 1
                ingrediente.pop(-1)
            else:
                print(f"Infelizmente acabou o {ingrediente}")
                break
        print(f"um {lanche} saindo no capricho!!!")
        print(f"O estoque atual é: {estoque}")
    else:
        return print("Item não localizado no cardápio")


def cardapioo():
    """
    Cardápio dos produtos

    :return: none
    """
    print('x-burguer')
    print('x-salada')
    print('x-bacon')
    print('x-egg')
    print('x-tudo')
    print('')


def main():
    """
    Função principal onde contém as listas e as opções de menu

    :return: none
    """
    estoque = {'pao': 10, 'hamburguer': 12, 'tomate': 5, 'bacon': 5, 'ovo': 5}
    cardapio = {
        'x-burguer': ['pao', 'hamburguer'],
        'x-salada': ['pao', 'hamburguer', 'tomate'],
        'x-bacon': ['pao', 'hamburguer', 'tomate', 'bacon'],
        'x-egg': ['pao', 'hamburguer', 'ovo'],
        'x-tudo': ['pao', 'hamburguer', 'tomate', 'hamburguer', 'bacon', 'ovo']
    }
    while True:
        cardapioo()
        lanche = input("O que deseja pedir (0 para sair)? ")
        if lanche == 'x-burguer':
            pedidos(estoque, cardapio, lanche)
        elif lanche == 'x-salada':
            pedidos(estoque, cardapio, lanche)
        elif lanche == 'x-bacon':
            pedidos(estoque, cardapio, lanche)
        elif lanche == 'x-egg':
            pedidos(estoque, cardapio, lanche)
        elif lanche == 'x-tudo':
            pedidos(estoque, cardapio, lanche)
        elif lanche == '0':
            break


if __name__ == '__main__':
    main()
