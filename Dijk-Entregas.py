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
        
# Criação do grafo
grafo = { "Rua carlota kemper" : {"Rua doutor joão silva pena" : 1, "Rua travessa costa pinto" : 2} ,
        "Rua firmino sales" : {"Rua praça doutor augusto silva" : 1, "Rua praça leonardo venerando pereira" : 1},
        "Rua santana" : {"Rua comendador josé esteves" : 4, "Rua desembargador alberto luz" : 1},
        "Rua barão do rio branco" : {"Rua praça doutor augusto silva" : 6, "Rua santana" : 1 },
        "Rua doutor joão silva pena" : {"Rua travessa costa pinto" : 1, "Rua miceno de pádua" : 1},
        "Rua cincinato de paulo" : {"Rua getulio vargas" : 1, "Rua raul soares" : 2},
        "Rua getulio vargas" : {"Rua raul soares" : 1, "Rua comendador josé esteves" : 3},
        "Rua benedito valadares" : {"Rua praça dona josefina" : 2, "Rua praça doutor augusto silva" : 3},
        "Rua praça doutor augusto silva" : {"Rua firmino sales" : 1, "Rua miceno de pádua" : 1},
        "Rua praça leonardo venerando pereira" : {"Rua travessa costa pinto" : 1, "Rua miceno de pádua" : 2},
        "Rua travessa guadalupe" : {"Rua firmino sales" : 1},
        "Rua beco vila helena" : {"Rua comendador josé esteves" : 1},
        "Rua raul soares" : {"Rua benedito valadares" : 3, "Rua dona inacia" : 1},
        "Rua dona inacia" : {"Rua santana" : 2, "Rua comendador josé esteves" : 1},
        "Rua venerando pareira" : {"Rua miceno de pádua" : 1, "Rua carlota kemper" : 1},
        "Rua desembargador alberto luz" : {"Rua santana": 1, "Rua raul soares" : 1},
        "Rua comendador josé esteves" : {"Rua praça doutor augusto silva": 1, "Rua benedito valadares" : 1},
        "Rua travessa costa pinto" : {"Rua praça doutor augusto silva" : 1, "Rua miceno de pádua" : 1} ,
        "Rua bernadino macieira" : {"Rua desembargador alberto luz" : 1},
        "Rua praça dona josefina" : {"Rua raul soares" : 1, "Rua santana" : 1},
        "Rua monsenhor aureliano" : {"Rua miceno de pádua" : 1, "Rua praça doutor augusto silva" : 2},
        "Rua doutor francisco sales" : {"Rua praça leonardo venerando pereira" : 1, "Rua miceno de pádua" : 1},
        "Rua barbosa lima" : {"Rua doutor francisco sales" : 1, "Rua miceno de pádua" : 1},
        "Rua professor azarias ribeiro" : {"Rua doutor francisco sales" : 1, "Rua miceno de pádua" : 1},
        "Rua joão modesto" : {"Rua miceno de pádua" : 1, "Rua francisco andrade" : 1},
        "Rua francisco andrade" : {"Rua doutor francisco sales" : 1, "Rua doutor alvaro botelho" : 1},
        "Rua doutor alvaro botelho" : {"Rua doutor francisco sales" : 1, "Rua francisco de andrade" : 1},
        "Rua francisco de andrade" : {"Rua lourenço menucucci" : 1, "Rua doutor alvaro botelho" : 1},
        "Rua lourenço menucucci" : {"Rua francisco de andrade" : 1, "Rua doutor francisco sales" : 2},
        "Rua miceno de pádua" : {"Rua carlota kemper" : 1, "Rua travessa costa pinto" :1}}



# Classe usada para cadastrar representar um  restaurante 
class Restaurante:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco



restauranteA = Restaurante("Robinho", "Rua miceno de pádua")
restauranteB = Restaurante("Subway", "Rua barão do rio branco")
restauranteC = Restaurante("Restaurante Tropeiro Grill", "Rua praça doutor augusto silva")
restauranteD = Restaurante("Restaurante Manah", "Rua comendador josé esteves")
restauranteE = Restaurante("Restaurante Dallas Bar", "Rua santana")
restauranteF = Restaurante("Restaurante Picles Sabor e Prosa", "Rua doutor alvaro botelho")
restauranteG = Restaurante("Restaurante Sabor Mineiro", "Rua professor azarias ribeiro")
restauranteH = Restaurante("Restaurante Central", "Rua doutor francisco sales")



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




