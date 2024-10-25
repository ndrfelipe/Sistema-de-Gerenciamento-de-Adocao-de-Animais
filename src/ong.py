lista_de_clientes = []

def exibir_menu_ong():
    print('''
    
▒█▀▀▀█ ░▀░ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀█ 　 █▀▀▄ █▀▀ 　 ▒█▀▀▀█ █▀▀▄ █▀▀▀ 
░▀▀▀▄▄ ▀█▀ ▀▀█ ░░█░░ █▀▀ █░▀░█ █▄▄█ 　 █░░█ █▀▀ 　 ▒█░░▒█ █░░█ █░▀█ 
▒█▄▄▄█ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀░░▀ 　 ▀▀▀░ ▀▀▀ 　 ▒█▄▄▄█ ▀░░▀ ▀▀▀▀
    ''')
    print('''
      |  [1] Cadastro de ONG's parceiras |
      |  [2] Cadastro de voluntários     |
      |  [3] Registro de adoções         |
      |  [4] Voltar ao menu principal    |
    ''')


def cadastrar_ong():
    pergunta = 's'
    while pergunta != "N":   
        nome = input("Digite o nome do cliente: ")
        idade = int(input("Digite a idade do cliente: "))
        pergunta = input("Deseja cadastrar mais um usuário (S / N) ? ")
        lista_de_clientes.append({'nome': nome, 'idade': idade})
        print("Usuário adicionado com sucesso. ")
    return 
    
def cadastrar_voluntario():
    for cliente in lista_de_clientes:
        print(f"Nome do cliente: {cliente['nome']} | Idade: {cliente['idade']}")

def registrar_adocao():
    pass

#essa função será colocada no arquivo tela_inicial, na opcao cadastro de cliente.
def exibir_opcoes_ong():
    while True:
        exibir_menu_ong()
        opcao_ong = int(input("Informe uma opção: "))
    
        match(opcao_ong):
            case 1:
                cadastrar_ong()
            case 2:
                cadastrar_voluntario()
            case 3:
                registrar_adocao()
            case 4:
                print("Voltando ao menu inicial")
                break
            case _:
                print("Opção inválida. Tente novamente")
                



    
   # █▀▀ ░▀░ █▀▀ ▀▀█▀▀ █▀▀ █▀▄▀█ █▀▀█ 　 █▀▀█ █▀▀▄ █▀▀▀ 
    #▀▀█ ▀█▀ ▀▀█ ░░█░░ █▀▀ █░▀░█ █▄▄█ 　 █░░█ █░░█ █░▀█ 
   # ▀▀▀ ▀▀▀ ▀▀▀ ░░▀░░ ▀▀▀ ▀░░░▀ ▀░░▀ 　 ▀▀▀▀ ▀░░▀ ▀▀▀▀ 