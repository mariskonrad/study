listaSorteio = []

nome = input("Olá! Qual seu nome? ")
while not nome.isalpha():
    print("Dígitos inválidos. Digite apenas letras.")
    nome = input("Olá! Qual seu nome? ")

while True:
    try:
        valor = float(input("Digite o valor que deseja doar: "))
        break
    except:
        print("Dígitos inválidos. Digite apenas números.")
        valor = float(input("Digite o valor que deseja doar: "))


# pedir input do usuario ref valor a ser doado
# a cada 10,00 armazenar o nome da pessoa na listaSorteio
