from estoque_mp import entrada_mp, saida_mp, listar_estoque_mp
from estoque_pa import entrada_pa, saida_pa, listar_estoque_pa, top_produtos_por_quantidade


def menu_materia_prima():
    while True:
        print("\n=== [MP] Matéria-Prima ===")
        print("1. Registrar ENTRADA")
        print("2. Registrar SAÍDA")
        print("3. Listar ESTOQUE")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cod = input("Código: ")
            nome = input("Nome: ")
            qtd = int(input("Quantidade: "))
            embalagem = input("Embalagem: ")
            empresa = input("Empresa: ")
            entrada_mp(cod, nome, qtd, embalagem, empresa)

        elif opcao == "2":
            cod = input("Código: ")
            qtd = int(input("Quantidade de saída: "))
            saida_mp(cod, qtd)

        elif opcao == "3":
            listar_estoque_mp()

        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_produto_acabado():
    while True:
        print("\n=== [PA] Produto Acabado ===")
        print("1. Registrar ENTRADA (produção)")
        print("2. Registrar SAÍDA (pedido)")
        print("3. Listar ESTOQUE")
        print("0. Voltar")

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
            break
        else:
            print("Opção inválida.")


def menu_relatorios():
    while True:
        print("\n=== [RELATÓRIOS] ===")
        print("1. Top produtos acabados por quantidade")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            n = input("Quantos produtos mostrar? (padrão 5): ").strip()
            top_n = int(n) if n.isdigit() else 5
            top_produtos_por_quantidade(top_n)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")


def menu_principal():
    while True:
        print("\n=== CONTROLE DE ESTOQUE (Terminal) ===")
        print("1. Matéria-Prima")
        print("2. Produto Acabado")
        print("3. Relatórios")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_materia_prima()
        elif opcao == "2":
            menu_produto_acabado()
        elif opcao == "3":
            menu_relatorios()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu_principal()
