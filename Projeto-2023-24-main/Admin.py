import random #serve para gerar os 4 digitos na criação da zona
import os # De momento so uso para limpar o terminal
from colorama import init, Fore, Style #Cores e estilos
import pandas as pd #Para utilizamento de tabelas
import time #Para dar tempo entre as funçoes
import csv #Para criar ficheiros em EXEL
import menu #Chama o menu.py
import keyboard


init(autoreset=True) #Loop que ja vem com a biblioteca 
os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal


#----------------------------------------------------------------Ler Ficherio csv--------------------------------------------------------------#
# Lista de codificações possíveis
codificacoes = ['utf-8', 'latin1', 'cp1252']

# Função para ler o arquivo zonas.csv
def ler_arquivo(arquivo, codificacoes):
    codigos_zona = []
    try:
        df = pd.read_csv(arquivo, encoding='utf-8', header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Descrição'])
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT +'Aqui estão as zonas disponíveis.')
        print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Descrição']].to_string(index=False))
        codigos_zona = df['Código'].tolist()
    except FileNotFoundError:
        print("Arquivo de zonas não encontrado.")
    except UnicodeDecodeError:
        print("")
        for cod in codificacoes:
            try:
                df = pd.read_csv(arquivo, encoding=cod, header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Descrição'])
                print(Fore.BLUE + Style.BRIGHT +'Aqui estão as zonas disponíveis.')
                print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Descrição']].to_string(index=False))
                codigos_zona = df['Código'].tolist()
                break
            except UnicodeDecodeError:
                pass
    return codigos_zona


# Função para ler o arquivo comodidades.csv
def ler_comodidades(arquivo, codificacoes):
    try:
        df = pd.read_csv(arquivo, encoding='utf-8', header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Zona Associada', 'Estado Atual', 'Descrição'])
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT +'Aqui estão as comodidades disponíveis.')
        print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Zona Associada', 'Estado Atual', 'Descrição']].to_string(index=False))
    except FileNotFoundError:
        print("Arquivo de comodidades não encontrado.")
    except UnicodeDecodeError:
        print("")
        for cod in codificacoes:
            try:
                df = pd.read_csv(arquivo, encoding=cod, header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Zona Associada', 'Estado Atual', 'Descrição'])
                print(f'Aqui estão as comodidades disponíveis:')
                print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Zona Associada', 'Estado Atual', 'Descrição']].to_string(index=False))
                break
            except UnicodeDecodeError:
                pass

# Função para ler o arquivo diversoes.csv            
def ler_diversoes(arquivo, codificacoes):
    try:
        df = pd.read_csv(arquivo, encoding='utf-8', header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Tipo', 'Zona Associada', 'Idade Mínima', 'Altura Mínima', 'Intensidade', 'Estado Atual', 'Duração', 'Descrição'])
        print(Fore.LIGHTBLUE_EX + Style.BRIGHT +'Aqui estão as diversoes disponíveis.')
        print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Tipo', 'Zona Associada', 'Idade Mínima', 'Altura Mínima', 'Intensidade', 'Estado Atual', 'Duração', 'Descrição']].to_string(index=False))
    except FileNotFoundError:
        print("Arquivo de diversões não encontrado.")
    except UnicodeDecodeError:
        print("")
        for cod in codificacoes:
            try:
                df = pd.read_csv(arquivo, encoding=cod, header=None, names=['Código', 'Nome', 'Latitude', 'Longitude', 'Tipo', 'Zona Associada', 'Idade Mínima', 'Altura Mínima', 'Intensidade', 'Estado Atual', 'Duração', 'Descrição'])
                print(f'Aqui estão as diversões disponíveis:')
                print(df[['Código', 'Nome', 'Latitude', 'Longitude', 'Tipo', 'Zona Associada', 'Idade Mínima', 'Altura Mínima', 'Intensidade', 'Estado Atual', 'Duração', 'Descrição']].to_string(index=False))
                break
            except UnicodeDecodeError:
                pass


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
        # Lista os códigos de zona disponíveis
    codigos_zona = ler_arquivo('Arquivos\zonas.csv', codificacoes)
    if not codigos_zona:
        print("Não há códigos de zona disponíveis. Crie uma zona primeiro.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
    print("Códigos de Zona Disponíveis:")
    for i, codigo in enumerate(codigos_zona, start=1):
        print(f"{i}. {codigo}")

    # Solicita ao usuário que escolha um código de zona
    escolha_zona = input("Escolha o número correspondente ao código de zona desejado: ")
    
    try:
        indice_zona = int(escolha_zona) - 1
        if 0 <= indice_zona < len(codigos_zona):
            zona_associada = codigos_zona[indice_zona]
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            criar()
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
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
        return ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))

def criar_comodidade():
    print("Criar Nova Comodidade:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    # Lista os códigos de zona disponíveis
    codigos_zona = ler_arquivo('Arquivos\zonas.csv', codificacoes)
    if not codigos_zona:
        print("Não há códigos de zona disponíveis. Crie uma zona primeiro.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
    print("Códigos de Zona Disponíveis:")
    for i, codigo in enumerate(codigos_zona, start=1):
        print(f"{i}. {codigo}")

    # Solicita ao usuário que escolha um código de zona
    escolha_zona = input("Escolha o número correspondente ao código de zona desejado: ")
    
    try:
        indice_zona = int(escolha_zona) - 1
        if 0 <= indice_zona < len(codigos_zona):
            zona_associada = codigos_zona[indice_zona]
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            criar()
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

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
        
#----------------------------------------------------------------Criar Paragem de Comboio--------------------------------------------------------------#

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


    # Lista os códigos de zona disponíveis
    codigos_zona = ler_arquivo('Arquivos\zonas.csv', codificacoes)
    if not codigos_zona:
        print("Não há códigos de zona disponíveis. Crie uma zona primeiro.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
    print("Códigos de Zona Disponíveis:")
    for i, codigo in enumerate(codigos_zona, start=1):
        print(f"{i}. {codigo}")

    # Solicita ao usuário que escolha um código de zona
    escolha_zona = input("Escolha o número correspondente ao código de zona desejado: ")
    

    try:
        indice_zona = int(escolha_zona) - 1
        if 0 <= indice_zona < len(codigos_zona):
            zona_associada = list(codigos_zona.keys())[indice_zona]
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            criar()
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')


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


#----------------------------------------------------------------Criar Ligação Comboios--------------------------------------------------------------#

class LigacaoComboio:
    def __init__(self, codigo, paragem_inicio, paragem_fim, distancia):
        self.codigo = codigo
        self.paragem_inicio = paragem_inicio
        self.paragem_fim = paragem_fim
        self.distancia = distancia

    def gerar_codigo(self, paragem_inicio, paragem_fim):
        # Gera um código aleatório de quatro letras em maiúsculas
        return f"{paragem_inicio}{paragem_fim}"

def criar_ligacao_comboio():
    print("Criar Nova Ligação de Comboio:")
    
    # Lista os códigos e nomes de paragem de comboio disponíveis
    codigos_nomes_paragem = ler_arquivo('Arquivos\paragens_comboio.csv', codificacoes)
    if not codigos_nomes_paragem:
        print("Não há códigos de paragem disponíveis. Crie uma paragem primeiro.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
    print("Códigos e Nomes de Paragem de Comboio Disponíveis:")
    for i, (codigo, nome) in enumerate(codigos_nomes_paragem.items(), start=1):
        print(f"{i}. {codigo}: {nome}")

    # Solicita ao usuário que escolha códigos de paragem
    escolha_inicio = input("Escolha o número correspondente ao código de paragem de início desejado: ")
    escolha_fim = input("Escolha o número correspondente ao código de paragem de fim desejado: ")

    try:
        indice_inicio = int(escolha_inicio) - 1
        indice_fim = int(escolha_fim) - 1
        if 0 <= indice_inicio < len(codigos_nomes_paragem) and 0 <= indice_fim < len(codigos_nomes_paragem):
            paragem_inicio = list(codigos_nomes_paragem.keys())[indice_inicio]
            paragem_fim = list(codigos_nomes_paragem.keys())[indice_fim]
            codigo_ligacao = f"{paragem_inicio}{paragem_fim}"
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            criar()
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

    distancia = float(input("Distância: "))

    nova_ligacao_comboio = LigacaoComboio(
        codigo=codigo_ligacao,
        paragem_inicio=codigos_nomes_paragem[paragem_inicio],
        paragem_fim=codigos_nomes_paragem[paragem_fim],
        distancia=distancia
    )

    print("\nInformações da Nova Ligação de Comboio:")
    print("Código:", nova_ligacao_comboio.codigo)
    print("Paragem de Início:", nova_ligacao_comboio.paragem_inicio)
    print("Paragem de Fim:", nova_ligacao_comboio.paragem_fim)
    print("Distância:", nova_ligacao_comboio.distancia)

    salvar = input("\nDeseja salvar a nova ligação de comboio? (s/n): ").lower()

    if salvar == 's':
        salvar_ligacao_comboio_em_arquivo(nova_ligacao_comboio)
        print("Ligação de Comboio salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. A ligação de comboio não foi salva.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

def salvar_ligacao_comboio_em_arquivo(ligacao_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'ligacoes_comboio.csv')

    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            ligacao_comboio.codigo, ligacao_comboio.paragem_inicio, ligacao_comboio.paragem_fim,
            ligacao_comboio.distancia
        ])


#----------------------------------------------------------------Criar trajecto Comboios--------------------------------------------------------------#

# Modificamos a função ler_arquivo para retornar um dicionário com os códigos e nomes das paragens
class TrajectoComboio:
    def __init__(self, codigo_trajecto, nome, paragem_partida, paragem_chegada, estado_atual, periodicidade):
        self.codigo_trajecto = codigo_trajecto
        self.nome = nome
        self.paragem_partida = paragem_partida
        self.paragem_chegada = paragem_chegada
        self.estado_atual = estado_atual
        self.periodicidade = periodicidade

    def gerar_codigo_trajecto(self, paragem_partida, paragem_chegada):
        # Gera um código aleatório de quatro letras em maiúsculas
        return f"{paragem_partida}{paragem_chegada}"

def criar_trajecto_comboio():
    print("Criar Novo Trajecto de Comboio:")
    
    # Lista os códigos e nomes de paragem de comboio disponíveis
    codigos_nomes_paragem = ler_arquivo('Arquivos\paragens_comboio.csv', codificacoes)
    if not codigos_nomes_paragem:
        print("Não há códigos de paragem disponíveis. Crie uma paragem primeiro.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    
    print("Códigos e Nomes de Paragem de Comboio Disponíveis:")
    for i, (codigo, nome) in enumerate(codigos_nomes_paragem.items(), start=1):
        print(f"{i}. {codigo}: {nome}")

    # Solicita ao usuário que escolha códigos de paragem
    escolha_partida = input("Escolha o número correspondente ao código de paragem de partida desejado: ")
    escolha_chegada = input("Escolha o número correspondente ao código de paragem de chegada desejado: ")

    try:
        indice_partida = int(escolha_partida) - 1
        indice_chegada = int(escolha_chegada) - 1
        if 0 <= indice_partida < len(codigos_nomes_paragem) and 0 <= indice_chegada < len(codigos_nomes_paragem):
            paragem_partida = list(codigos_nomes_paragem.keys())[indice_partida]
            paragem_chegada = list(codigos_nomes_paragem.keys())[indice_chegada]
            codigo_trajecto = f"{paragem_partida}{paragem_chegada}"
        else:
            print("Opção inválida. Tente novamente.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            criar()
    except ValueError:
        print("Entrada inválida. Deve ser um número.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

    nome = input("Nome do Trajecto: ")
    estado_atual = input("Estado Atual: ")
    periodicidade = input("Periodicidade: ")

    novo_trajecto_comboio = TrajectoComboio(
        codigo_trajecto=codigo_trajecto,
        nome=nome,
        paragem_partida=codigos_nomes_paragem[paragem_partida],
        paragem_chegada=codigos_nomes_paragem[paragem_chegada],
        estado_atual=estado_atual,
        periodicidade=periodicidade
    )

    print("\nInformações do Novo Trajecto de Comboio:")
    print("Código Trajecto:", novo_trajecto_comboio.codigo_trajecto)
    print("Nome:", novo_trajecto_comboio.nome)
    print("Paragem de Partida:", novo_trajecto_comboio.paragem_partida)
    print("Paragem de Chegada:", novo_trajecto_comboio.paragem_chegada)
    print("Estado Atual:", novo_trajecto_comboio.estado_atual)
    print("Periodicidade:", novo_trajecto_comboio.periodicidade)

    salvar = input("\nDeseja salvar o novo trajecto de comboio? (s/n): ").lower()

    if salvar == 's':
        salvar_trajecto_comboio_em_arquivo(novo_trajecto_comboio)
        print("Trajecto de Comboio salvo com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()
    else:
        print("Operação cancelada. O trajecto de comboio não foi salvo.")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        criar()

def salvar_trajecto_comboio_em_arquivo(trajecto_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'trajectos_comboio.csv')

    with open(caminho_arquivo, mode='a', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        writer.writerow([
            trajecto_comboio.codigo_trajecto, trajecto_comboio.nome, trajecto_comboio.paragem_partida,
            trajecto_comboio.paragem_chegada, trajecto_comboio.estado_atual, trajecto_comboio.periodicidade
        ])

#----------------------------------------------------------------Menu de Criação--------------------------------------------------------------#
def criar():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 55 + "|    Criar    |" + "-" * 55 + "+")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 33 + "| 7. Procurar |" + " " * 33 + "| 9. Voltar |" + " " * 32 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 15 + "| 1. Criar uma Zona |" + " " * 16 + "| 2. Criar uma Diversão |" + " " * 12 + "| 3. Criar uma comodidade |" + " " * 9 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 5 + "| 4. Criar uma paragem de comboio |" + " " * 5 + "| 5. Criar uma ligação de 2 paragens |" + " " * 5 + "| 6. Criar trajecto de comboio |" + " " * 5 + "|")
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
        elif escolha == '4':
            criar_paragem_comboio()
        elif escolha == '5':
            criar_ligacao_comboio()
        elif escolha == '6':
            criar_trajecto_comboio()
        elif escolha == '9':
            menu_admin() 
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")

Opcao_criar = ("criar", "1")

#----------------------------------------------------------------Menu Consultar--------------------------------------------------------------#
def menu_consultar():
    while True:
        print_consultar()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 +"↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha.lower() in Opcao_criar:
            ler_diversoes('Arquivos/diversoes.csv', codificacoes)
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == 'Comodidades' or escolha == '2':
            ler_comodidades('Arquivos/comodidades.csv', codificacoes)
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == 'Zonas' or escolha == '3':
            ler_arquivo('Arquivos/zonas.csv', codificacoes)
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == 'voltar' or escolha == '9':
            menu_admin()
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")

def print_consultar():
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 53 + "|    Consultar    |" + "-" * 52 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 12 + "| 1. Diversoes |" + " " * 12 + "| 2. Comodidades |" + " " * 12 + "| 3. Zonas |" + " " * 12 + "| 9. Voltar |" + " " * 18 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")   
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")     
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")  
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")


#----------------------------------------------------------------Menu Principal--------------------------------------------------------------#
def menu_admin():
     while True:
        print_menu()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 +"↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha.lower() in Opcao_criar:
            print("lol")
            criar()
        elif escolha == 'alterar' or escolha == '2':
            print("Alterar")
        elif escolha == 'bilhetes' or escolha == '3':
            print("Bilhetes")
        elif escolha == 'procurar' or escolha == '4':
            print("procurar")
        elif escolha == 'consultar' or escolha == '5':
            menu_consultar()
        elif escolha == 'Encerrar' or escolha == '0':
            exit()    
        elif escolha == '6':
            opcao = input("\nDeseja voltar a pagina de login? (s/n): ").lower()
    
            if opcao == 's':
                print("A voltar a pagina de login")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                menu.menu_principal()
            else:
                print("A voltar ao menu inicial")
                time.sleep(2)
                os.system('cls' if os.name == 'nt' else 'clear')
                menu_admin()

def print_menu():
    
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 51 + "|    Administração    |" + "-" * 50 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 1 .Criar |" + " " * 3 + "| 2. Alterar |" + " " * 3 + "| 3. Bilhetes |" + " " * 3 + "| 4. Procurar |" + " " * 3 + "| 5. Consultar |" + " " * 4 +"| 6. Log out |" + " " * 3 + "| 0. Encerrar |" + " " * 2 +"|")
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