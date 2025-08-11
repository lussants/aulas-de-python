import random
def main():
    notas = [0.0] * 4      
    i = 0   
    media = 0
    while i < 4:

        notas[i] = random.uniform (0, 10)

        media += notas[i]

        i += 1
    media /= 4
    print(f" A media foi {media:,.3}")
          
    if media >= 6:
        print("Aprovado")
    elif media >= 4:
        print("Recuperação")
    else:
        print("Reprovado")
        
        


    return 0
main()