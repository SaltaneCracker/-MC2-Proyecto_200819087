# Este calcula explícitamente uno de los caminos más cortos de v a u

import networkx as nx

G = nx.Graph()
G.add_edges_from([(0,3), (1,4), (7,4), (10,2), (2,3), (2,4), (3,4), (6,7), (5,7), (6,8), (8,9), (6,10)])

def camino_corto(G,v,u):
    if v==u:
        return [u]
    encontrados={v}
    procesados=set()
    padres={v:None}
    en_proceso=[v]
    while en_proceso:
        w=en_proceso[0]
        for z in G.neighbors(w):
            if (z not in procesados) and (z not in encontrados):
                encontrados.add(z)
                en_proceso.append(z)
                padres[z]=w
                if z==u:
                    camino=[z]
                    padre=z
                    while padre!=v:
                        padre=padres[padre]
                        camino=[padre]+camino
                    return camino
        en_proceso.remove(w)
        procesados.add(w)
    return "No están conectados"

nx.draw_kamada_kawai(G,with_labels=True, node_color='#bbbb22',node_size=500)

print(camino_corto(G,1,10))
print(camino_corto(G,5,0))
print(camino_corto(G,0,4))