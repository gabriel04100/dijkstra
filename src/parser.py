from src.graphe import Graphe
import io

def parser_graphe(fichier) -> Graphe:
    graphe = Graphe()

    # Lire le fichier depuis l'objet UploadedFile
    contenu = fichier.read().decode("utf-8")
    
    # Parcourir chaque ligne du fichier
    for ligne in contenu.strip().splitlines():
        s1, s2, poids = ligne.strip().split()
        graphe.ajouter_arc((s1, s2), int(poids))
    
    return graphe

