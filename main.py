import random
import sys

"""
Projeto finalizado
"""


# classe produto
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        self.quantidade = 0

    # função que é chamado como por exemplo eu comprei duas camisas então seria o preço da camisa vezes a quantidade dela mesma
    def calcular_preco_total(self):
        return self.preco * self.quantidade


# classe camisa
class Camisa(Produto):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self.tamanho = tamanho

    # em cada classe vai ter uma função que gera numeros aletórios com seus respectivos multiplos
    def gera_aleatorio(self):
        numero_1 = random.randint(100, 999) * 5
        numero_2 = random.randint(100, 999) * 5
        numero_3 = random.randint(100, 999) * 5
        num_completo = f"({numero_1},{numero_2},{numero_3})"

        # retorna um dicionario com as especialidades do produto
        return {"id": num_completo, "preco": self.preco, "tamanho": self.tamanho}


class Caneca(Produto):
    def __init__(self, nome, preco, capacidade_litros):
        super().__init__(nome, preco)
        self.capacidade_litros = capacidade_litros

    def gera_aleatorio(self):
        numero_1 = random.randint(100, 999) * 3
        numero_2 = random.randint(100, 999) * 3
        numero_3 = random.randint(100, 999) * 3
        num_completo = f"({numero_1},{numero_2},{numero_3})"

        # mesma coisa que acontece na outra classe
        return {
            "id": num_completo,
            "preco": self.preco,
            "capacidade_litros": self.capacidade_litros,
        }


class Quadrinho(Produto):
    def __init__(self, nome, preco, autor, editora):
        super().__init__(nome, preco)
        self.autor = autor
        self.editora = editora

    def gera_aleatorio(self):
        numero_1 = random.randint(100, 999) * 7
        numero_2 = random.randint(100, 999) * 7
        numero_3 = random.randint(100, 999) * 7
        num_completo = f"({numero_1},{numero_2},{numero_3})"

        # denovo
        return {
            "id": num_completo,
            "preco": self.preco,
            "autor": self.autor,
            "editora": self.editora,
        }


# classe que vai ser o carrinho de compras
class Carrinho:
    def __init__(self):
        # cria uma dic vazia de produtos
        self.produtos = {}

    # funçao que adciona o produto na dic
    def adicionar_produto(self, produto, quantidade):
        # soma por exemplo a quantidade de produto que tem na classe Produto la em cima que seria 0 mais 5 por exemplo...
        produto.quantidade += quantidade

        # aqui verifica se o produto já tem no dicionario mais como não tem, criar um valor dentro do dic e cria uma lista dentro
        if produto not in self.produtos:
            self.produtos[produto] = []

        # aqui só vai rodar o loop conforme for a quantidade do produto em questão, e vai adicionar as especificações do produto na lista
        # exemplo de quando se chama a função gera_aleatório():
        # return {"id": num_completo, "preco": self.preco,"autor": self.autor,"editora": self.editora,}
        for _ in range(quantidade):
            self.produtos[produto].append(produto.gera_aleatorio())

        # aqui fuciona a lógica das promoções
        if produto.nome == "Camisa Legal" and produto.quantidade % 4 == 0:
            quantidade = produto.quantidade // 4
            # instacia um novo produto com outro nome e sem preço
            caneca_promocao = Camisa(
                "Ganhou um brinde Caneca Geek (Promoção da camisa", 00.00, 0.5
            )
            # e adciona no carrinho é claro
            carrinho.adicionar_produto(caneca_promocao, quantidade)

        # mesma coisa do código acima
        elif produto.nome == "Quadrinho Incrível" and produto.quantidade % 5 == 0:
            quantidade = produto.quantidade // 5
            # mesma coisa denovo
            quadrinho_promocao = Quadrinho(
                "Ganhou um Quadrinho Incrível free (Promoção Quadrinho)",
                00.00,
                "Autor yyy-xxx",
                "Editora yyy-xxx",
            )
            carrinho.adicionar_produto(quadrinho_promocao, quantidade)

    # aqui tanto imprime os produtos como também calcula o preço total
    def imprimir_nota_fiscal(self):
        total = 0
        for produto, detalhes in self.produtos.items():
            total += produto.calcular_preco_total()

            print(
                f"{produto.nome} - {produto.quantidade} unidades - R${produto.calcular_preco_total():.2f}"
            )

            for detalhe in detalhes:
                print(detalhe)

        print(f"Total da compra: R${total:.2f}")


# Instanciando as classes

camisa = Camisa("Camisa Legal", 20, "M")
caneca = Caneca("Caneca Geek", 10, 0.5)
quadrinho = Quadrinho("Quadrinho Incrível", 5.50, "Autor yyy-xxx", "Editora yyy-xxx")
carrinho = Carrinho()

print(
    """
      
Seja Bem-Vindo a minha loja virtual!!
      
"""
)

try:
    s_n_camisa = input("Você irá querer camisa? [SIM/NAO]\n").upper()
    if s_n_camisa == "SIM":
        try:
            quantidade_camisa = int(input("Você irá querer quantas camisas? "))
            carrinho.adicionar_produto(camisa, quantidade_camisa)
        except ValueError:
            raise ValueError("Selecione a quantidade certa da Camisa")

    elif s_n_camisa != "NAO":
        raise ValueError

except ValueError as ve:
    print("Sua compra deu erro. Tente novamente.")
    sys.exit()

try:
    s_n_caneca = input("Você irá querer a caneca? [SIM/NAO]\n").upper()
    if s_n_caneca == "SIM":
        try:
            quantidade_caneca = int(input("Você irá querer quantos canecos? "))
            carrinho.adicionar_produto(caneca, quantidade_caneca)
        except ValueError:
            raise ValueError

    elif s_n_caneca != "NAO":
        raise ValueError("Você não respondeu corretamente\nERRORR")

except ValueError as ve:
    print("Sua compra deu erro. Tente novamente.")
    sys.exit()

try:
    s_n_quadrinho = input("Você irá querer o quadrinho? [SIM/NAO]\n").upper()
    if s_n_quadrinho == "SIM":
        try:
            quantidade_quadrinho = int(input("Você irá querer quantos quadrinhos? "))
            carrinho.adicionar_produto(quadrinho, quantidade_quadrinho)
        except ValueError:
            raise ValueError

    elif s_n_quadrinho != "NAO":
        raise ValueError("Você não respondeu corretamente\nERRORR")

except ValueError as ve:
    print("Sua compra deu erro. Tente novamente.")
    sys.exit()

carrinho.imprimir_nota_fiscal()
