
import networkx as nx
import matplotlib.pyplot as plt

def gerar_grafo():
    G = nx.Graph()

    edges = [
        ("Restaurante","A",2),
        ("Restaurante","B",4),
        ("A","C",1),
        ("B","C",3),
        ("C","D",2)
    ]

    for u,v,w in edges:
        G.add_edge(u,v,weight=w)

    pos = nx.spring_layout(G)
    nx.draw(G,pos,with_labels=True)
    labels = nx.get_edge_attributes(G,'weight')
    nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)

    plt.savefig("outputs/grafo.png")
    plt.close()

    return G
