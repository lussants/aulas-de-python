from Div import div
from Mult import mult 
from Soma import soma
from Sub import sub

def main():


    num1 = int (input("Digite o primeiro número: "))
    num2 = int (input("Digite o seguno número: "))

    print("A soma de ", num1, " + ", num2, " = ", soma(num1, num2))
    print("A subtração de ", num1, " - ", num2, " = ", sub(num1, num2))
    print("A multiplicação de ", num1, " * ", num2, " = ", mult(num1, num2))
    print("A divisão de ", num1, " / ", num2, " = ", soma(num1, num2))
    return 0
main()