"""
Module : tri_recherche_2d.py
Auteur : [Ton nom]
Description :
    Ce module fournit des algorithmes de tri et de recherche
    pour des tables à deux dimensions (listes de listes en Python).

    Algorithmes de tri disponibles :
        - Tri à bulles
        - Tri rapide (Quick Sort)
        - Tri par sélection
        - Tri par insertion
        - Tri par fusion (Merge Sort)

    Algorithmes de recherche disponibles :
        - Recherche linéaire
        - Recherche binaire
        - Recherche par dichotomie

    Comment ça marche en interne :
        Tous les algorithmes de tri travaillent en 3 étapes :
            1. Aplatir le tableau 2D en une liste 1D
            2. Trier cette liste 1D
            3. Reconstruire un tableau 2D avec les mêmes dimensions

Exemple d'utilisation :
    import tri_recherche_2d as tr

    table = tr.generer_table(3, 4)
    table_triee = tr.tri_bulle(table)
    resultat = tr.recherche_lineaire(table_triee, 42)
"""

import random
import copy


# ==============================================================================
# UTILITAIRES — fonctions d'aide utilisées par tous les algorithmes
# ==============================================================================

def generer_table(lignes=4, colonnes=5, min_val=0, max_val=100):
    """
    Génère un tableau 2D rempli de valeurs entières aléatoires.

    Paramètres :
        lignes   (int) : nombre de lignes du tableau
        colonnes (int) : nombre de colonnes du tableau
        min_val  (int) : valeur minimale possible
        max_val  (int) : valeur maximale possible

    Retourne :
        Une liste de listes (tableau 2D) remplie aléatoirement.

    Exemple :
        generer_table(2, 3) peut donner :
        [[45, 12, 78],
         [3,  91, 56]]
    """
    # Pour chaque ligne, on génère une liste de valeurs aléatoires
    # random.randint(a, b) retourne un entier entre a et b inclus
    return [
        [random.randint(min_val, max_val) for _ in range(colonnes)]
        for _ in range(lignes)
    ]


def afficher_table(table, titre="Tableau"):
    """
    Affiche un tableau 2D de manière lisible dans la console.

    Paramètres :
        table (list) : le tableau 2D à afficher
        titre (str)  : un titre à afficher au-dessus du tableau
    """
    print(f"\n{'='*40}")
    print(f"  {titre}")
    print(f"{'='*40}")
    for ligne in table:
        # On formate chaque nombre sur 4 caractères pour aligner les colonnes
        print("  " + "  ".join(f"{val:4}" for val in ligne))
    print(f"{'='*40}\n")


def aplatir(table):
    """
    Convertit un tableau 2D en une liste 1D (liste simple).

    C'est l'étape clé avant tout tri : les algorithmes classiques
    travaillent sur des listes à une seule dimension.

    Paramètre :
        table (list) : tableau 2D, ex. [[3, 1], [4, 2]]

    Retourne :
        Une liste 1D, ex. [3, 1, 4, 2]

    Formule :
        Si le tableau a L lignes et C colonnes,
        la liste aplatie a L × C éléments.
    """
    # On parcourt chaque ligne, et pour chaque ligne chaque élément
    liste = []
    for ligne in table:
        for element in ligne:
            liste.append(element)
    return liste


def reconstruire(liste, lignes, colonnes):
    """
    Reconstruit un tableau 2D à partir d'une liste 1D.

    C'est l'opération inverse de aplatir().
    Après avoir trié la liste 1D, on la "recoupe" en lignes.

    Paramètres :
        liste   (list) : la liste 1D triée
        lignes  (int)  : nombre de lignes souhaité
        colonnes (int) : nombre de colonnes souhaité

    Retourne :
        Un tableau 2D reconstruit.

    Formule :
        La ligne i contient les éléments de l'index i*C à (i+1)*C - 1
        où C est le nombre de colonnes.
    """
    # Pour chaque ligne i, on "découpe" la liste 1D en tranches de taille colonnes
    # liste[i*colonnes : (i+1)*colonnes] donne les éléments de la ligne i
    return [
        liste[i * colonnes:(i + 1) * colonnes]
        for i in range(lignes)
    ]


# ==============================================================================
# ALGORITHMES DE TRI
# ==============================================================================

def tri_bulle(table):
    """
    Tri à bulles (Bubble Sort).

    Principe :
        On compare chaque élément avec son voisin de droite.
        Si l'élément de gauche est plus grand, on les échange.
        On répète ce processus jusqu'à ce qu'aucun échange ne soit fait,
        ce qui signifie que la liste est triée.
        Les grandes valeurs "remontent" vers la droite comme des bulles.

    Complexité :
        - Meilleur cas  : O(n)   — liste déjà triée, aucun échange
        - Cas moyen     : O(n²)
        - Pire cas      : O(n²)  — liste triée en sens inverse
        où n = nombre total d'éléments (lignes × colonnes)

    Paramètre :
        table (list) : le tableau 2D à trier

    Retourne :
        Un nouveau tableau 2D trié (le tableau original n'est pas modifié).
    """
    lignes = len(table)
    colonnes = len(table[0])

    # Étape 1 : on aplatit le tableau 2D en liste 1D
    liste = aplatir(table)
    n = len(liste)

    # Étape 2 : algorithme de tri à bulles sur la liste 1D
    for i in range(n):
        # À chaque tour i, les i derniers éléments sont déjà en place
        # On peut donc s'arrêter à n-1-i
        echange_fait = False  # on détecte si un échange a eu lieu

        for j in range(0, n - 1 - i):
            # On compare l'élément j avec son voisin j+1
            if liste[j] > liste[j + 1]:
                # Échange des deux éléments (swap)
                # Formule : liste[j], liste[j+1] = liste[j+1], liste[j]
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
                echange_fait = True

        # Optimisation : si aucun échange n'a été fait dans ce tour,
        # la liste est déjà triée → on arrête
        if not echange_fait:
            break

    # Étape 3 : on reconstruit le tableau 2D avec les mêmes dimensions
    return reconstruire(liste, lignes, colonnes)


def tri_selection(table):
    """
    Tri par sélection (Selection Sort).

    Principe :
        On divise mentalement la liste en deux parties :
            - La partie gauche : déjà triée (commence vide)
            - La partie droite : non triée (commence avec toute la liste)
        À chaque étape, on cherche le minimum dans la partie non triée,
        et on le place à la fin de la partie triée (on l'échange avec
        le premier élément non trié).

    Complexité :
        - Meilleur cas  : O(n²) — on cherche toujours le minimum
        - Cas moyen     : O(n²)
        - Pire cas      : O(n²)
        où n = nombre total d'éléments

    Paramètre :
        table (list) : le tableau 2D à trier

    Retourne :
        Un nouveau tableau 2D trié.
    """
    lignes = len(table)
    colonnes = len(table[0])

    # Étape 1 : aplatir
    liste = aplatir(table)
    n = len(liste)

    # Étape 2 : tri par sélection
    for i in range(n):
        # On suppose que le minimum de la partie non triée est à l'index i
        index_min = i

        # On cherche le vrai minimum dans la partie non triée [i+1 ... n-1]
        for j in range(i + 1, n):
            if liste[j] < liste[index_min]:
                index_min = j  # on a trouvé un nouveau minimum

        # Si le minimum n'est pas déjà à sa place, on l'échange
        # Formule : liste[i], liste[index_min] = liste[index_min], liste[i]
        if index_min != i:
            liste[i], liste[index_min] = liste[index_min], liste[i]

    # Étape 3 : reconstruire le tableau 2D
    return reconstruire(liste, lignes, colonnes)


def tri_insertion(table):
    """
    Tri par insertion (Insertion Sort).

    Principe :
        On construit la liste triée élément par élément,
        comme quand on trie des cartes dans sa main :
            - On prend la carte suivante
            - On la glisse à sa bonne place parmi les cartes déjà triées
            - On répète jusqu'à la dernière carte

    Complexité :
        - Meilleur cas  : O(n)   — liste déjà triée
        - Cas moyen     : O(n²)
        - Pire cas      : O(n²)  — liste triée à l'envers
        où n = nombre total d'éléments

    Paramètre :
        table (list) : le tableau 2D à trier

    Retourne :
        Un nouveau tableau 2D trié.
    """
    lignes = len(table)
    colonnes = len(table[0])

    # Étape 1 : aplatir
    liste = aplatir(table)
    n = len(liste)

    # Étape 2 : tri par insertion
    # On commence à l'index 1 car un seul élément est toujours trié
    for i in range(1, n):
        # On prend l'élément courant (la "carte" à insérer)
        cle = liste[i]

        # On remonte dans la partie triée tant qu'on trouve des éléments
        # plus grands que notre clé
        j = i - 1
        while j >= 0 and liste[j] > cle:
            # On décale l'élément d'une position vers la droite
            liste[j + 1] = liste[j]
            j -= 1

        # On place la clé à sa bonne position
        # Formule : liste[j+1] = cle
        liste[j + 1] = cle

    # Étape 3 : reconstruire le tableau 2D
    return reconstruire(liste, lignes, colonnes)


def tri_rapide(table):
    """
    Tri rapide (Quick Sort).

    Principe :
        C'est un algorithme "diviser pour régner" :
            1. On choisit un élément appelé "pivot" (ici le dernier)
            2. On partitionne la liste en deux parties :
                - Les éléments plus petits que le pivot (à gauche)
                - Les éléments plus grands que le pivot (à droite)
            3. On applique récursivement le même processus
               sur chaque partie
        Au final, toutes les parties s'assemblent en une liste triée.

    Complexité :
        - Meilleur cas  : O(n log n) — pivot toujours au milieu
        - Cas moyen     : O(n log n)
        - Pire cas      : O(n²)     — liste déjà triée, pivot toujours le plus grand
        où n = nombre total d'éléments

    Paramètre :
        table (list) : le tableau 2D à trier

    Retourne :
        Un nouveau tableau 2D trié.
    """
    lignes = len(table)
    colonnes = len(table[0])

    # Étape 1 : aplatir
    liste = aplatir(table)

    # Étape 2 : tri rapide (on appelle la fonction récursive interne)
    liste_triee = _quick_sort_recursif(liste)

    # Étape 3 : reconstruire le tableau 2D
    return reconstruire(liste_triee, lignes, colonnes)


def _quick_sort_recursif(liste):
    """
    Fonction interne récursive pour le tri rapide.
    (Le underscore _ indique que cette fonction est "privée" au module)

    Paramètre :
        liste (list) : sous-liste à trier

    Retourne :
        La sous-liste triée.
    """
    # Cas de base : une liste vide ou un seul élément est déjà triée
    if len(liste) <= 1:
        return liste

    # On choisit le pivot : ici le dernier élément de la liste
    pivot = liste[-1]

    # On sépare les éléments en trois groupes :
    # - gauche  : éléments strictement inférieurs au pivot
    # - milieu  : éléments égaux au pivot (pour gérer les doublons)
    # - droite  : éléments strictement supérieurs au pivot
    gauche = [x for x in liste[:-1] if x < pivot]
    milieu = [x for x in liste if x == pivot]
    droite = [x for x in liste[:-1] if x > pivot]

    # On trie récursivement gauche et droite, puis on assemble
    # Formule : tri_rapide(L) = tri_rapide(gauche) + [pivot] + tri_rapide(droite)
    return _quick_sort_recursif(gauche) + milieu + _quick_sort_recursif(droite)


def tri_fusion(table):
    """
    Tri par fusion (Merge Sort).

    Principe :
        Autre algorithme "diviser pour régner" :
            1. On divise la liste en deux moitiés égales
            2. On trie récursivement chaque moitié
            3. On fusionne (merge) les deux moitiés triées en une seule liste triée
        La fusion est l'opération clé : on compare les premiers éléments
        des deux moitiés et on prend le plus petit.

    Complexité :
        - Meilleur cas  : O(n log n)
        - Cas moyen     : O(n log n)
        - Pire cas      : O(n log n) — toujours le même, très stable
        où n = nombre total d'éléments

    Paramètre :
        table (list) : le tableau 2D à trier

    Retourne :
        Un nouveau tableau 2D trié.
    """
    lignes = len(table)
    colonnes = len(table[0])

    # Étape 1 : aplatir
    liste = aplatir(table)

    # Étape 2 : tri par fusion (fonction récursive interne)
    liste_triee = _merge_sort_recursif(liste)

    # Étape 3 : reconstruire le tableau 2D
    return reconstruire(liste_triee, lignes, colonnes)


def _merge_sort_recursif(liste):
    """
    Fonction interne récursive pour le tri par fusion.

    Paramètre :
        liste (list) : sous-liste à trier

    Retourne :
        La sous-liste triée.
    """
    # Cas de base : une liste d'un seul élément est déjà triée
    if len(liste) <= 1:
        return liste

    # On trouve le milieu de la liste
    # Formule : milieu = len(liste) // 2  (division entière)
    milieu = len(liste) // 2

    # On divise en deux moitiés
    gauche = liste[:milieu]
    droite = liste[milieu:]

    # On trie chaque moitié récursivement
    gauche = _merge_sort_recursif(gauche)
    droite = _merge_sort_recursif(droite)

    # On fusionne les deux moitiés triées
    return _fusionner(gauche, droite)


def _fusionner(gauche, droite):
    """
    Fusionne deux listes triées en une seule liste triée.

    Principe :
        On compare le premier élément de chaque liste.
        On prend le plus petit et on avance dans cette liste.
        On répète jusqu'à épuisement d'une des deux listes,
        puis on ajoute le reste de l'autre.

    Paramètres :
        gauche (list) : première liste triée
        droite (list) : deuxième liste triée

    Retourne :
        Une liste fusionnée et triée.
    """
    resultat = []
    i = 0  # index pour parcourir gauche
    j = 0  # index pour parcourir droite

    # Tant qu'il reste des éléments dans les deux listes
    while i < len(gauche) and j < len(droite):
        if gauche[i] <= droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # On ajoute les éléments restants (une des deux listes est épuisée)
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat


# ==============================================================================
# ALGORITHMES DE RECHERCHE
# ==============================================================================

def recherche_lineaire(table, valeur):
    """
    Recherche linéaire (Linear Search).

    Principe :
        On parcourt chaque élément du tableau un par un,
        de gauche à droite, ligne par ligne.
        On s'arrête dès qu'on trouve la valeur cherchée,
        ou quand on a tout parcouru sans la trouver.

        Aucune condition préalable : le tableau n'a pas besoin d'être trié.

    Complexité :
        - Meilleur cas  : O(1)   — valeur en première position
        - Cas moyen     : O(n/2) ≈ O(n)
        - Pire cas      : O(n)   — valeur absente ou en dernière position
        où n = nombre total d'éléments

    Paramètres :
        table  (list) : le tableau 2D dans lequel chercher
        valeur (int)  : la valeur à chercher

    Retourne :
        Un tuple (ligne, colonne) si la valeur est trouvée,
        ou None si elle n'existe pas dans le tableau.
    """
    # On parcourt chaque ligne avec son index i
    for i, ligne in enumerate(table):
        # On parcourt chaque élément de la ligne avec son index j
        for j, element in enumerate(ligne):
            if element == valeur:
                # Valeur trouvée ! On retourne sa position
                return (i, j)

    # Si on arrive ici, la valeur n'a pas été trouvée
    return None


def recherche_binaire(table, valeur):
    """
    Recherche binaire (Binary Search).

    Principe :
        ⚠️ Le tableau doit être TRIÉ avant d'utiliser cette fonction.

        On aplatit le tableau en liste 1D triée, puis :
            1. On définit deux bornes : gauche (début) et droite (fin)
            2. On calcule le milieu : milieu = (gauche + droite) // 2
            3. Si liste[milieu] == valeur → trouvé !
            4. Si liste[milieu] < valeur  → on cherche dans la moitié droite
            5. Si liste[milieu] > valeur  → on cherche dans la moitié gauche
            6. On répète jusqu'à trouver ou jusqu'à ce que gauche > droite

        C'est comme chercher un mot dans un dictionnaire :
        on ouvre au milieu, on voit si on est avant ou après, etc.

    Complexité :
        - Meilleur cas  : O(1)      — valeur exactement au milieu
        - Cas moyen     : O(log n)
        - Pire cas      : O(log n)  — bien meilleur que la recherche linéaire !
        où n = nombre total d'éléments
        Formule : à chaque étape, on divise l'espace de recherche par 2

    Paramètres :
        table  (list) : le tableau 2D TRIÉ dans lequel chercher
        valeur (int)  : la valeur à chercher

    Retourne :
        Un tuple (ligne, colonne) si trouvé, ou None sinon.
    """
    colonnes = len(table[0])

    # On aplatit le tableau trié en liste 1D
    liste = aplatir(table)
    n = len(liste)

    # On initialise les bornes de recherche
    gauche = 0
    droite = n - 1

    while gauche <= droite:
        # On calcule l'index du milieu
        # Formule : milieu = (gauche + droite) // 2
        milieu = (gauche + droite) // 2

        if liste[milieu] == valeur:
            # Valeur trouvée ! On convertit l'index 1D en position (ligne, colonne)
            # Formule :
            #   ligne   = milieu // colonnes
            #   colonne = milieu %  colonnes
            ligne = milieu // colonnes
            colonne = milieu % colonnes
            return (ligne, colonne)

        elif liste[milieu] < valeur:
            # La valeur est dans la moitié droite → on déplace la borne gauche
            gauche = milieu + 1

        else:
            # La valeur est dans la moitié gauche → on déplace la borne droite
            droite = milieu - 1

    # La valeur n'a pas été trouvée
    return None


def recherche_dichotomie(table, valeur):
    """
    Recherche par dichotomie sur les lignes du tableau.

    Principe :
        ⚠️ Le tableau doit être TRIÉ avant d'utiliser cette fonction.

        Contrairement à la recherche binaire qui travaille sur la liste aplatie,
        ici on travaille directement sur le tableau 2D :

            1. On détermine la ligne candidate grâce à une dichotomie sur les lignes :
               on compare la valeur avec le premier et dernier élément de chaque ligne
               pour savoir dans quelle ligne elle pourrait se trouver.
            2. Une fois la ligne trouvée, on fait une recherche binaire sur cette ligne.

        La dichotomie signifie "couper en deux" : à chaque étape,
        on élimine la moitié des lignes.

    Complexité :
        - Recherche de la ligne  : O(log L)  où L = nombre de lignes
        - Recherche dans la ligne: O(log C)  où C = nombre de colonnes
        - Total                  : O(log L + log C) = O(log(L×C)) = O(log n)
        où n = nombre total d'éléments

    Paramètres :
        table  (list) : le tableau 2D TRIÉ dans lequel chercher
        valeur (int)  : la valeur à chercher

    Retourne :
        Un tuple (ligne, colonne) si trouvé, ou None sinon.
    """
    lignes = len(table)

    # Étape 1 : dichotomie pour trouver la ligne candidate
    haut = 0
    bas = lignes - 1

    while haut <= bas:
        # On prend la ligne du milieu
        # Formule : milieu = (haut + bas) // 2
        milieu = (haut + bas) // 2
        ligne_milieu = table[milieu]

        # Valeur minimale et maximale de cette ligne
        min_ligne = ligne_milieu[0]
        max_ligne = ligne_milieu[-1]

        if min_ligne <= valeur <= max_ligne:
            # La valeur est dans cette ligne → on fait une recherche binaire dessus
            index = _recherche_binaire_1d(ligne_milieu, valeur)
            if index is not None:
                return (milieu, index)
            else:
                return None  # La valeur n'existe pas dans le tableau

        elif valeur < min_ligne:
            # La valeur est avant cette ligne → on cherche dans les lignes du haut
            bas = milieu - 1

        else:
            # La valeur est après cette ligne → on cherche dans les lignes du bas
            haut = milieu + 1

    # La valeur n'a pas été trouvée
    return None


def _recherche_binaire_1d(liste, valeur):
    """
    Fonction interne : recherche binaire sur une liste 1D triée.

    Paramètres :
        liste  (list) : liste 1D triée
        valeur (int)  : valeur à chercher

    Retourne :
        L'index de la valeur dans la liste, ou None si absente.
    """
    gauche = 0
    droite = len(liste) - 1

    while gauche <= droite:
        milieu = (gauche + droite) // 2

        if liste[milieu] == valeur:
            return milieu
        elif liste[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1

    return None
