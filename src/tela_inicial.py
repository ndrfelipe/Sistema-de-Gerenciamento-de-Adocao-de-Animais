from src.cliente import *
from src.animal import *
from src.ong import *
import os

def menu_inicial():
    os.system('cls')
    print(""" 
╭━━━╮╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╭╮╱╱╱╱╱╱╱╱╱╱╭━━━╮╱╱╭╮╭╮╱╱╱╱╭━╮
┃╭━╮┃╱╱╭╮╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱┃┃╱╱╱╱╱╱╱╱╱╱┃╭━╮┃╱╭╯╰┫┃╱╱╱╱┃╭╯
┃╰━━┳━━╋╋━━╮┃╰━┳━━┳╮╭╮╭╮╭┳┳━╮╭━╯┣━━╮╭━━┳━━╮┃╰━╯┣━┻╮╭┫┃╱╱╭┳╯╰┳━━╮
╰━━╮┃┃━╋┫╭╮┃┃╭╮┃┃━┫╰╯┃┃╰╯┣┫╭╮┫╭╮┃╭╮┃┃╭╮┃╭╮┃┃╭━━┫┃━┫┃┃┃╱╭╋╋╮╭┫┃━┫
┃╰━╯┃┃━┫┃╭╮┃┃╰╯┃┃━┫┃┃┃╰╮╭┫┃┃┃┃╰╯┃╰╯┃┃╭╮┃╰╯┃┃┃╱╱┃┃━┫╰┫╰━╯┃┃┃┃┃┃━┫
╰━━━┻━━┫┣╯╰╯╰━━┻━━┻┻┻╯╱╰╯╰┻╯╰┻━━┻━━╯╰╯╰┻━━╯╰╯╱╱╰━━┻━┻━━━┻╯╰╯╰━━╯
╱╱╱╱╱╱╭╯┃
╱╱╱╱╱╱╰━╯.\n""")
    
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
                exibir_opcoes_animal()
            case 3:
                exibir_opcoes_ong()
            case 4:
                print("Saindo...")
                sleep(1)
               
                break
            case __:
                print("Opção inválida. Tente novamente")