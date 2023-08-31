#varejo de itens
variedade = [
             '[ 0 ] Maçã = $1.5',
             '[ 1 ] Pera = $2',
             '[ 2 ] Melancia = $5',
             '[ 3 ] Banana = $1', 
             '[ 4 ] Abacaxi = $4'
             ]
produtos = ['Maçã','Pera', 'Melancia', 'Banana', 'Abacaxi']
precos = [1.5, 2, 5, 1, 4] 

# Função recursiva para calcular o valor total da conta
def calcular_valor_conta(quantidades_de_produtos):
    # se quantidade de produtos for igual a 0 retorna 0 e a função encerra
    if quantidades_de_produtos == 0:
        return 0
    
    # pergunta a escolha do produto
    escolha_do_produto = int(input('Qual produto você irá querer? '))
    
    # se a escolha do produto for maior ou igual a 0 e menor que "len(produtos) = 'quantidade de valores dentro da lista'"
    if 0 <= escolha_do_produto < len(produtos):
        # pergunta quantas unidade irá querer do produto escolhido
        unidade_produto = int(input(f'Quantas unidades você irá querer do produto {produtos[escolha_do_produto]}? '))
        # armazena o valor da compra do primeiro produto dentro de um subtotal
        subtotal = unidade_produto * precos[escolha_do_produto]
        # retorna o valor do subtotal e o valor da função com o paremetro "-" menos 1, até a quantidade de produto for igual a zero
        return subtotal + calcular_valor_conta(quantidades_de_produtos - 1)
    
    # senão o código se reinicia retornando o valor da função
    else:
        print('Escolha o valor certo')
        return calcular_valor_conta(quantidades_de_produtos)

# pergunta a quantidade de produtos
quantidades_de_produtos = int(input('Quantos produtos você irá levar: '))

# se a quantidade for igual a zero da erro, e manda reiniciar o código
if quantidades_de_produtos == 0:
    print('ERROR iremos reiniciar o programa')

    
else:
    valor_total = calcular_valor_conta(quantidades_de_produtos)
    print(f'A sua compra de um total de {valor_total:.2f}')