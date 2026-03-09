from estoque_pa import entrada_pa, saida_pa, listar_estoque_pa


def menu_pa():
    while True:
        print("\n=== Controle de Estoque - Produto Acabado ===")
        print("1. Registrar ENTRADA (produção)")
        print("2. Registrar SAÍDA (pedido)")
        print("3. Listar ESTOQUE")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade produzida: "))
            peso = float(input("Peso total (kg): "))
            embalagem = input("Embalagem: ")
            of = input("Ordem de Fabricação (OF): ")
            entrada_pa(nome, qtd, peso, embalagem, of)

        elif opcao == "2":
            nome = input("Nome do produto: ")
            qtd = int(input("Quantidade de saída: "))
            peso = float(input("Peso total (kg): "))
            pedido = input("Número do Pedido: ")
            saida_pa(nome, qtd, peso, pedido)

        elif opcao == "3":
            listar_estoque_pa()

        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_pa()

