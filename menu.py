import Admin
import User
from colorama import init, Fore, Style #Dw so serve para costumizar


init(autoreset=True) #A biblioteca ja traz uma cena para resetar automaticamente

def print_menu():
    print(Fore.WHITE + Style.BRIGHT + "+" + "-" * 40 + "+")
    print(Fore.WHITE + Style.BRIGHT + "|" + " " * 40 + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + Fore.GREEN + Style.BRIGHT + "    Bem-vindo ao Parque Divertido!    " + " " * 2 + Fore.WHITE + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + " " * 40 + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + Fore.YELLOW + Style.BRIGHT +"    1. " + Style.NORMAL + "Administração" + " " * 20 + Fore.WHITE + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + Fore.YELLOW + Style.BRIGHT +"    2. " + Style.NORMAL + "Visitante" + " " * 24 + Fore.WHITE + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + Fore.RED + Style.BRIGHT +"    3. " + Style.NORMAL + "Sair" + " " * 29 + Fore.WHITE + "|")
    print(Fore.WHITE + Style.BRIGHT + "|" + " " * 40 + "|")
    print(Fore.WHITE + Style.BRIGHT + "+" + "-" * 40 + "+")

def menu_principal():
    while True:
        print_menu()
        escolha = input(Fore.WHITE + Style.BRIGHT + "|" + "Escolha uma opção: " + Fore.LIGHTCYAN_EX)
        print(Fore.WHITE + Style.BRIGHT + "+" + "-" * 40 + "+")
        if escolha == '1':
            login_admin()
        elif escolha == '2':
            User.menu_visitante()
        elif escolha == '3':
            print(Fore.RED + "Encerrando...")
            break
        else:
            print(Fore.LIGHTRED_EX + "Opção inválida. Tente novamente.")

def login_admin():
    username = input(Fore.WHITE + Style.BRIGHT + "Username: " + Fore.LIGHTCYAN_EX)
    senha = input(Fore.WHITE + Style.BRIGHT + "Password: " + Fore.LIGHTCYAN_EX)

    if autenticar_admin(username, senha):
        Admin.menu_admin()
    else:
        print(Fore.LIGHTRED_EX + "Credenciais inválidas. Tente novamente.")

def autenticar_admin(username, senha):
    return username == "admin" and senha == "senha_admin"

if __name__ == "__main__":
    menu_principal()
