import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
        except ValueError:
            pass
        print("Erro: Insira um ano válido.")

def main():
    nome_completo = input("Digite o nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = datetime.datetime.now().year - ano_nascimento
    print(f"\nNome: {nome_completo}\nIdade: {idade} anos")

if __name__ == "__main__":
    main()
