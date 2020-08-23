
# A ideia do algoritmo é ajudar o usuario a escolher um restaurante que o atenda mais rapido,
# para isso usamos o algoritimo de dijkstra para ver qual restaurante tem o menor caminho
# até a casa do cliente e com isso podemos recomendar qual chegarar mais rapido.

# Criação do algorítimo de Dijkstra 
def dijkstra(grafo,inicio,fim):
    menor_distancia = {}
    antecessor = {}
    naoVisitados = grafo
    infinito = 9999999
    caminho = []
    for noh in naoVisitados:
        menor_distancia[noh] = infinito
    menor_distancia[inicio] = 0
 
# Verificando se o nó ja foi visitado
    while naoVisitados:
        minNoh = None
        for noh in naoVisitados:
            if minNoh is None:
                minNoh = noh
            elif menor_distancia[noh] < menor_distancia[minNoh]:
                minNoh = noh
 
        for nohFilho, peso in grafo[minNoh].items():
            if peso + menor_distancia[minNoh] < menor_distancia[nohFilho]:
                menor_distancia[nohFilho] = peso + menor_distancia[minNoh]
                antecessor[nohFilho] = minNoh
        naoVisitados.pop(minNoh)
 # Caminhando pelo grafo
    nohAtual = fim
    while nohAtual != inicio:
        try:
            caminho.insert(0,nohAtual)
            nohAtual = antecessor[nohAtual]
        except KeyError:
            print('Rua não alcançável')
            break

    caminho.insert(0,inicio)
    if menor_distancia[fim] != infinito:
        return menor_distancia[fim]
        

grafo = {'a':{'b':10,'c':3},
         'b':{'c':1,'d':2},
         'c':{'b':4,'d':8,
         'e':2},'d':{'e':7},
         'e':{'d':9}}



#Classe usada para cadastrar representar um  restaurante 
class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco



restauranteA = Restaurante("Robinho", "b")
restauranteB = Restaurante("Subway", "a")

restaurantes = [restauranteA, restauranteB]
distancias = []

# Main
while 1:
    print("Bem vindo ao Dijk-Entregas \n")
    print("Escolha uma opção: ")
    print("1-Novo pedido")
    print("2-Cadastro de restaurante")
    print("3-Para execução")
    opcao = input()


    if opcao == "1":
        ruaDeEntrega = input("Qual Endereço de entrega(Somente rua): ")
        for restaurante in restaurantes:
           distancias.append(dijkstra(grafo, ruaDeEntrega, restaurante.endereco))

        posicaoMenor = distancias.index(min(distancias))

        print("A sua comida chegarar mais rapido se optar pela restaurante: " + restaurantes[posicaoMenor].nome)

        
    elif opcao == "2":
        nomeRestaurante = input("Qual nome do Restaurante: ")
        enderecoRestaurante = input("Qual endereço do Restaurante: ")

        restaurante = Restaurante(nomeRestaurante, enderecoRestaurante)
        restaurantes.append(restaurante)
    elif opcao == "3":
        break













