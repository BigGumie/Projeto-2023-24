import Admin
from colorama import Fore, Style

def menu_usuario():

    while True:
        print(Fore.GREEN + Style.BRIGHT + "+" + "-" * 51 + "|    Cliente    |" + "-" * 51 + "+|")
        print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 120 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 1. Consultar lista de diversões." + " " * 83 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 2. Consultar lista de comodidades." + " " * 81 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 3. Consultar lista de zonas." + " " * 87 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 4. Consultar zona em detalhe." + " " * 86+ "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 5. Consultar diversão em detalhe." + " " * 82 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 6. Procurar diversões por filtro." + " " * 82 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 7. Procurar comodidades por filtro." + " " * 80 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 8. Procurar trajetos de comboio por zona inicial." + " " * 66 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 9. Listar bilhetes emitidos." + " " * 87 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 10. Listar bilhetes emitidos por data." + " " * 77 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 11. Procurar bilhete por referência." + " " * 79 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + " " * 3 + "| 0. Sair" + " " * 108 + "|")
        print(Fore.GREEN + Style.BRIGHT + "|" + "-" * 120 + "|")

        print(Fore.GREEN + Style.BRIGHT + "|" + "↓ " * 25 +"↓ Escolha uma opção ↓" + " ↓" * 24 + "|")
        escolha = input(" " * 53 + Fore.GREEN + "→" + Style.BRIGHT + Fore.LIGHTCYAN_EX )
        if escolha == "1":
            Admin.consultar_lista_diversoes()
        elif escolha == "2":
            Admin.consultar_lista_comodidades()
        elif escolha == "3":
            Admin.consultar_lista_zonas()
        elif escolha == "4":
            Admin.consultar_lista_zonas()
        elif escolha == "5":
            Admin.consultar_diversao_em_detalhe()
        elif escolha == "6":
            Admin.procurar_diversoes()
        elif escolha == "7":
            Admin.procurar_comodidades()
        elif escolha == "8":
            Admin.obter_paragens_comboio_existentes()
        elif escolha == "9":
            Admin.listar_bilhetes_emitidos()
        elif escolha == "10":
            Admin.listar_bilhetes_por_data()
        elif escolha == "11":
            Admin.listar_referencias_bilhetes()

        elif escolha == "0":
            print("Saindo do Menu do Usuário.")
            exit()

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_usuario()
