# Aplicación de búsqueda en Árboles por Ancho
# Distancia y caminos cortos

import networkx as nx

def distancia(G,v,u):
    if v==u:
        return 0
    encontrados={v}
    distancias={v:0}
    procesados=set()
    en_proceso=[v]
    while en_proceso:
        w=en_proceso[0]
        for z in G.neighbors(w):
            if (z not in procesados) and (z not in encontrados):
                encontrados.add(z)
                en_proceso.append(z)
                distancias[z]=distancias[w]+1
                if z==u:
                    return(distancias[z])
        en_proceso.remove(w)
        procesados.add(w)
    return "No están conectados, la gráfica no es conexa."

G = nx.Graph()
G.add_edges_from([(0,3), (1,4), (7,4), (10,2), (2,3), (2,4), (3,4), (6,7), (5,7), (6,8), (8,9), (6,10)])
nx.draw_kamada_kawai(G,with_labels=True, node_color='#bbbb22',node_size=500)

print(distancia(G,1,10))
print(distancia(G,5,0))
print(distancia(G,0,4))