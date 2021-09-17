import random

# Função que solicita input e retorna o nome do usuário
def get_nome():
    '''
    Pede o do nome do usuário e o retorna em string.
    '''
    while True:
        nome = input('Digite o nome: ')
        if nome.isalpha(): # Testa se o usuário digitou caracteres válidos
            return nome
        print('Dígitos inválidos. Digite apenas letras.')

# Função que solicita input e retorna o valor a ser doado
def get_valor():
    '''
    Pede um valor numérico e o retorna em float.
    '''

    while True:
        try:
            valor = float(input('Digite o valor da doação: '))
            return valor
        except: # trata erros caso o usuário digite valor inválido que não pode ser retornado em float.
            print('Dígitos inválidos. Digite apenas números.')

# Função padronizada para perguntas ao usuário com resposta (S)im ou (N)ão.
def get_sim_ou_nao(prompt):
    '''
    Recebe como parâmetro a mensagem a ser impressa na tela.
    Pede um input "s" ou "n" ao usuário e o retorna.

    prompt: string
    '''
    while True:
        opcao = input('{} (S)im ou (N)ão: ' .format(prompt))
        opcao = opcao.lower() # converte o input do usuário para letras minúsculas
        if opcao != 's' and opcao != 'n':
           print('Dígitos inválidos.')
           continue
        return opcao

# Função para inserir o nome da lista
def inserir_nome_na_lista():
    '''
    Função que adiciona elementos à lista e a retorna.
    '''
    lista_sorteio = []
    while True:
        # Pergunta se o usuário deseja cadastrar nome na lista
        inserir = get_sim_ou_nao('Deseja cadastrar um nome na lista?')
        if inserir == 'n':
            return lista_sorteio
        # Chama a função e atribui o seu retorno à variável "nome".
        nome = get_nome()
        # Chama a função e atribui o seu retorno à variável "valor"
        valor = get_valor()
        print('{} doou R$ {}' .format(nome, valor))
        # Indica quantas vezes o nome da pessoa irá aparecer na lista
        vezes_lista = int(valor) // 10
        #Adiciona o nome da pessoa à lista
        lista_sorteio += [nome] * vezes_lista
        # Imprime a lista
        print('Os nomes na lista são {}.' .format(lista_sorteio))

# Função que realiza o sorteio
def sortear_nome():
    '''
    Realiza o sorteio da lista e retorna o resultado.
    '''
    # Chama a função que insere nomes na lista a atribui o retorno à variável lista_sorteio
    lista_sorteio = inserir_nome_na_lista()
    # Se a lista estiver vazia, retorna.
    if len(lista_sorteio) == 0:
        return
    # Se a lista não estiver vazia, o sorteio é realizado:
    print("Realizando o sorteio...")
    # Embaralha a lista
    random.shuffle(lista_sorteio)
    # Realiza o sorteio e atribui o resultado à variável "sorteado"
    sorteado = random.choice(lista_sorteio)
    # Imprime o resultado na tela e o retorna.
    print('O sorteado foi {}' .format(sorteado))
    return sorteado

def main():
    # Programa principal
    sortear_nome()


if __name__ == '__main__':
    main()
