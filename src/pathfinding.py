from heapq import heappop, heappush
from src.graphe import Graphe

# Algorithme de Dijkstra avec suivi des étapes
def dijkstra(graphe: Graphe, source: str, cible: str):
    distances = {sommet: float('inf') for sommet in graphe.sommets()}
    predecesseurs = {sommet: None for sommet in graphe.sommets()}
    distances[source] = 0
    
    queue = [(0, source)]
    visited = set()
    parcours = []  # Pour stocker le suivi textuel des étapes
    
    while queue:
        dist, u = heappop(queue)
        
        if u in visited:
            continue
        visited.add(u)
        
        parcours.append(f"Sommet actuel: {u}, Distance: {dist}")
        
        if u == cible:
            break
        
        for v in graphe.voisins_sortants(u):
            if v in visited:
                continue
            
            new_dist = dist + graphe.poids_arc((u, v))
            if new_dist < distances[v]:
                distances[v] = new_dist
                predecesseurs[v] = u
                heappush(queue, (new_dist, v))
                parcours.append(f"    Mise à jour: {v}, Nouvelle distance: {new_dist}, Prédécesseur: {u}")
    
    parcours.append(f"Terminé. Distance finale de {source} à {cible}: {distances[cible]}")
    
    return distances, predecesseurs, parcours



