from typing import Dict, Set, Tuple
import heapq

class Graphe:
    def __init__(self):
        self.voisins: Dict[str, Set[str]] = {}  # Les sommets sont des chaînes de caractères, et les voisins sont des ensembles de sommets
        self.poids: Dict[Tuple[str, str], int] = {}  # Les arcs sont des tuples (s1, s2) et les poids sont des entiers

    def ajouter_sommet(self, s: str) -> None:
        if s in self.voisins:
            return
        self.voisins[s] = set()

    def ajouter_arc(self, a: Tuple[str, str], p: int = 1) -> None:
        s1, s2 = a
        self.ajouter_sommet(s1)
        self.ajouter_sommet(s2)
        self.poids[a] = p
        self.voisins[s1].add(s2)

    def supprimer_arc(self, a: Tuple[str, str]) -> None:
        if a not in self.poids:
            return
        del self.poids[a]
        s1, s2 = a
        self.voisins[s1].remove(s2)

    def supprimer_sommet(self, s: str) -> None:
        if s not in self.voisins:
            return
        # Supprimer tous les arcs liés au sommet
        for voisin in set(self.voisins[s]):  # On utilise un set pour éviter de modifier la collection pendant l'itération
            self.supprimer_arc((s, voisin))
        for sommet in self.voisins:
            if s in self.voisins[sommet]:
                self.supprimer_arc((sommet, s))
        del self.voisins[s]

    def sommets(self) -> Set[str]:
        return set(self.voisins)

    def voisins_sortants(self, s: str) -> Set[str]:
        return self.voisins[s]

    def voisins_entrants(self, s: str) -> Set[str]:
        return set(s1 for s1, s2 in self.poids if s2 == s)

    def poids_arc(self, a: Tuple[str, str]) -> int:
        return self.poids[a]

