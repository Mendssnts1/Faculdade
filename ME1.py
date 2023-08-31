'''Faça um programa que calcula o preço total da conta de um cliente. Este programa deve
receber via input um valor n, que representa o número de itens do pedido dele. Cada item tem
uma quantidade e um preço associado, logo deve-se ler n itens, cada um com uma variável de
preço e quantidade, que multiplicadas geram o subtotal do item, Ao final, a conta deve ser o
somatório dos subtotais de itens, imprimindo na tela valor final da conta.
Você deve apresentar duas soluções para o problema: Recursiva e com Loop de Repetição
(while ou for), cada um valendo 1 ponto. Faça uma função para cada uma das soluções.
Durante a solução do problema, os valores de quantidade, preço e subtotal devem ser
armazenados em uma matriz de modo que cada linha represente um item.
O código deve ser enviado com link do Colab ou Github, devendo ser explicado no intervalo
de 5 minutos.'''


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

# pergunta a quantidade de produtos
quantidades_de_produtos = int(input('Quantos produtos você irá levar: '))

def loop_for():
    total = [] 

    # inicia um loop (n = "quantidade_de_produtos") 
    for i in range(quantidades_de_produtos):
        # imprime a tabela dos produtos
        for i in variedade:
            print(i)

        # pergunta qual item ele vai querer
        escolha_do_produto = int(input('Qual produto você irá querer? '))
        
        # verifica se o usuario escolheu entre o intervalo de 0 a 4
        if escolha_do_produto in range(5):
            unidade_produto = int(input(f'Quantas unidades você irá querer do produto {produtos[escolha_do_produto]}? '))
            subtotal = unidade_produto * precos[escolha_do_produto]
            valor.append(subtotal)

        # senão retorna 0 e encerra o loop
        else:
            return 0
            

    valor = f'A sua compra de um total de {sum(total):.2f}'
    return valor

# se a quantidade de produtos escolhido for igual a zero o programa da error
if quantidades_de_produtos == 0:
    print('ERROR iremos reiniciar o programa')

else:
    inicia = loop_for()
    # se a função dentro da variavel "inicia" retornar 0, vai rolar o códigoo abaixo
    if not inicia:
        print('Sua Compra deu erro, Tente novamente!!')

    # senão
    else:
        print(f'{inicia}')
        