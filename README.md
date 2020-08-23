# Dijkstra_entregas
Trabalho final da matéria de Algoritmos em Grafos

Problema do Caminho Mínimo


# Motivação
A ideia do algoritmo é ajudar o usuario a escolher um restaurante que o atenda mais rapido,
gerenciar e recomendar que o usuario faça pedido em restaurantes que tenha uma rota mais curta
assim tendo uma otmização no tempo de entrega.
A ideia principal era otimizar a rota para do restaurante para atender melhor seus clientes,
mais devido a falta de tempo e desistencia de membro do grupo fizemos algo mais simples sem perder a essência.


# Definição formal
Para implementação usamos o algoritmo dijkstra para escolher a menor distancia da rua do restaurante
até a rua do cliente e depois verificamos qual restaurante consegue atender em menor tempo. 
Foi escolhido o algorítimo de Dijkstra pois este algoritmo é capaz de determinar o caminho mínimo,
partindo de um vértice de início para todos os outros vértices do grafo, que neste caso é a casa do cliente.

# Algorítimo
Primeiramente é criado o Dijkstra:
     são definidas as variáveis
     enquanto o nó está em 'nãoVisitados':
          primeiro, ele define o primeiro nó como caminho mínimo
          para: nohFilho ainda não finalizado
               calcula-se o menor caminho entre nohFilho e minNoh
          determina o menor caminho.
     é feita a caminhada pelo grafo até achar o endereço final.
É criada a classe para receber o restaurante.
Main:
     é crada uma mini interface para o cliente
     se opção '1':
          recebe o nome da rua de entrega e entrega o nome do restaurante mais próximo
     se opção '2':
          cadastra um novo restaurante
     se opção '3':
          para sair
fim.

# Instâcia teste
Rua santana : Restaurante Dallas Bar
Rua doutor alvaro botelho : Restaurante Picles Sabor e Prosa

# Forças e fraquezas
Força: oferece uma rapidez e uma facilidade de forma simples
Fraqueza: cobre uma área pequena (centro), melhoraria se conseguissemos abranger a cidade inteira.

# Grafo
Nosso grafo é modelado da seguinte forma:

bash
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
 


Rua : {Ruas interligadas: peso}
