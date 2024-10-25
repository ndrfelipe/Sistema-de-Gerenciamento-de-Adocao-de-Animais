lista_de_clientes = []

def exibir_menu_cliente():
    print("Sistema Cliente: ")
    print(" 1 - Cadastrar um novo cliente")
    print(" 2 - Listar clientes")
    print(" 3 - Atualizar cliente")
    print(" 4 - Excluir cliente")
    print(" 5 - Listar um cliente")
    print(" 6 - Voltar ao menu anterior")


def cadastrar_cliente():
    pergunta = 's'
    while pergunta != "N":   
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        pergunta = input("Deseja cadastrar mais um usuário (S / N) ? ")
        lista_de_clientes.append({'nome': nome, 'idade': idade})
        print("Usuário adicionado com sucesso. ")
    return 
    
def listar_clientes():
    for cliente in lista_de_clientes:
        print(f"Nome do cliente: {cliente['nome']} | Idade: {cliente['idade']}")

def atualizar_cliente():
    pass

def excluir_cliente():
    pass

def listar_um_cliente():
    pass

def exibir_opcoes_cliente():
    while True:
        exibir_menu_cliente()
        opcao_cliente = int(input("Informe uma opção: "))
    
        match(opcao_cliente):
            case 1:
                cadastrar_cliente()
            case 2:
                listar_clientes()
            case 3:
                atualizar_cliente()
            case 4:
                excluir_cliente()
            case 5:
                listar_um_cliente()
            case 6:
                print("Voltando ao menu inicial... ")
                break
            case _:
                print("Opção inválida. Tente novamente")
                
