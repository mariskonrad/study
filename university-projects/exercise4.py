from operator import itemgetter

# Função padrão para pedir input para o usuário.
def ler_int(s):
    '''
    Recebe como parâmetro uma string com a frase que será apresentada
    ao usuário e retorna um número inteiro.

    s: string
    '''
    while True:
        try:
            resp = int(input('{} ' .format(s)))
            return resp
        except: # trata erros caso o usuário digite valor inválido que não pode ser retornado como int.
            print('Digite apenas números.')

# Função para adicionar item na lista
def adicionar_na_lista():
    itens = []
    while True:
        # Para encerrar o programa
        codigo = ler_int('Digite o código ou 0 para sair:')
        if codigo == 0:
            return itens
        # Chamar a função ler_int e a atribuir a variável estoque
        estoque = ler_int('Digite o número de itens no estoque:')
        # Chamar a variável ler_int e atribuir o retorno à variável estoque_minimo
        estoque_minimo = ler_int('Digite o número mínimo de itens no estoque:')
        # Criar dicionário e atribuir à variável item
        item = {'codigo': codigo, 'estoque': estoque, 'minimo': estoque_minimo}
        # Adicionar item à lista itens
        itens.append(item)
        # Ordenar a lista
        itens = sorted(itens, key=itemgetter('codigo'))

# Programa principal
if __name__ == '__main__':
    # Chamar a função adicionar_na_lista e atribuir o retorno à variável itens.
    itens = adicionar_na_lista()
    # Imprimir em linhas separadas:
    for item in itens:
        print(item)

