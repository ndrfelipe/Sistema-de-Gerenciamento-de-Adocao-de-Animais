from src.cliente import *
from src.animal import *

def menu_inicial():
    print(" Seja bem vindo ao sistema de crud.\n")
    
    print(" 1 - Sistema Cliente ")
    print(" 2 - Sistema Animal ")
    print(" 3 - Sistema ONG ")
    print(" 4 - Sair ")
        

def tela_usuario():
    while True:
        menu_inicial()
        opcao_inicial = int(input("Digite uma opção: "))

        match(opcao_inicial):
            case 1:
                # aqui vai ser chamada a funçao do crud cliente
                exibir_opcoes_cliente()
            case 2:
                # aqui vai ser chamada a funçao do crud adoc
                exibir_menu_animal()
                print("CRUD Animais")
            case 3:
                # aqui vai ser chamada a funçao do crud animais
                pass
            case 4:
                print("Saindo...")
                break
            case __:
                print("Opção inválida. Tente novamente")