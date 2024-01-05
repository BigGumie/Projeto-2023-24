import keyboard 
import random #serve para gerar os 4 digitos na criação da zona
import os # De momento so uso para limpar o terminal
from colorama import init, Fore, Style #Cores e estilos
import pandas as pd #Para utilizamento de tabelas
import time #Para dar tempo entre as funçoes
import csv #Para criar ficheiros em EXEL
import menu #Chama o menu.py
import datetime

init(autoreset=True) #Loop que ja vem com a biblioteca 
os.system('cls' if os.name == 'nt' else 'clear') #Limpa o terminal



#---------------------------------------------------------------Bilhetes ---------------------------------------------------------#

class TipoBilhete:
    def __init__(self, codigo, nome, duracao, descricao):
        self.codigo = codigo
        self.nome = nome
        self.duracao = duracao
        self.descricao = descricao

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_tipos_bilhetes():
    tipos_bilhetes = []
    arquivo_tipos_bilhetes = "Arquivos/tipos_bilhetes.txt"

    try:
        if not os.path.exists(arquivo_tipos_bilhetes):
            with open(arquivo_tipos_bilhetes, mode='w') as new_file:
                pass 

        with open(arquivo_tipos_bilhetes, mode='r') as file:
            for linha in file:
                dados_tipo_bilhete = linha.strip().split('\t')
                tipo_bilhete = TipoBilhete(*dados_tipo_bilhete)
                tipos_bilhetes.append(tipo_bilhete)
    except Exception as e:
        print(f"Erro inesperado ao ler 'tipos_bilhetes.txt': {e}")

    return tipos_bilhetes



class Bilhete:
    def __init__(self, referencia, nome_pessoa, nacionalidade, tipo_bilhete, dia_inicio, mes_inicio, ano_inicio, dia_fim, mes_fim, ano_fim):
        self.referencia = referencia
        self.nome_pessoa = nome_pessoa
        self.nacionalidade = nacionalidade
        self.tipo_bilhete = tipo_bilhete
        self.data_inicio = datetime.date(ano_inicio, mes_inicio, dia_inicio)
        self.data_fim = datetime.date(ano_fim, mes_fim, dia_fim)

    @staticmethod
    def gerar_referencia():
        referencia = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(8))
        return referencia

def emitir_bilhete():
    print("Emissão de Bilhete:")
    
    tipos_bilhetes = obter_tipos_bilhetes()
    if not tipos_bilhetes:
        print("Erro: Não existem tipos de bilhetes cadastrados.")
        return

    print("Tipos de Bilhetes Disponíveis:")
    for tipo_bilhete in tipos_bilhetes:
        print(f"{tipo_bilhete.codigo}: {tipo_bilhete.nome} - {tipo_bilhete.descricao}")

    codigo_tipo_bilhete = input("Digite o código do tipo de bilhete desejado: ")
    
    tipo_bilhete_escolhido = None
    for tipo_bilhete in tipos_bilhetes:
        if tipo_bilhete.codigo == codigo_tipo_bilhete:
            tipo_bilhete_escolhido = tipo_bilhete
            break

    if not tipo_bilhete_escolhido:
        print("Erro: Tipo de bilhete não encontrado.")
        return

    nome_pessoa = input("Digite o nome da pessoa: ")
    nacionalidade = input("Digite a nacionalidade: ")
    dia_inicio = int(input("Digite o dia de início: "))
    mes_inicio = int(input("Digite o mês de início: "))
    ano_inicio = int(input("Digite o ano de início: "))
    dia_fim = int(input("Digite o dia de fim: "))
    mes_fim = int(input("Digite o mês de fim: "))
    ano_fim = int(input("Digite o ano de fim: "))

    nova_referencia = Bilhete.gerar_referencia()
    novo_bilhete = Bilhete(nova_referencia, nome_pessoa, nacionalidade, tipo_bilhete_escolhido, dia_inicio, mes_inicio, ano_inicio, dia_fim, mes_fim, ano_fim)

    print("\nInformações do Novo Bilhete:")
    print("Referência:", novo_bilhete.referencia)
    print("Nome da Pessoa:", novo_bilhete.nome_pessoa)
    print("Nacionalidade:", novo_bilhete.nacionalidade)
    print("Tipo de Bilhete:", f"{tipo_bilhete_escolhido.nome} - {tipo_bilhete_escolhido.descricao}")
    print("Data de Início:", novo_bilhete.data_inicio.strftime("%d/%m/%Y"))
    print("Data de Fim:", novo_bilhete.data_fim.strftime("%d/%m/%Y"))

    salvar_bilhete(novo_bilhete)

def salvar_bilhete(bilhete):
    arquivo_bilhetes = "Arquivos/bilhetes.txt"

    try:
        with open(arquivo_bilhetes, mode='a') as file:
            file.write(f"{bilhete.referencia}\t{bilhete.nome_pessoa}\t{bilhete.nacionalidade}\t"
                       f"{bilhete.tipo_bilhete.codigo}\t{bilhete.data_inicio.day}\t{bilhete.data_inicio.month}\t{bilhete.data_inicio.year}\t"
                       f"{bilhete.data_fim.day}\t{bilhete.data_fim.month}\t{bilhete.data_fim.year}\n")
        print("Bilhete emitido com sucesso!")

    except FileNotFoundError:
        print("Erro: O arquivo 'bilhetes.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao salvar o bilhete: {e}")

def listar_bilhetes_emitidos():
    print("Listagem de Bilhetes Emitidos:")
    try:
        with open("Arquivos/bilhetes.txt", mode='r') as file:
            for linha in file:
                dados_bilhete = linha.strip().split('\t')
                print("Referência:", dados_bilhete[0])
                print("Nome da Pessoa:", dados_bilhete[1])
                print("Nacionalidade:", dados_bilhete[2])
                codigo_tipo_bilhete = dados_bilhete[3]
                tipo_bilhete = obter_tipo_bilhete_por_codigo(codigo_tipo_bilhete)
                print("Tipo de Bilhete:", f"{tipo_bilhete.nome} - {tipo_bilhete.descricao}")
                print("Data de Início:", f"{dados_bilhete[4]}/{dados_bilhete[5]}/{dados_bilhete[6]}")
                print("Data de Fim:", f"{dados_bilhete[7]}/{dados_bilhete[8]}/{dados_bilhete[9]}")
                print("--------")

    except FileNotFoundError:
        print("Nenhum bilhete foi emitido ainda.")
    except Exception as e:
        print(f"Erro inesperado ao listar os bilhetes emitidos: {e}")

def obter_tipo_bilhete_por_codigo(codigo):
    tipos_bilhetes = obter_tipos_bilhetes()
    for tipo_bilhete in tipos_bilhetes:
        if tipo_bilhete.codigo == codigo:
            return tipo_bilhete
    return None

def listar_referencias_bilhetes():
    try:
        with open("Arquivos/bilhetes.txt", mode='r') as file:
            referencias = [linha.strip().split('\t')[0] for linha in file]
            return referencias
    except FileNotFoundError:
        return []

def procurar_bilhete_por_referencia():
    print("Procura de Bilhete por Referência:")
    
    referencias_disponiveis = listar_referencias_bilhetes()
    
    if not referencias_disponiveis:
        print("Nenhum bilhete foi emitido ainda.")
        return

    print("Referências Disponíveis:")
    for referencia in referencias_disponiveis:
        print(referencia)

    referencia_desejada = input("Digite a referência do bilhete que deseja procurar: ")

    try:
        with open("Arquivos/bilhetes.txt", mode='r') as file:
            for linha in file:
                dados_bilhete = linha.strip().split('\t')
                if dados_bilhete[0] == referencia_desejada:
                    print("Referência:", dados_bilhete[0])
                    print("Nome da Pessoa:", dados_bilhete[1])
                    print("Nacionalidade:", dados_bilhete[2])
                    codigo_tipo_bilhete = dados_bilhete[3]
                    tipo_bilhete = obter_tipo_bilhete_por_codigo(codigo_tipo_bilhete)
                    print("Tipo de Bilhete:", f"{tipo_bilhete.nome} - {tipo_bilhete.descricao}")
                    print("Data de Início:", f"{dados_bilhete[4]}/{dados_bilhete[5]}/{dados_bilhete[6]}")
                    print("Data de Fim:", f"{dados_bilhete[7]}/{dados_bilhete[8]}/{dados_bilhete[9]}")
                    return

    except FileNotFoundError:
        print("Nenhum bilhete foi emitido ainda.")
    except Exception as e:
        print(f"Erro inesperado ao procurar o bilhete por referência: {e}")
    print("Bilhete não encontrado.")



def obter_ultimo_codigo():
    try:
        with open("Arquivos/tipos_bilhetes.txt", mode='r') as file:
            linhas = file.readlines()
            if linhas:
                ultimo_codigo = int(linhas[-1].split('\t')[0])
                return ultimo_codigo + 1
            else:
                return 1
    except FileNotFoundError:
        return 1
    except Exception as e:
        print(f"Erro ao obter o último código: {e}")
        return 1

def criar_tipo_bilhete():
    print("Criação de Tipo de Bilhete:")
    
    novo_codigo = obter_ultimo_codigo()
    nome = input("Digite o nome do tipo de bilhete: ")
    duracao = input("Digite a duração do tipo de bilhete: ")
    descricao = input("Digite a descrição do tipo de bilhete: ")

    novo_tipo_bilhete = TipoBilhete(novo_codigo, nome, duracao, descricao)

    print("\nNovo Tipo de Bilhete Criado:")
    print("Código:", novo_tipo_bilhete.codigo)
    print("Nome:", novo_tipo_bilhete.nome)
    print("Duração:", novo_tipo_bilhete.duracao)
    print("Descrição:", novo_tipo_bilhete.descricao)

    salvar_tipo_bilhete(novo_tipo_bilhete)

def salvar_tipo_bilhete(tipo_bilhete):
    try:
        with open("Arquivos/tipos_bilhetes.txt", mode='a') as file:
            file.write(f"{tipo_bilhete.codigo}\t{tipo_bilhete.nome}\t{tipo_bilhete.duracao}\t{tipo_bilhete.descricao}\n")
        print("Tipo de bilhete salvo com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar o tipo de bilhete: {e}")


def mostrar_referencias_disponiveis():
    referencias = listar_referencias_bilhetes()

    if not referencias:
        print("Nenhum bilhete foi emitido ainda.")
        return

    print("Referências Disponíveis:")
    for referencia in referencias:
        print(referencia)

#---------------------------------------------------------------Procurar Diversoes---------------------------------------------------------#

def procurar_diversoes():
    print("Opções de Pesquisa:")
    zonas_disponiveis = obter_zonas_existentes()
    tipos_disponiveis = ["aberto", "fechado"]
    intensidades_disponiveis = ["alta", "media", "baixa"]

    zona = input(f"Zona ({', '.join(zonas_disponiveis)}) (deixe em branco para ignorar): ").upper()
    tipo = input(f"Tipo ({', '.join(tipos_disponiveis)}) (deixe em branco para ignorar): ").lower()
    intensidade = input(f"Intensidade ({', '.join(intensidades_disponiveis)}) (deixe em branco para ignorar): ").lower()
    estado = input("Estado (deixe em branco para ignorar): ")

    # Restrições de entrada
    if zona and zona not in zonas_disponiveis:
        print("Erro: Zona inválida.")
        return
    if tipo and tipo not in tipos_disponiveis:
        print("Erro: Tipo inválido.")
        return
    if intensidade and intensidade not in intensidades_disponiveis:
        print("Erro: Intensidade inválida.")
        return

    arquivo_diversoes = "Arquivos/diversoes.txt"

    try:
        with open(arquivo_diversoes, mode='r') as file:
            for linha in file:
                dados_diversao = linha.strip().split('\t')

                # Filtros
                if (not zona or dados_diversao[5] == zona) and \
                   (not tipo or dados_diversao[9] == tipo) and \
                   (not intensidade or dados_diversao[8] == intensidade) and \
                   (not estado or dados_diversao[4] == estado):
                    print("Código:", dados_diversao[0])
                    print("Nome:", dados_diversao[1])
                    print("Latitude:", dados_diversao[2])
                    print("Longitude:", dados_diversao[3])
                    print("Tipo:", dados_diversao[4])
                    print("Zona Associada:", dados_diversao[5])
                    print("Idade Mínima:", dados_diversao[6])
                    print("Altura Mínima:", dados_diversao[7])
                    print("Intensidade:", dados_diversao[8])
                    print("Estado:", dados_diversao[9])
                    print("Duração:", dados_diversao[10])
                    print("Descrição:", dados_diversao[11])
                    print("--------")

    except FileNotFoundError:
        print("Erro: O arquivo 'diversoes.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'diversoes.txt': {e}")

#---------------------------------------------------------------Procurar comodidades---------------------------------------------------------#

def procurar_comodidades():
    print("Opções de Pesquisa:")
    zonas_disponiveis = obter_zonas_existentes()
    tipos_disponiveis = ["aberto", "fechado"]

    zona = input(f"Zona ({', '.join(zonas_disponiveis)}) (deixe em branco para ignorar): ").upper()
    tipo = input(f"Tipo ({', '.join(tipos_disponiveis)}) (deixe em branco para ignorar): ").lower()
    estado = input("Estado (deixe em branco para ignorar): ")

    # Restrições de entrada
    if zona and zona not in zonas_disponiveis:
        print("Erro: Zona inválida.")
        return
    if tipo and tipo not in tipos_disponiveis:
        print("Erro: Tipo inválido.")
        return

    arquivo_comodidades = "Arquivos/comodidades.txt"

    try:
        with open(arquivo_comodidades, mode='r') as file:
            for linha in file:
                dados_comodidade = linha.strip().split('\t')

                # Filtros
                if (not zona or dados_comodidade[2] == zona) and \
                   (not tipo or dados_comodidade[3] == tipo) and \
                   (not estado or dados_comodidade[4] == estado):
                   
                    print("Código:", dados_comodidade[0])
                    print("Nome:", dados_comodidade[1])
                    print("Zona Associada:", dados_comodidade[2])
                    print("Estado:", dados_comodidade[3])
                    print("Descricao:", dados_comodidade[6])
                    print("--------")

    except FileNotFoundError:
        print("Erro: O arquivo 'comodidades.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'comodidades.txt': {e}")


#---------------------------------------------------------------Procurar trejectos---------------------------------------------------------#

def procurar_trajectos_comboio():
    print("Opções de Pesquisa:")
    zonas_disponiveis = obter_zonas_existentes()
    zona_inicial = input(f"Zona Inicial ({', '.join(zonas_disponiveis)}) (deixe em branco para ignorar): ").upper()
    ordenacao_ascendente = input("Ordenação Ascendente (s/n): ").lower() == 's'

    arquivo_trajectos_comboio = "Arquivos/trajectos_comboio.txt"

    try:
        with open(arquivo_trajectos_comboio, mode='r') as file:
            linhas = file.readlines()

            # Filtros
            trajectos_filtrados = []
            for linha in linhas:
                dados_trajecto = linha.strip().split('\t')
                if (not zona_inicial or dados_trajecto[2] == zona_inicial):
                    trajectos_filtrados.append(dados_trajecto)

            # Ordenação
            trajectos_filtrados.sort(key=lambda x: x[2], reverse=not ordenacao_ascendente)

            # Exibição
            for trajecto in trajectos_filtrados:
                print("Código:", trajecto[0])
                print("Nome:", trajecto[1])
                print("Paragem de Partida:", trajecto[2])
                print("Paragem de Chegada:", trajecto[3])
                print("Estado Atual:", trajecto[4])
                print("Periodicidade:", trajecto[5])
                print("--------")

    except FileNotFoundError:
        print("Erro: O arquivo 'trajectos_comboio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'trajectos_comboio.txt': {e}")


#----------------------------------------------------------------Alterar estado--------------------------------------------------------------#
def obter_zonas_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.txt')

    zonas_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_zona = linha.split('\t')[0]
                zonas_existentes.add(codigo_zona)
    except FileNotFoundError:
        print("Erro: O arquivo 'zonas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'zonas.txt': {e}")

    return zonas_existentes

def alterar_estado_diversao():
    # Ler o arquivo diversoes.txt
    arquivo_diversoes = "Arquivos/diversoes.txt"

    try:
        with open(arquivo_diversoes, mode='r') as file:
            linhas = file.readlines()

        # Exibir as diversões disponíveis
        print("\nDiversões Disponíveis:")
        for linha in linhas:
            dados_diversao = linha.strip().split('\t')
            print(f"Código: {dados_diversao[0]}, Nome: {dados_diversao[1]}, Estado Atual: {dados_diversao[3]}")

        # Solicitar ao usuário o código da diversão a ser alterada
        codigo_diversao = input("\nDigite o código da diversão que deseja alterar: ")

        # Encontrar a diversão com base no código
        diversao_encontrada = None
        for i, linha in enumerate(linhas):
            dados_diversao = linha.strip().split('\t')
            if dados_diversao[0] == codigo_diversao:
                diversao_encontrada = dados_diversao
                break

        if diversao_encontrada:
            print("\nInformações da Diversão:")
            print("Código:", diversao_encontrada[0])
            print("Nome:", diversao_encontrada[1])
            print("Estado Atual:", diversao_encontrada[3])

            # Solicitar as novas informações
            novo_nome = input("Digite o novo nome: ")
            nova_latitude = input("Digite a nova latitude: ")
            nova_longitude = input("Digite a nova longitude: ")
            novo_tipo = input("Digite o novo tipo: ")
            
            
            # Verificar se a nova zona_associada é válida
            zonas_disponiveis = obter_zonas_existentes()
            zonas_existentes = obter_zonas_existentes()
            if not zonas_existentes:
                print("Erro: Não existem zonas cadastradas.")
                return

            print("Zonas Disponíveis:", ', '.join(zonas_existentes))
            nova_zona_associada = input("Zona Associada: ").upper()
            if nova_zona_associada not in zonas_disponiveis:
                print("Erro: Zona associada não encontrada.")
                return

            nova_idade_minima = input("Digite a nova idade mínima: ")
            nova_altura_minima = input("Digite a nova altura mínima: ")
            nova_intensidade = input("Digite a nova intensidade: ")
            novo_estado = input("Digite o novo estado (aberto/fechado): ")
            nova_duracao = input("Digite a nova duração: ")
            nova_descricao = input("Digite a nova descrição: ")

            # Remover a diversão antiga da lista
            linhas.pop(i)

            # Atualizar o arquivo diversoes.txt
            with open(arquivo_diversoes, mode='w') as file:
                for linha in linhas:
                    file.write(linha)

                # Escrever a diversão com as informações atualizadas
                diversao_encontrada[1] = novo_nome
                diversao_encontrada[2] = nova_latitude
                diversao_encontrada[3] = nova_longitude
                diversao_encontrada[4] = novo_tipo
                diversao_encontrada[5] = nova_zona_associada
                diversao_encontrada[6] = nova_idade_minima
                diversao_encontrada[7] = nova_altura_minima
                diversao_encontrada[8] = nova_intensidade
                diversao_encontrada[9] = novo_estado
                diversao_encontrada[10] = nova_duracao
                diversao_encontrada[11] = nova_descricao

                file.write('\t'.join(diversao_encontrada) + '\n')

            print("Informações da diversão atualizadas com sucesso!")
        else:
            print("Diversão não encontrada com o código fornecido.")

    except FileNotFoundError:
        print("Erro: O arquivo 'diversoes.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'diversoes.txt': {e}")

#----------------------------------------------------------------Alterar Comodidade------------------------------------------------------------------#
def obter_comodidades_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'comodidades.txt')

    comodidades_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_comodidade = linha.split('\t')[0]
                comodidades_existentes.add(codigo_comodidade)
    except FileNotFoundError:
        print("Erro: O arquivo 'comodidades.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'comodidades.txt': {e}")

    return comodidades_existentes

def alterar_info_comodidade():
    # Ler o arquivo comodidades.txt
    arquivo_comodidades = "Arquivos/comodidades.txt"

    try:
        with open(arquivo_comodidades, mode='r') as file:
            linhas = file.readlines()

        # Exibir as comodidades disponíveis
        print("\nComodidades Disponíveis:")
        for linha in linhas:
            dados_comodidade = linha.strip().split('\t')
            print(f"Código: {dados_comodidade[0]}, Nome: {dados_comodidade[1]}, Estado Atual: {dados_comodidade[3]}")

        # Solicitar ao usuário o código da comodidade a ser alterada
        codigo_comodidade = input("\nDigite o código da comodidade que deseja alterar: ")

        # Encontrar a comodidade com base no código
        comodidade_encontrada = None
        for i, linha in enumerate(linhas):
            dados_comodidade = linha.strip().split('\t')
            if dados_comodidade[0] == codigo_comodidade:
                comodidade_encontrada = dados_comodidade
                break

        if comodidade_encontrada:
            print("\nInformações da Comodidade:")
            print("Código:", comodidade_encontrada[0])
            print("Nome:", comodidade_encontrada[1])
            print("Estado Atual:", comodidade_encontrada[3])

            # Solicitar as novas informações
            novo_nome = input("Digite o novo nome: ")

            # Verificar se a nova zona_associada é válida
            zonas_disponiveis = obter_zonas_existentes()
            if not zonas_disponiveis:
                print("Erro: Não existem zonas cadastradas.")
                return

            print("Zonas Disponíveis:", ', '.join(zonas_disponiveis))
            nova_zona_associada = input("Zona Associada: ").upper()
            if nova_zona_associada not in zonas_disponiveis:
                print("Erro: Zona associada não encontrada.")
                return

            novo_estado = input("Digite o novo estado (aberto/fechado): ")

            # Remover a comodidade antiga da lista
            linhas.pop(i)

            # Atualizar o arquivo comodidades.txt
            with open(arquivo_comodidades, mode='w') as file:
                for linha in linhas:
                    file.write(linha)

                # Escrever a comodidade com as informações atualizadas
                comodidade_encontrada[1] = novo_nome
                comodidade_encontrada[2] = nova_zona_associada
                comodidade_encontrada[3] = novo_estado

                file.write('\t'.join(comodidade_encontrada) + '\n')

            print("Informações da comodidade atualizadas com sucesso!")
        else:
            print("Comodidade não encontrada com o código fornecido.")

    except FileNotFoundError:
        print("Erro: O arquivo 'comodidades.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'comodidades.txt': {e}")


#----------------------------------------------------------------Alterar Paragem------------------------------------------------------------------#
def obter_paragens_comboio_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'paragens_comboio.txt')

    paragens_comboio_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_paragem = linha.split('\t')[0]
                paragens_comboio_existentes.add(codigo_paragem)
    except FileNotFoundError:
        print("Erro: O arquivo 'paragens_comboio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'paragens_comboio.txt': {e}")

    return paragens_comboio_existentes

def alterar_info_trajecto_comboio():
    # Ler o arquivo trajectos_comboio.txt
    arquivo_trajectos_comboio = "Arquivos/trajectos_comboio.txt"

    try:
        with open(arquivo_trajectos_comboio, mode='r') as file:
            linhas = file.readlines()

        # Exibir os trajectos de comboio disponíveis
        print("\nTrajectos de Comboio Disponíveis:")
        for linha in linhas:
            dados_trajecto = linha.strip().split('\t')
            print(f"Código: {dados_trajecto[0]}, Nome: {dados_trajecto[1]}, Estado Atual: {dados_trajecto[4]}, Paragem de Partida: {dados_trajecto[2]}, Paragem de Chegada: {dados_trajecto[3]}")

        # Solicitar ao usuário o código do trajecto a ser alterado
        codigo_trajecto = input("\nDigite o código do trajecto de comboio que deseja alterar: ")

        # Encontrar o trajecto com base no código
        trajecto_encontrado = None
        for i, linha in enumerate(linhas):
            dados_trajecto = linha.strip().split('\t')
            if dados_trajecto[0] == codigo_trajecto:
                trajecto_encontrado = dados_trajecto
                break

        if trajecto_encontrado:
            print("\nInformações do Trajecto de Comboio:")
            print("Código:", trajecto_encontrado[0])
            print("Nome:", trajecto_encontrado[1])
            print("Estado Atual:", trajecto_encontrado[4])
            print("Paragem de Partida:", trajecto_encontrado[2])
            print("Paragem de Chegada:", trajecto_encontrado[3])

            # Solicitar as novas informações
            novo_nome = input("Digite o novo nome: ")

            # Verificar se as novas paragens de partida e chegada são válidas
            paragens_comboio_disponiveis = obter_paragens_comboio_existentes()
            if not paragens_comboio_disponiveis:
                print("Erro: Não existem paragens de comboio cadastradas.")
                return

            print("Paragens de Comboio Disponíveis:", ', '.join(paragens_comboio_disponiveis))
            nova_paragem_partida = input("Paragem de Partida: ").upper()
            nova_paragem_chegada = input("Paragem de Chegada: ").upper()

            if nova_paragem_partida not in paragens_comboio_disponiveis or nova_paragem_chegada not in paragens_comboio_disponiveis:
                print("Erro: Paragem de comboio não encontrada.")
                return

            novo_estado = input("Digite o novo estado (aberto/fechado): ")
            nova_periodicidade = input("Digite a nova periodicidade: ")

            # Remover o trajecto antigo da lista
            linhas.pop(i)

            # Atualizar o arquivo trajectos_comboio.txt
            with open(arquivo_trajectos_comboio, mode='w') as file:
                for linha in linhas:
                    file.write(linha)

                # Escrever o trajecto com as informações atualizadas
                trajecto_encontrado[1] = novo_nome
                trajecto_encontrado[2] = nova_paragem_partida
                trajecto_encontrado[3] = nova_paragem_chegada
                trajecto_encontrado[4] = novo_estado
                trajecto_encontrado[5] = nova_periodicidade

                file.write('\t'.join(trajecto_encontrado) + '\n')

            print("Informações do trajecto de comboio atualizadas com sucesso!")
        else:
            print("Trajecto de comboio não encontrado com o código fornecido.")

    except FileNotFoundError:
        print("Erro: O arquivo 'trajectos_comboio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'trajectos_comboio.txt': {e}")


#----------------------------------------------------------------Ler os ficheiros para a consulta--------------------------------------------------------------#
# Função para consultar a lista de diversões
def consultar_lista_diversoes():
    print("\nLista de Diversões:")
    try:
        with open("Arquivos/diversoes.txt", mode='r') as file:
            for linha in file:
                dados_diversao = linha.strip().split('\t')
                if len(dados_diversao) == 12:  #Verefica se a linhas suficeintes
                    print("Código:", dados_diversao[0])
                    print("Nome:", dados_diversao[1])
                    print("Latitude:", dados_diversao[2])
                    print("Longitude:", dados_diversao[3])
                    print("Tipo:", dados_diversao[4])
                    print("Zona Associada:", dados_diversao[5])
                    print("Idade Mínima:", dados_diversao[6])
                    print("Altura Mínima:", dados_diversao[7])
                    print("Intensidade:", dados_diversao[8])
                    print("Estado Atual:", dados_diversao[9])
                    print("Duração:", dados_diversao[10])
                    print("Descrição:", dados_diversao[11])
                    print("--------")
                else:
                    print(f"Erro: Linha com dados incompletos: {linha}")
            print("Fim do Loop")
    except FileNotFoundError:
        print("Erro: O arquivo 'diversoes.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'diversoes.txt': {e}")

# Função para consultar a lista de comodidades
def consultar_lista_comodidades():
    print("\nLista de Comodidades:")
    try:
        with open("Arquivos/comodidades.txt", mode='r') as file:
            for linha in file:
                dados_comodidade = linha.strip().split('\t')
                print("Código:", dados_comodidade[0])
                print("Nome:", dados_comodidade[1])
                print("Descrição:", dados_comodidade[2])
                print("--------")
    except FileNotFoundError:
        print("Erro: O arquivo 'comodidades.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'comodidades.txt': {e}")

# Função para consultar a lista de zonas
def consultar_lista_zonas():
    print("\nLista de Zonas:")
    try:
        with open("Arquivos/zonas.txt", mode='r') as file:
            for linha in file:
                dados_zona = linha.strip().split('\t')
                print("Código:", dados_zona[0])
                print("Nome:", dados_zona[1])
                print("Latitude:", dados_zona[2])
                print("Longitude:", dados_zona[3])
                print("Descrição:", dados_zona[4])
                print("--------")
    except FileNotFoundError:
        print("Erro: O arquivo 'zonas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'zonas.txt': {e}")

#----------------------------------------------------------------Criar Zona--------------------------------------------------------------#
class Zona:
    def __init__(self, codigo, nome, latitude, longitude, descricao):
        self.codigo = codigo
        self.nome = nome
        self.latitude = latitude
        self.longitude = longitude
        self.descricao = descricao

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def salvar_zona_em_arquivo(zona):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{zona.codigo}\t{zona.nome}\t{zona.latitude}\t{zona.longitude}\t{zona.descricao}\n")

def criar_zona():
    print("Criar Nova Zona:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))
    descricao = input("Descrição: ")

    nova_zona = Zona(Zona.gerar_codigo(), nome, latitude, longitude, descricao)

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

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_zonas_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.txt')

    zonas_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_zona = linha.split('\t')[0]
                zonas_existentes.add(codigo_zona)
    except FileNotFoundError:
        print("Erro: O arquivo 'zonas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'zonas.txt': {e}")

    return zonas_existentes

def validar_tipo_estado():
    while True:
        estado = input("Estado (aberto/fechado): ").lower()
        if estado in ['aberto', 'fechado']:
            return estado
        else:
            print("Erro: Por favor, digite 'aberto' ou 'fechado'.")

def criar_diversao():
    print("Criar Nova Diversão:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    zonas_existentes = obter_zonas_existentes()
    if not zonas_existentes:
        print("Erro: Não existem zonas disponiveis.")
        return

    print("Zonas Disponíveis:", ', '.join(zonas_existentes))
    zona_associada = input("Zona Associada: ").upper()
    if zona_associada not in zonas_existentes:
        print("Erro: Zona não encontrada.")
        return

    tipo = validar_tipo_estado()
    idade_minima = int(input("Idade Mínima: "))
    altura_minima = float(input("Altura Mínima: "))
    intensidade = input("Intensidade (Baixo/Médio/Alto/Extremo): ").capitalize()
    estado_atual = validar_tipo_estado()
    duracao = float(input("Duração (em minutos): "))
    descricao = input("Descrição: ")

    nova_diversao = Diversao(Diversao.gerar_codigo(), nome, latitude, longitude, tipo, zona_associada, idade_minima, altura_minima, intensidade, estado_atual, duracao, descricao)

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

def salvar_diversao_em_arquivo(diversao):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'diversoes.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{diversao.codigo}\t{diversao.nome}\t{diversao.latitude}\t{diversao.longitude}\t{diversao.tipo}\t{diversao.zona_associada}\t{diversao.idade_minima}\t{diversao.altura_minima}\t{diversao.intensidade}\t{diversao.estado_atual}\t{diversao.duracao}\t{diversao.descricao}\n")

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

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_zonas_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.txt')

    zonas_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_zona = linha.split('\t')[0]
                zonas_existentes.add(codigo_zona)
    except FileNotFoundError:
        print("Erro: O arquivo 'zonas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'zonas.txt': {e}")

    return zonas_existentes

def validar_estado():
    while True:
        estado = input("Estado (aberto/fechado): ").lower()
        if estado in ['aberto', 'fechado']:
            return estado
        else:
            print("Erro: Por favor, digite 'aberto' ou 'fechado'.")

def criar_comodidade():
    print("Criar Nova Comodidade:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    zonas_existentes = obter_zonas_existentes()
    if not zonas_existentes:
        print("Erro: Não existem zonas cadastradas.")
        return

    print("Zonas Disponíveis:", ', '.join(zonas_existentes))
    zona_associada = input("Zona Associada: ").upper()
    if zona_associada not in zonas_existentes:
        print("Erro: Zona não encontrada.")
        return

    estado_atual = validar_estado()
    descricao = input("Descrição: ")

    nova_comodidade = Comodidade(Comodidade.gerar_codigo(), nome, latitude, longitude, zona_associada, estado_atual, descricao)

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

def salvar_comodidade_em_arquivo(comodidade):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'comodidades.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{comodidade.codigo}\t{comodidade.nome}\t{comodidade.latitude}\t{comodidade.longitude}\t{comodidade.zona_associada}\t{comodidade.estado_atual}\t{comodidade.descricao}\n")

#----------------------------------------------------------------Criar Paragem de Comboio--------------------------------------------------------------#

class ParagemComboio:
    def __init__(self, codigo, nome, zona_associada, latitude, longitude, estado_atual, descricao):
        self.codigo = codigo
        self.nome = nome
        self.zona_associada = zona_associada
        self.latitude = latitude
        self.longitude = longitude
        self.estado_atual = estado_atual
        self.descricao = descricao

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_zonas_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'zonas.txt')

    zonas_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_zona = linha.split('\t')[0]
                zonas_existentes.add(codigo_zona)
    except FileNotFoundError:
        print("Erro: O arquivo 'zonas.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'zonas.txt': {e}")

    return zonas_existentes

def validar_estado():
    while True:
        estado = input("Estado (aberto/fechado): ").lower()
        if estado in ['aberto', 'fechado']:
            return estado
        else:
            print("Erro: Por favor, digite 'aberto' ou 'fechado'.")

def criar_paragem_comboio():
    print("Criar Nova Paragem de Comboio:")
    nome = input("Nome: ")
    latitude = float(input("Latitude: "))
    longitude = float(input("Longitude: "))

    zonas_existentes = obter_zonas_existentes()
    if not zonas_existentes:
        print("Erro: Não existem zonas cadastradas.")
        return

    print("Zonas Disponíveis:", ', '.join(zonas_existentes))
    zona_associada = input("Zona Associada: ").upper()
    if zona_associada not in zonas_existentes:
        print("Erro: Zona não encontrada.")
        return

    estado_atual = validar_estado()
    descricao = input("Descrição: ")

    nova_paragem_comboio = ParagemComboio(ParagemComboio.gerar_codigo(), nome, zona_associada, latitude, longitude, estado_atual, descricao)

    print("\nInformações da Nova Paragem de Comboio:")
    print("Código:", nova_paragem_comboio.codigo)
    print("Nome:", nova_paragem_comboio.nome)
    print("Latitude:", nova_paragem_comboio.latitude)
    print("Longitude:", nova_paragem_comboio.longitude)
    print("Zona Associada:", nova_paragem_comboio.zona_associada)
    print("Estado Atual:", nova_paragem_comboio.estado_atual)
    print("Descrição:", nova_paragem_comboio.descricao)

    salvar = input("\nDeseja salvar a nova paragem de comboio? (s/n): ").lower()
    
    if salvar == 's':
        salvar_paragem_comboio_em_arquivo(nova_paragem_comboio)
        print("Paragem de Comboio salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def salvar_paragem_comboio_em_arquivo(paragem_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'paragens_comboio.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{paragem_comboio.codigo}\t{paragem_comboio.nome}\t{paragem_comboio.zona_associada}\t{paragem_comboio.latitude}\t{paragem_comboio.longitude}\t{paragem_comboio.estado_atual}\t{paragem_comboio.descricao}\n")


#----------------------------------------------------------------Criar Ligação Comboios--------------------------------------------------------------#

class LigacaoComboio:
    def __init__(self, codigo, paragem_inicio, paragem_fim, distancia):
        self.codigo = codigo
        self.paragem_inicio = paragem_inicio
        self.paragem_fim = paragem_fim
        self.distancia = distancia

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_paragens_comboio_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'paragens_comboio.txt')

    paragens_comboio_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_paragem = linha.split('\t')[0]
                paragens_comboio_existentes.add(codigo_paragem)
    except FileNotFoundError:
        print("Erro: O arquivo 'paragens_comboio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'paragens_comboio.txt': {e}")

    return paragens_comboio_existentes

def criar_ligacao_comboio():
    print("Criar Nova Ligação de Comboio:")
    
    paragens_existentes = obter_paragens_comboio_existentes()
    if not paragens_existentes:
        print("Erro: Não existem paragens de comboio cadastradas.")
        return

    print("Paragens Disponíveis:", ', '.join(paragens_existentes))
    paragem_inicio_codigo = input("Código da Paragem de Início: ")
    paragem_fim_codigo = input("Código da Paragem de Fim: ")

    if paragem_inicio_codigo not in paragens_existentes or paragem_fim_codigo not in paragens_existentes:
        print("Erro: Paragem de comboio não encontrada.")
        return

    distancia = float(input("Distância entre as paragens (em km): "))

    nova_ligacao_comboio = LigacaoComboio(LigacaoComboio.gerar_codigo(), paragem_inicio_codigo, paragem_fim_codigo, distancia)


    print("\nInformações da Nova Ligação de Comboio:")
    print("Código:", nova_ligacao_comboio.codigo)
    print("Paragem de Início:", nova_ligacao_comboio.paragem_inicio)
    print("Paragem de Fim:", nova_ligacao_comboio.paragem_fim)
    print("Distância:", nova_ligacao_comboio.distancia, "km")

    salvar = input("\nDeseja salvar a nova ligação de comboio? (s/n): ").lower()
    
    if salvar == 's':
        salvar_ligacao_comboio_em_arquivo(nova_ligacao_comboio)
        print("Ligação de Comboio salva com sucesso!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

def salvar_ligacao_comboio_em_arquivo(ligacao_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'ligacoes_comboio.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{ligacao_comboio.codigo}\t{ligacao_comboio.paragem_inicio}\t{ligacao_comboio.paragem_fim}\t{ligacao_comboio.distancia}\n")

#----------------------------------------------------------------Criar trajecto Comboios--------------------------------------------------------------#
class TrajectoComboio:
    def __init__(self, codigo, nome, paragem_partida, paragem_chegada, estado_atual, periodicidade):
        self.codigo = codigo
        self.nome = nome
        self.paragem_partida = paragem_partida
        self.paragem_chegada = paragem_chegada
        self.estado_atual = estado_atual
        self.periodicidade = periodicidade

    @staticmethod
    def gerar_codigo():
        codigo = ''.join(random.choice(chr(random.randint(65, 90))) for _ in range(4))
        return codigo

def obter_paragens_comboio_existentes():
    pasta_arquivos = "Arquivos"
    caminho_arquivo = os.path.join(pasta_arquivos, 'paragens_comboio.txt')

    paragens_comboio_existentes = set()

    try:
        with open(caminho_arquivo, mode='r') as file:
            for linha in file:
                codigo_paragem = linha.split('\t')[0]
                paragens_comboio_existentes.add(codigo_paragem)
    except FileNotFoundError:
        print("Erro: O arquivo 'paragens_comboio.txt' não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado ao ler 'paragens_comboio.txt': {e}")

    return paragens_comboio_existentes

# Função para criar um trajecto de comboio
def criar_trajecto_comboio():
    print("Criar Novo Trajecto de Comboio:")

    paragens_existentes = obter_paragens_comboio_existentes()
    if not paragens_existentes:
        print("Erro: Não existem paragens de comboio cadastradas.")
        return

    print("Paragens Disponíveis:", ', '.join(paragens_existentes))
    
    nome = input("Nome do Trajecto: ")
    paragem_partida = input("Código da Paragem de Partida: ")
    paragem_chegada = input("Código da Paragem de Chegada: ")

    if paragem_partida not in paragens_existentes or paragem_chegada not in paragens_existentes:
        print("Erro: Paragem de comboio não encontrada.")
        return

    # Validar o estado atual
    while True:
        estado_atual = input("Estado Atual do Trajecto (aberto/fechado): ").lower()
        if estado_atual in ['aberto', 'fechado']:
            break
        else:
            print("Erro: Por favor, escolha entre 'aberto' ou 'fechado'.") 
    periodicidade = input("Periodicidade do Trajecto: ")

    novo_trajecto_comboio = TrajectoComboio(TrajectoComboio.gerar_codigo(), nome, paragem_partida, paragem_chegada, estado_atual, periodicidade)

    print("\nInformações do Novo Trajecto de Comboio:")
    print("Código:", novo_trajecto_comboio.codigo)
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

def salvar_trajecto_comboio_em_arquivo(trajecto_comboio):
    pasta_arquivos = "Arquivos"
    if not os.path.exists(pasta_arquivos):
        os.makedirs(pasta_arquivos)

    caminho_arquivo = os.path.join(pasta_arquivos, 'trajectos_comboio.txt')

    with open(caminho_arquivo, mode='a', newline='') as file:
        file.write(f"{trajecto_comboio.codigo}\t{trajecto_comboio.nome}\t{trajecto_comboio.paragem_partida}\t{trajecto_comboio.paragem_chegada}\t{trajecto_comboio.estado_atual}\t{trajecto_comboio.periodicidade}\n")


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

#----------------------------------------------------------------Menu Procurar--------------------------------------------------------------#
def menu_procurar():
    while True:
        print_procurar()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 + "↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha == '1':
            procurar_diversoes()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de procurar" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '2':
            procurar_comodidades()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de procurar" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '3':
            procurar_trajectos_comboio()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de procurar" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '9':
            menu_admin()
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")
def print_procurar():
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 53 + "|    Procurar    |" + "-" * 52 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 12 + "| 1. Diversoes |" + " " * 12 + "| 2. Comodidades |" + " " * 12 + "| 3. Trajectos |" + " " * 12 + "| 9. Voltar |" + " " * 14 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")   
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")     
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")  
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")

#----------------------------------------------------------------Menu Alterar--------------------------------------------------------------#
def menu_alterar():
    while True:
        print_alterar()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 + "↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha == '1':
            alterar_estado_diversao()
        elif escolha == '2':
            alterar_info_comodidade()
        elif escolha == '3':
            alterar_info_trajecto_comboio()

        elif escolha == '9':
            menu_admin()
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")
def print_alterar():
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 53 + "|    Alterar    |" + "-" * 52 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 12 + "| 1. Diversoes |" + " " * 12 + "| 2. Comodidades |" + " " * 12 + "| 3. Trajetos |" + " " * 12 + "| 9. Voltar |" + " " * 15 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")   
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")     
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")  
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")

#----------------------------------------------------------------Menu Bilhetes--------------------------------------------------------------#
    
def menu_bilhete():
    while True:
        print_bilhete()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 + "↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha == '1':
            emitir_bilhete()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de Bilhete" + "|")
            keyboard.read_event(suppress=True)  
        elif escolha == '2':
            listar_bilhetes_emitidos()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de Bilhete" + "|")
            keyboard.read_event(suppress=True)  
        elif escolha == '3':
            procurar_bilhete_por_referencia()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de Bilhete" + "|")
            keyboard.read_event(suppress=True)  
        elif escolha == '4':
            mostrar_referencias_disponiveis()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de Bilhete" + "|")
            keyboard.read_event(suppress=True)  
            keyboard.read_event(suppress=True)  
        elif escolha == '5':
            criar_tipo_bilhete()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de Bilhete" + "|")
            keyboard.read_event(suppress=True)  
        elif escolha == '9':
            menu_admin()
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")
def print_bilhete():
    print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 53 + "|    Bilhetes    |" + "-" * 52 + "+|")
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|") 
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 9 + "| 1. Emitir |" + " " * 9 + "| 2. Listar |" + " " * 9 + "| 3. Procurar |" + " " * 9 + "| 4. Referencia |" +" " * 9 + "| 9. Voltar |" + " " * 9 + "|")
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")         
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 52 + "| 5. Criar tipo |" + " " * 56 + "|")  
    print(Fore.GREEN + Style.BRIGHT + "|" + " " * 22 + "                                                                                        " + " " * 15 +"|")      
    print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 125 + "|")

#----------------------------------------------------------------Menu Consultar--------------------------------------------------------------#
def menu_consultar():
    while True:
        print_consultar()
        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 26 + "↓ Escolha uma opção ↓" + " ↓" * 26 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )

        if escolha == '1':
            consultar_lista_diversoes()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '2':
            consultar_lista_comodidades()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '3':
            consultar_lista_zonas()
            print(Fore.GREEN + Style.BRIGHT + "|" + "Clique em alguma tecla para voltar ao menu de consulta" + "|")
            keyboard.read_event(suppress=True)  # Aguarda que uma tecla seja pressionada
        elif escolha == '9':
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
            criar()
        elif escolha == 'alterar' or escolha == '2':
            menu_alterar()
        elif escolha == 'bilhetes' or escolha == '3':
            menu_bilhete()
            print("Bilhetes")
        elif escolha == 'procurar' or escolha == '4':
            print("procurar")
            menu_procurar()
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