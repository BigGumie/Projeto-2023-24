import random #serve para gerar os 4 digitos na criação da zona
import os # De momento so uso para limpar o terminal
from colorama import init, Fore, Style #Cores e estilos
import pandas as pd #Para utilizamento de tabelas
import time #Para dar tempo entre as funçoes
import csv #Para criar ficheiros em EXEL

init(autoreset=True) #Loop que ja vem com a biblioteca 
os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal

#----------------------------------------------------------------Criar Zona--------------------------------------------------------------#
class Zona:
    def __init__(self, nome, latitude, longitude, descricao):
        self.codigo = self.gerar_codigo() 
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.descricao = descricao

    def gerar_codigo(self):
        # Gera um código aleatório de quatro letras em maiúsculas
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))  #Nao ligues ao 65 e 90 é uma cena qualquer para o ASCII entender de A a Z
        return codigo

def salvar_zona_em_arquivo(zona):

    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.csv')

    #O mode='a' supostamente é "read"??
    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL) #Tbh nao sei bem para oq isto serve mas no tuturial tinha por isso...
        writer.writerow([zona.codigo, zona.nome, zona.latitude, zona.longitude, zona.descricao]) #Isto escreve no exel tho

def criar_zona():
    print("Criar Nova Zona:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    descricao = input("Descrição: ")

    nova_zona = Zona(nome, latitude, longitude, descricao)

    print("\nInformações da Nova Zona:")
    print("Código:", nova_zona.codigo)
    print("Nome:", nova_zona.nome)
    print("Latitude:", nova_zona.latitude)
    print("Longitude:", nova_zona.longitude)
    print("Descrição:", nova_zona.descricao)

    salvar = input("\nDeseja salvar a nova zona? (s/n): ").lower()
    
    if salvar == 's':
        salvar_zona_em_arquivo(nova_zona)
        print("Zona salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. A zona não foi salva.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
        
#----------------------------------------------------------------Criar Diversao--------------------------------------------------------------#
class Diversao:
    def __init__(self, codigo, nome, latitude, longitude, tipo, zona_associada, idade_minima, altura_minima, intensidade, estado_atual, duracao, descricao):
        self.codigo = codigo
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.tipo = tipo
        self.zona_associada = zona_associada
        self.idade_minima = idade_minima
        self.altura_minima = altura_minima
        self.intensidade = intensidade
        self.estado_atual = estado_atual
        self.duracao = duracao
        self.descricao = descricao

def gerar_codigo():
    return ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))


def criar_diversao():
    print("Criar Nova Diversão:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    tipo = input("Tipo: ")
    zona_associada = input("Zona Associada: ")
    idade_minima = int(input("Idade Mínima: "))
    altura_minima = float(input("Altura Mínima: "))
    intensidade = input("Intensidade: ")
    estado_atual = input("Estado Atual (Aberto/Fechado): ")
    duracao = input("Duração: ")
    descricao = input("Descrição: ")

    nova_diversao = Diversao(
        codigo=gerar_codigo(),
        nome=nome,
        latitude=latitude,
        longitude=longitude,
        tipo=tipo,
        zona_associada=zona_associada,
        idade_minima=idade_minima,
        altura_minima=altura_minima,
        intensidade=intensidade,
        estado_atual=estado_atual,
        duracao=duracao,
        descricao=descricao
    )
    
    print("\nInformações da Nova Diversão:")
    print("Código:", nova_diversao.codigo)
    print("Nome:", nova_diversao.nome)
    print("Latitude:", nova_diversao.latitude)
    print("Longitude:", nova_diversao.longitude)
    print("Tipo:", nova_diversao.tipo)
    print("Zona Associada:", nova_diversao.zona_associada)
    print("Idade Mínima:", nova_diversao.idade_minima)
    print("Altura Mínima:", nova_diversao.altura_minima)
    print("Intensidade:", nova_diversao.intensidade)
    print("Estado Atual:", nova_diversao.estado_atual)
    print("Duração:", nova_diversao.duracao)
    print("Descrição:", nova_diversao.descricao)

    salvar = input("\nDeseja salvar a nova diversão? (s/n): ").lower()
    
    if salvar == 's':
        salvar_diversao_em_arquivo(nova_diversao)
        print("Diversão salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. A diversão não foi salva.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

def salvar_diversao_em_arquivo(diversao):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'diversoes.csv')

    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            diversao.codigo, diversao.nome, diversao.latitude, diversao.longitude,
            diversao.tipo, diversao.zona_associada, diversao.idade_minima,
            diversao.altura_minima, diversao.intensidade, diversao.estado_atual,
            diversao.duracao, diversao.descricao
        ])

#----------------------------------------------------------------Menu de Comodidade--------------------------------------------------------------#

class Comodidade:
    def __init__(self, codigo, nome, latitude, longitude, zona_associada, estado_atual, descricao):
        self.codigo = codigo
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.zona_associada = zona_associada
        self.estado_atual = estado_atual
        self.descricao = descricao

    def gerar_codigo(self):
        # Gera um código aleatório de quatro letras em maiúsculas
        return ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))

def criar_comodidade():
    print("Criar Nova Comodidade:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    zona_associada = input("Zona Associada: ")
    estado_atual = input("Estado Atual (Aberta/Fechada): ")
    descricao = input("Descrição: ")

    nova_comodidade = Comodidade(
        codigo=gerar_codigo(), 
        nome=nome,
        latitude=latitude,
        longitude=longitude,
        zona_associada=zona_associada,
        estado_atual=estado_atual,
        descricao=descricao
    )

    print("\nInformações da Nova Comodidade:")
    print("Código:", nova_comodidade.codigo)
    print("Nome:", nova_comodidade.nome)
    print("Latitude:", nova_comodidade.latitude)
    print("Longitude:", nova_comodidade.longitude)
    print("Zona Associada:", nova_comodidade.zona_associada)
    print("Estado Atual:", nova_comodidade.estado_atual)
    print("Descrição:", nova_comodidade.descricao)

    salvar = input("\nDeseja salvar a nova comodidade? (s/n): ").lower()
    
    if salvar == 's':
        salvar_comodidade_em_arquivo(nova_comodidade)
        print("Comodidade salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. A comodidade não foi salva.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

def salvar_comodidade_em_arquivo(comodidade):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'comodidades.csv')

    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            comodidade.codigo, comodidade.nome, comodidade.latitude, comodidade.longitude,
            comodidade.zona_associada, comodidade.estado_atual, comodidade.descricao
        ])

#----------------------------------------------------------------Menu de Paragem de Comboio--------------------------------------------------------------#

class ParagemComboio:
    def __init__(self, codigo, nome, zona_associada, latitude, longitude, descricao):
        self.codigo = codigo
        self.nome = nome
        self.zona_associada = zona_associada
        self.latitude = latitude
        self.longitude = longitude
        self.descricao = descricao

    def gerar_codigo(self):
        # Gera um código aleatório de quatro letras em maiúsculas
        return ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))

def criar_paragem_comboio():
    print("Criar Nova Paragem de Comboio:")
    nome = input("Nome: ")
    zona_associada = input("Zona Associada: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    descricao = input("Descrição: ")

    nova_paragem_comboio = ParagemComboio(
        codigo=gerar_codigo(),
        nome=nome,
        zona_associada=zona_associada,
        latitude=latitude,
        longitude=longitude,
        descricao=descricao
    )

    print("\nInformações da Nova Paragem de Comboio:")
    print("Código:", nova_paragem_comboio.codigo)
    print("Nome:", nova_paragem_comboio.nome)
    print("Zona Associada:", nova_paragem_comboio.zona_associada)
    print("Latitude:", nova_paragem_comboio.latitude)
    print("Longitude:", nova_paragem_comboio.longitude)
    print("Descrição:", nova_paragem_comboio.descricao)

    salvar = input("\nDeseja salvar a nova paragem de comboio? (s/n): ").lower()
    
    if salvar == 's':
        salvar_paragem_comboio_em_arquivo(nova_paragem_comboio)
        print("Paragem de Comboio salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. A paragem de comboio não foi salva.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

def salvar_paragem_comboio_em_arquivo(paragem_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'paragens_comboio.csv')

    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            paragem_comboio.codigo, paragem_comboio.nome, paragem_comboio.zona_associada,
            paragem_comboio.latitude, paragem_comboio.longitude, paragem_comboio.descricao
        ])

#----------------------------------------------------------------Menu de Criação--------------------------------------------------------------#
def criar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 55 + "|    Criar    |" + "-" * 55 + "+")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 33 + "| 8. Procurar |" + " " * 33 + "| 9. Voltar |" + " " * 32 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 15 + "| 1. Criar uma Zona |" + " " * 16 + "| 2. Criar uma Diversão |" + " " * 12 + "| 3. Criar uma comodidade |" + " " * 9 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 5 + "| 4. Criar uma paragem de comboio |" + " " * 5 + "| 6. Criar uma ligação de 2 paragens |" + " " * 5 + "| 7. Criar trajecto de comboio |" + " " * 5 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")

    while True:
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 +"↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )
        if escolha == '1':
            criar_zona()
        elif escolha == '2':
            criar_diversao()
        elif escolha == '3':
            criar_comodidade() 
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")

Opcao_criar = ("criar", "1")

#----------------------------------------------------------------Menu Principal--------------------------------------------------------------#
def menu_admin():
     while True:
        print_menu()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 +"↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha.lower() in Opcao_criar:
            print("lol")
            criar()
        elif escolha == 'alterar':
            print("Alterar")
        elif escolha == 'bilhetes':
            print("Bilhetes")
        elif escolha == 'Alterar':
            print("Alterar")
        elif escolha == '3':
            print(Fore.RED + "Encerrando...")
            break
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")

def print_menu():
    
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 51 + "|    Administração    |" + "-" * 51 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 1 .Criar |" + " " * 7 + "| 2. Alterar |" + " " * 7 + "| 3. Bilhetes |" + " " * 7 + "| 4. Procurar |" + " " * 7 + "| 5. Log out |" + " " * 7 + "| 0. Encerrar |" + " " * 2 +"|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "  ___       __   _______   ___       ________  ________  _____ ______    _______        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + " |\  \     |\  \|\  ___ \ |\  \     |\   ____\|\   __  \|\   _ \  _   \|\  ___ \        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + " \ \  \    \ \  \ \   __/|\ \  \    \ \  \___|\ \  \|\  \ \  \\\__\ \  \ \   __/|       " + " " * 16 +"|")       
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "  \ \  \  __\ \  \ \  \_|/_\ \  \    \ \  \    \ \  \\\  \ \  \\|__| \  \ \  \_|/__     " + " " * 17 +"|")      
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "   \ \  \|\__\_\  \ \  \_|\ \ \  \____\ \  \____\ \  \\\  \ \  \    \ \  \ \  \_|\ \    " + " " * 16 +"|")     
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "    \ \____________\ \_______\ \_______\ \_______\ \_______\ \__\    \ \__\ \_______\   " + " " * 15 +"|")    
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "     \|____________|\|_______|\|_______|\|_______|\|_______|\|__|     \|__|\|_______|   " + " " * 15 +"|")    
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")    
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")     
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")  
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")


if __name__ == "__main__":
    menu_admin()
