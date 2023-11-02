# Aplicación de búsqueda en Árboles por Profundidad
# Detección de ciclos

import networkx as nx

def ciclos(G,v0,encontrados=[],padres={},tiempo=0,inicio_p={},fin_p={}):
    tiempo+=1
    inicio_p[v0]=tiempo
    if encontrados==[]:
        encontrados=[v0]
        padres[v0]=None
    for w in G.neighbors(v0):
        if w in encontrados and padres[v0]!=w: # Verificación clave
            ciclo=[w,v0]
            while ciclo[0]!=ciclo[-1]:
                # Por propiedades de búsqueda por anchura, el ciclo
                # se puede encontrar aplicando repetidamente padre.
                ciclo.append(padres[ciclo[-1]]) 
            return ciclo
        if w not in encontrados:
            encontrados.append(w)
            padres[w]=v0
            inner_res=ciclos(G,w,encontrados,padres,tiempo,inicio_p,fin_p)
            if type(inner_res) == list: # i.e. si ya encontramos ciclo.
                return inner_res
            else: # si no encontramos ciclo, seguir recursivamente con búsqueda.
                encontrados,padres,tiempo,inicio_p,fin_p=inner_res
    tiempo+=1
    fin_p[v0]=tiempo
    return encontrados,padres,tiempo,inicio_p,fin_p

G = nx.Graph()
G.add_edges_from([(0,1), (1,3), (1,4), (7,8), (7,3), (10,2), (2,3), (3,4), (5,7), (6,8), (8,9), (6,10)])
ciclo=ciclos(G,1)
print("El ciclo encontrado fue {}".format(ciclo))
nx.draw_kamada_kawai(G,with_labels=True, node_color='#bbbb22',node_size=500)
KKL=nx.kamada_kawai_layout(G)