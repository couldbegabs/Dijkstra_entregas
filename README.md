# Dijkstra_entregas
Trabalho final da matéria de Algoritmos em Grafos


#Motivação
A ideia do algoritmo é ajudar o usuario a escolher um restaurante que o atenda mais rapido,
gerenciar e recomendar que o usuario faça pedido em restaurantes que tenha uma rota mais curta
assim tendo uma otmização ns tempo de entrega.
A ideia principal era otimizar a rota para do restaurante para atender melhor seus clientes,
mais devido a falta de tempo e desistencia de membro do grupo fizemos algo mais simples.


#Definição e algoritmo 
Para implementação usamos o algoritmo dijkstra para escolher a menor distancia da rua do restaurante
até a rua do cliente e depois vemos qual restaurante consegue atender em menor tempo. 

Nosso grafo é modelado da seguinte forma:

```bash
     grafo = { "Rua Carlota Kemper" : {"Rua Dr.João Silva Pena" : 1, "Travessa Costa Pinto" : 2} 
               "Rua Benedito Valadares" : { "RPraça Doutor Augusto Silva " : 3 }}
``` 


Rua : {Ruas interligadas: peso}




