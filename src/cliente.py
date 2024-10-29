import json
import os
from time import sleep

arquivo = os.path.join(os.path.dirname(__file__), 'database', 'cliente.json')

def carregar_dados_clientes():
    if os.path.exists(arquivo):
        with open(arquivo, 'r') as file:
            return json.load(file)
    else:
        return []

def salvar_dados_clientes(dados):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, 'w') as file:
        json.dump(dados, file, indent=4, ensure_ascii=False)


def exibir_menu_cliente():
    os.system('cls')
    print("Sistema Cliente: \n")
    print(" 1 - Cadastrar um novo cliente")
    print(" 2 - Listar clientes")
    print(" 3 - Atualizar cliente")
    print(" 4 - Excluir cliente")
    print(" 5 - Listar um cliente")
    print(" 6 - Voltar ao menu anterior")


def cadastrar_cliente():
    clientes = carregar_dados_clientes()

    nome = input("Digite o nome do cliente: ")
    idade = input("Digite a idade do cliente: ")
    cpf = input("Digite o seu cpf: ")
    email = input("Digite seu email: ")
    telefone = input("Digite seu número de telefone: ")
    endereco = input("Digite seu endereço: ")
    renda = input("Digite sua renda familiar: ")
    profissao = input("Digite sua profissão: ")
    
    clientes.append({'nome': nome,
                     'idade': idade,
                     'cpf':cpf,
                     'email':email,
                     'telefone':telefone,
                     'endereco':endereco,
                     'renda':renda,
                     'profissao':profissao })
    
    print(f"O usuário {nome} adicionado com sucesso. ")

    salvar_dados_clientes(clientes)
    voltar_menu_principal()
    
def listar_clientes():
    os.system('cls')
    lista_clientes = carregar_dados_clientes()
    if lista_clientes:
        print(f"Lista de Clientes \n")
        print(f"{'nome'.ljust(20)} | {'idade'.ljust(5)} | {'cpf'.ljust(15)} | {'email'.ljust(25)} | {'telefone'.ljust(15)} | {'endereco'.ljust(25)} | {'renda'.ljust(10)} | {'profissao'}")
        for cliente in lista_clientes:

            try:
                print(f"{cliente.get('nome', '').ljust(20)} | {str(cliente.get('idade', '')).ljust(5)} | {str(cliente.get('cpf', '')).ljust(15)} | {cliente.get('email', '').ljust(25)} | {str(cliente.get('telefone', '')).ljust(15)} | {str(cliente.get('endereco', '')).ljust(25)} | R${str(cliente.get('renda', '')).ljust(10)} | {cliente.get('profissao', '')}")

            except Exception as e:
                print(f"Erro ao processar cliente: {e}")
                continue
    else:
        print("Nenhum usuário encontrado.")

    voltar_menu_principal()

    

def atualizar_cliente():
    clientes = carregar_dados_clientes()
    cadastro_antigo = str(input("Digite o CPF da pessoa que deseja atualizar os dados: "))
    for cliente in clientes:
        if cliente['cpf']== cadastro_antigo:
            cliente['nome'] = input("Digite o novo nome: ")
            cliente['idade'] = str(input("Digite a nova idade: "))
            cliente['cpf'] = str(input("Digite o novo CPF: "))
            cliente['email'] = input("Digite o novo email: ")
            cliente['telefone'] = input("Digite o novo telefone: ")
            cliente['endereco'] = str(input("Digite o novo endereço: "))
            cliente['renda'] = str(input("Digite a nova renda: "))
            cliente['profissao'] = input("Digite a nova profissão: ")
            
            salvar_dados_clientes(clientes)
            print("\nCliente atualizado com sucesso!")
            break
            
    else:
        print("Cliente não encontrado.")


    voltar_menu_principal()

def excluir_cliente():
    pass

def listar_um_cliente():
    pass

def voltar_menu_principal():
    input('Digite uma tecla para voltar ao menu: ')
    sleep(1)
    exibir_opcoes_cliente()

def opcao_invalida():
    
    print("Opção inválida. Tente novamente. ")
    voltar_menu_principal()


def exibir_opcoes_cliente():        
    try:
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
                sleep(1)
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
