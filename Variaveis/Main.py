def main():
    nome = input("Digite seu nome: ") 
    idade = int (input("Digite a sua idade: "))
    peso = float (input("Digite o seu peso: "))
    isEmpregado = input("")

    print("o ", nome, " tem ", idade, " anos de idade, pesa ",peso)
    if isEmpregado== "S":
        print("Ele possui um emprego")
    else:
        print("Ele não possui emprego")

    return 0
main()