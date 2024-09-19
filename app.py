# app.py
import streamlit as st
from src.parser import parser_graphe
from src.pathfinding import dijkstra
import networkx as nx
import matplotlib.pyplot as plt


# Fonction pour dessiner le graphe avec NetworkX et Matplotlib
def dessiner_graphe(graphe, chemin=None, titre=""):
    G = nx.DiGraph()  # Créer un graphe orienté avec NetworkX
    
    # Ajouter les sommets et les arcs
    for sommet in graphe.sommets():
        G.add_node(sommet)
    
    for (s1, s2), poids in graphe.poids.items():
        G.add_edge(s1, s2, weight=poids)
    
    # Dessiner le graphe
    pos = nx.spring_layout(G)  # Position des nœuds
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(s1, s2): f'{poids}' for (s1, s2), poids in graphe.poids.items()})
    
    # Si un chemin est donné, mettre en évidence ce chemin
    if chemin:
        chemin_edges = [(chemin[i], chemin[i+1]) for i in range(len(chemin)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=chemin_edges, edge_color='r', width=2)
    
    # Afficher le graphe avec Matplotlib
    plt.title(titre)
    plt.show()


# Charger le graphe depuis un fichier texte
st.title("Visualisation de l'algorithme Dijkstra")
uploaded_file = st.file_uploader("Choisir un fichier de graphe", type=["txt"])

if uploaded_file is not None:
    # Passer directement l'objet 'uploaded_file' à la fonction parser_graphe
    graphe = parser_graphe(uploaded_file)
    
    # Sélection des sommets de départ et d'arrivée
    sommets = list(graphe.sommets())
    source = st.selectbox("Sommet de départ", sommets)
    cible = st.selectbox("Sommet d'arrivée", sommets)
    
    
    # Exécution de Dijkstra avec suivi
    distances, predecesseurs, parcours = dijkstra(graphe, source, cible)
    
    # Affichage textuel du parcours
    st.write("Parcours de l'algorithme Dijkstra :")
    for etape in parcours:
        st.text(etape)
    
    # Si un chemin est trouvé, afficher le chemin
    if distances[cible] == float('inf'):
        st.write(f"Pas de chemin trouvé entre {source} et {cible}.")
    else:
        chemin = []
        s = cible
        while s is not None:
            chemin.insert(0, s)
            s = predecesseurs[s]
        
        st.write(f"Chemin trouvé: {' -> '.join(chemin)}")
        st.write(f"Distance totale: {distances[cible]}")
    
    # Afficher le graphe avec le chemin trouvé (si trouvé)
    st.write("Graphe avec le chemin trouvé :")
    fig2, ax2 = plt.subplots()
    dessiner_graphe(graphe, chemin, titre="Graphe avec le chemin trouvé")
    st.pyplot(fig2)



