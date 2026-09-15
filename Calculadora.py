def adicionar(x, y):
    """Adiciona dois números"""
    return x + y

def subtrair(x, y):
    """Subtrai dois números"""
    return x - y

def multiplicar(x, y):
    """Multiplica dois números"""
    return x * y

def dividir(x, y):
    """Divide dois números"""
    if y == 0:
        return "Erro: Divisão por zero"
    return x / y

def potencia(x, y):
    """Calcula a potência"""
    return x ** y

def raiz_quadrada(x):
    """Calcula a raiz quadrada"""
    if x < 0:
        return "Erro: Raiz de número negativo"
    return x ** 0.5

def calculadora():
    """Função principal da calculadora"""
    print("=" * 40)
    print("CALCULADORA COMPARTILHADA")
    print("=" * 40)
    
    while True:
        print("\nOperações disponíveis:")
        print("1. Adição (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (**)")
        print("6. Raiz Quadrada (√)")
        print("0. Sair")
        print("-" * 40)
        
        opcao = input("Escolha uma operação (0-6): ").strip()
        
        if opcao == "0":
            print("Encerrando a calculadora. Até logo!")
            break
        
        if opcao in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == "1":
                    resultado = adicionar(num1, num2)
                    print(f"\n{num1} + {num2} = {resultado}")
                elif opcao == "2":
                    resultado = subtrair(num1, num2)
                    print(f"\n{num1} - {num2} = {resultado}")
                elif opcao == "3":
                    resultado = multiplicar(num1, num2)
                    print(f"\n{num1} * {num2} = {resultado}")
                elif opcao == "4":
                    resultado = dividir(num1, num2)
                    print(f"\n{num1} / {num2} = {resultado}")
                elif opcao == "5":
                    resultado = potencia(num1, num2)
                    print(f"\n{num1} ** {num2} = {resultado}")
            
            except ValueError:
                print("Erro: Digite números válidos!")
        
        elif opcao == "6":
            try:
                num = float(input("Digite o número: "))
                resultado = raiz_quadrada(num)
                print(f"\n√{num} = {resultado}")
            except ValueError:
                print("Erro: Digite um número válido!")
        
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    calculadora()
