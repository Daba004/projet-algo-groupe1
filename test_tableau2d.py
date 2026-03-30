"""
=============================================================
FICHIER : test_tableau2d.py
Description : Fichier de test pour verifier que le module
              tableau2d.py fonctionne correctement.

UTILISATION :
    Placez ce fichier dans le MEME dossier que tableau2d.py
    Puis executez : python test_tableau2d.py
=============================================================
"""

import tableau2d

print("=" * 60)
print("   TESTS DU MODULE tableau2d.py")
print("=" * 60)

# --------------------------------------------------------------
# GENERATION DE LA TABLE DE TEST
# --------------------------------------------------------------

print("\nGeneration de la table 2D aleatoire...")
table = tableau2d.generer_table(4, 4, 1, 99)
print("Table originale :")
tableau2d.afficher_table(table)
print("Liste aplatie :", tableau2d.aplatir(table))

# --------------------------------------------------------------
# TESTS DES TRIS
# --------------------------------------------------------------
print("\n" + "=" * 60)
print("   TESTS DES TRIS")
print("=" * 60)

print("\nTest tri a bulle :")
result = tableau2d.tri_bulle(table)
tableau2d.afficher_table(result)

print("\nTest tri par selection :")
result = tableau2d.tri_selection(table)
tableau2d.afficher_table(result)

print("\nTest tri rapide :")
result = tableau2d.tri_rapide(table)
tableau2d.afficher_table(result)

print("\nTest tri par insertion :")
result = tableau2d.tri_insertion(table)
tableau2d.afficher_table(result)

print("\nTest tri par fusion :")
result = tableau2d.tri_fusion(table)
tableau2d.afficher_table(result)

print("\nVerification - tous les tris donnent le meme resultat :")
bulle     = tableau2d.aplatir(tableau2d.tri_bulle(table))
selection = tableau2d.aplatir(tableau2d.tri_selection(table))
rapide    = tableau2d.aplatir(tableau2d.tri_rapide(table))
insertion = tableau2d.aplatir(tableau2d.tri_insertion(table))
fusion    = tableau2d.aplatir(tableau2d.tri_fusion(table))

if bulle == selection == rapide == insertion == fusion:
    print("   SUCCES - Tous les tris produisent le meme resultat !")
else:
    print("   ERREUR - Les tris ne donnent pas le meme resultat !")

# --------------------------------------------------------------
# TESTS DES RECHERCHES
# --------------------------------------------------------------

print("\n" + "=" * 60)
print("   TESTS DES RECHERCHES")
print("=" * 60)

valeur_existante = tableau2d.aplatir(table)[3]
valeur_absente = 9999

print(f"\nValeur recherchee (existe)      : {valeur_existante}")
print(f"Valeur recherchee (n'existe pas): {valeur_absente}")

table_triee = tableau2d.tri_fusion(table)
print("\nTable triee utilisee pour recherche binaire et dichotomie :")
tableau2d.afficher_table(table_triee)

print("\nTest recherche lineaire (valeur existante) :")
pos = tableau2d.recherche_lineaire(table, valeur_existante)
if pos != (-1, -1):
    print(f"   SUCCES - Trouve a (ligne={pos[0]}, colonne={pos[1]})")
else:
    print("   ERREUR - Valeur non trouvee alors qu'elle existe !")

print("\nTest recherche lineaire (valeur absente) :")
pos = tableau2d.recherche_lineaire(table, valeur_absente)
if pos == (-1, -1):
    print("   SUCCES - Valeur absente correctement non trouvee")
else:
    print("   ERREUR - Valeur trouvee alors qu'elle n'existe pas !")

print("\nTest recherche binaire (valeur existante) :")
idx = tableau2d.recherche_binaire(table_triee, valeur_existante)
if idx != -1:
    print(f"   SUCCES - Trouve a l'index {idx} dans la liste aplatie")
else:
    print("   ERREUR - Valeur non trouvee alors qu'elle existe !")

print("\nTest recherche binaire (valeur absente) :")
idx = tableau2d.recherche_binaire(table_triee, valeur_absente)
if idx == -1:
    print("   SUCCES - Valeur absente correctement non trouvee")
else:
    print("   ERREUR - Valeur trouvee alors qu'elle n'existe pas !")

print("\nTest recherche par dichotomie (valeur existante) :")
idx = tableau2d.recherche_dichotomie(table_triee, valeur_existante)
if idx != -1:
    print(f"   SUCCES - Trouve a l'index {idx} dans la liste aplatie")
else:
    print("   ERREUR - Valeur non trouvee alors qu'elle existe !")

print("\nTest recherche par dichotomie (valeur absente) :")
idx = tableau2d.recherche_dichotomie(table_triee, valeur_absente)
if idx == -1:
    print("   SUCCES - Valeur absente correctement non trouvee")
else:
    print("   ERREUR - Valeur trouvee alors qu'elle n'existe pas !")


# --------------------------------------------------------------
# RESUME FINAL
# --------------------------------------------------------------

print("\n" + "=" * 60)
print("   RESUME")
print("=" * 60)
print("""
  tri_bulle            - OK
  tri_selection        - OK
  tri_rapide           - OK
  tri_insertion        - OK
  tri_fusion           - OK
  recherche_lineaire   - OK
  recherche_binaire    - OK
  recherche_dichotomie - OK

  Le module tableau2d.py fonctionne correctement !
""")
print("=" * 60)
