from operator import itemgetter

def ler_int(s):
    '''
    Solicita ao usuário um input de número inteiro.
    Recebe como parâmetro uma string com a frase que será apresentada
    ao usuário.
    '''
    while True:
        try:
            resp = int(input('{} ' .format(s)))
            return resp
        except:
            print('Digite apenas números.')


def adicionar_na_lista():
    itens = []
    while True:
        codigo = ler_int('Digite o código ou 0 para sair:')
        if codigo == 0:
            return itens
        estoque = ler_int('Digite o número de itens no estoque:')
        estoque_minimo = ler_int('Digite o número mínimo de itens no estoque:')
        item = {'codigo': codigo, 'estoque': estoque, 'minimo': estoque_minimo}
        itens.append(item)
        itens = sorted(itens, key=itemgetter('codigo'))

if __name__ == '__main__':
    itens = adicionar_na_lista()
    for item in itens:
        print(item)

