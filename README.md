# Dijkstra_entregas
Trabalho final da matéria de Algoritmos em Grafos


# Motivação
A ideia do algoritmo é ajudar o usuario a escolher um restaurante que o atenda mais rapido,
gerenciar e recomendar que o usuario faça pedido em restaurantes que tenha uma rota mais curta
assim tendo uma otmização ns tempo de entrega.
A ideia principal era otimizar a rota para do restaurante para atender melhor seus clientes,
mais devido a falta de tempo e desistencia de membro do grupo fizemos algo mais simples.


# Definição e algoritmo 
Para implementação usamos o algoritmo dijkstra para escolher a menor distancia da rua do restaurante
até a rua do cliente e depois vemos qual restaurante consegue atender em menor tempo. 

Nosso grafo é modelado da seguinte forma:

```bash
     grafo = { "Rua carlota kemper" : {"Rua doutor joão silva pena" : 1, "Rua travessa costa pinto" : 2} 
        "Rua benedito valadares" : { "Rua praça doutor augusto silva " : 3 }
        "Rua firmino sales" : {"Rua praça doutor augusto silva" : 1, "Rua praça leonardo venerando pereira" : 1}
        "Rua santana" : {"Rua comendador josé esteves" : 4, "rua desembargador alberto luz" : 1}
        "Rua barão do rio branco" : {"Rua praça doutor augusto silva" : 6, "Rua santana" : 1 }
        "Rua doutor joão silva pena" : {"Rua travessa costa pinto" : 1, "Rua micendo de pádua" : 1}
        "Rua cincinato de paulo" : {"Rua getulio vargas" : 1, "Rua raul soares" : 2}
        "Rua getulio vargas" : {"Rua raul soares" : 1, "Rua comendador josé esteves" : 3}
        "Rua benedito valadares" : {"Rua praça dona josefina" : 2, "Rua praça doutor augusto silva" : 3}
        "Rua praça doutor augusto silva" : {"Rua firmino sales" : 1, "Rua miceno de pádua" : 1}
        "Rua praça leonardo venerando pereira" : {"Rua travessa costa pinto" : 1, "Rua miceno de pádua" : 2}
        "Rua travessa guadalupe" : {"Rua firmino sales" : 1}
        "Rua beco vila helena" : {"Rua comendador josé esteves" : 1}
        "Rua raul soares" : {"Rua benedito valadares" : 3, "Rua dona inacia" : 1}
        "Rua dona inacia" : {"Rua santana" : 2, "Rua comendador josé esteves" : 1}
        "Rua venerando pareira" : {"Rua miceno de pádua" : 1, "Rua carlota kemper" : 1}
        "Rua desembargador alberto luz" : {"Rua santana": 1, "Rua raul soares" : 1}
        "Rua comendador josé esteves" : {"Rua praça doutor augusto silva": 1, "Rua benedito valadares" : 1}
        "Rua travessa costa pinto" : {"Rua praça doutor augusto silva" : 1, "Rua miceno de pádua" : 1} 
        "Rua bernadino macieira" : {"Rua desembargador alberto luz" : 1}
        "Rua praça dona josefina" : {"Rua raul soares" : 1, "Rua santana" : 1}
        "Rua monsenhor aureliano" : {"Rua miceno de pádua" : 1, "Rua praça doutor augusto silva" : 2}
        "Rua doutor francisco sales" : {"Rua praça leonardo venerando pereira" : 1, "Rua miceno de pádua" : 1}
        "Rua barbosa lima" : {"Rua doutor francisco sales" : 1, "Rua miceno de pádua" : 1}
        "Rua professor azarias ribeiro" : {"Rua doutor francisco sales" : 1, "Rua miceno de pádua" : 1}
        "Rua joão modesto" : {"Rua miceno de pádua" : 1, "Rua francisco andrade" : 1}
        "Rua francisco andrade" : {"Rua doutor francisco sales" : 1, "Rua doutor alvaro botelho" : 1}
        "Rua doutor alvaro botelho" : {"Rua doutor francisco sales" : 1, "Rua francisco de andrade" : 1}
        "Rua francisco de andrade" : {"Rua lourenço menucucci" : 1, "Rua doutor alvaro botelho" : 1}
        "Rua lourenço menucucci" : {"Rua francisco de andrade" : 1, "Rua doutor francisco sales" : 2}

}
``` 


Rua : {Ruas interligadas: peso}




