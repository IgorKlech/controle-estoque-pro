from estoque_mp import entrada_mp, saida_mp, listar_estoque_mp

def menu():
    while True:
        print("\n=== Controle de Estoque - Matéria-Prima ===")
        print("1. Registrar ENTRADA")
        print("2. Registrar SAÍDA")
        print("3. Listar ESTOQUE")
        print("0. Sair")

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
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()