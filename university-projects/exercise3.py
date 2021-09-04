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

# Função padronizada para perguntas ao usuário com resposta (S)im ou (N)ão.
def get_sim_ou_nao(prompt):
    while True:
        opcao = input('{} (S)im ou (N)ão: ' .format(prompt))
        opcao = opcao.lower() # converte o input do usuário para letras minúsculas
        if opcao != 's' and opcao != 'n':
           print('Dígitos inválidos.')
           continue
        return opcao

def inserir_nome_na_lista():
    lista_sorteio = []
    while True:
        inserir = get_sim_ou_nao('Deseja cadastrar um nome na lista?')
        if inserir == 'n':
            return lista_sorteio
        nome = get_nome()
        valor = get_valor()
        print('{} doou R$ {}' .format(nome, valor))
        vezes_lista = int(valor) // 10
        lista_sorteio += [nome] * vezes_lista
        print('Os nomes na lista são {}.' .format(lista_sorteio))

def sortear_nome():
    lista_sorteio = inserir_nome_na_lista()
    if len(lista_sorteio) == 0:
        return
    print("Realizando o sorteio...")
    random.shuffle(lista_sorteio)
    sorteado = random.choice(lista_sorteio)
    print('O sorteado foi {}' .format(sorteado))
    return sorteado

def main():
    # Programa principal
    sortear_nome()




if __name__ == '__main__':
    main()
