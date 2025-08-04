def main():
    idade = int (input("Digite sua idade :"))
    if idade >= 18:
        print("entrada liberada")
    elif idade >= 16 :
    
         acompanhante =  input("Você está acompanhado?")
         if acompanhante == "sim": 
            print("Sim, estou acompanhada")
         else  :
            print("Não estou acompanhada")
    else :
        print("entrada proibida")

        return 0
main()