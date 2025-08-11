def main():
    nome = input("Digite seu nome: ")
    i = 0
    espaço = 0 
    for i in range(len(nome)):
        if nome [i] == " ":
            print("Espaço vazio")
            espaço += 1
        else:
            print("", i + 1 - espaço,"° letra do seu nome: ", nome [i])

    print("Seu nome tem ", i + 1 - espaço, "letras")


    return 0
main()