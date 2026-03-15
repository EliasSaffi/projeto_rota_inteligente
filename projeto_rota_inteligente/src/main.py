
from graph_generator import gerar_grafo
from clustering import cluster_entregas
from visualization import plot_clusters, plot_mapa
from astar import astar

def heuristic(a,b):
    return 1

print("Gerando grafo...")
G = gerar_grafo()

graph = {
    'Restaurante':[('A',2),('B',4)],
    'A':[('Restaurante',2),('C',1)],
    'B':[('Restaurante',4),('C',3)],
    'C':[('A',1),('B',3),('D',2)],
    'D':[('C',2)]
}

print("Calculando melhor rota...")
path = astar(graph,'Restaurante','D',heuristic)
print("Melhor rota:",path)

print("Agrupando entregas...")
df = cluster_entregas("data/entregas.csv",3)

print("Gerando visualizações...")
plot_clusters(df)
plot_mapa(df)

print("Arquivos gerados em /outputs")
