import random

# Função que recebe o nome do usuário
def get_nome():
    while True:
        nome = input('Digite o nome: ')
        if nome.isalpha():
            return nome
        print('Dígitos inválidos. Digite apenas letras.')

# Função que recebe o valor a ser doado
def get_valor():
    while True:
        try:
            valor = float(input('Digite o valor da doação: '))
            return valor
        except:
            print('Dígitos inválidos. Digite apenas números.')

# Função que armazena os nomes dos doadores e realiza o sorteio
def main():
    # Programa principal
    lista_sorteio = []
    inserir = ''
    while True:
        while (not inserir.isalpha()): # garantir que o input sejam letras
            inserir = input('Deseja cadastrar um nome na lista? (S)im / (N)ão ')
        inserir = inserir.lower()
        if inserir == 'n':
            break
        nome = get_nome()
        valor = get_valor()
        print('{} doou R$ {}' .format(nome, valor))
        vezes_lista = int(valor) // 10
        lista_sorteio += [nome] * vezes_lista
        print(lista_sorteio)

    sortear = ''
    while True:
        while not sortear.isalpha():
            sortear = input('Deseja realizar o sorteio? (S)im / (N)ão ')
        sortear = sortear.lower()
        if sortear == 'n':
            return
        random.shuffle(lista_sorteio)
        sorteado = random.choice(lista_sorteio)
        print('O sorteado foi {}' .format(sorteado))
        return sorteado



if __name__ == '__main__':
    main()
