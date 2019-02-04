#!/bin/env python
#encoding:utf-8
import fonctions

def tab_2D(dim1, dim2):
    a = []
    for i in range(dim1):
        a.append([])
        for j in range(dim2):
            a[i].append(0)
    return a

b = tab_2D(9, 8)
#Aucune action
b[0][0] = 0
b[0][1] = 1
b[0][2] = 2
b[0][3] = 3
b[0][4] = 4
b[0][5] = 5
b[0][6] = 6
b[0][7] = 7

#Victoire
b[1][0] = 6
b[1][1] = 6
b[1][2] = 6
b[1][3] = 6
b[1][4] = 6
b[1][5] = 6
b[1][6] = 6
b[1][7] = 6

#Fin_Partie
b[2][0] = 7
b[2][1] = 7
b[2][2] = 7
b[2][3] = 7
b[2][4] = 7
b[2][5] = 7
b[2][6] = 7
b[2][7] = 7

#Pause
b[3][0] = 0
b[3][1] = 1
b[3][2] = 2
b[3][3] = 3
b[3][4] = 5
b[3][5] = 5
b[3][6] = 6
b[3][7] = 7

#Jouer
b[4][0] = 2
b[4][1] = 0
b[4][2] = 4
b[4][3] = 0
b[4][4] = 4
b[4][5] = 4
b[4][6] = 6
b[4][7] = 7

#Afficher_Score
b[5][0] = 3
b[5][1] = 1
b[5][2] = 2
b[5][3] = 3
b[5][4] = 4
b[5][5] = 5
b[5][6] = 6
b[5][7] = 7

#Sélection_perso
b[6][0] = 2
b[6][1] = 1
b[6][2] = 2
b[6][3] = 3
b[6][4] = 4
b[6][5] = 5
b[6][6] = 6
b[6][7] = 7

#Afficher_Crédits
b[7][0] = 1
b[7][1] = 1
b[7][2] = 2
b[7][3] = 3
b[7][4] = 4
b[7][5] = 5
b[7][6] = 6
b[7][7] = 7

#Sélection_menu
b[8][0] = 0
b[8][1] = 0
b[8][2] = 0
b[8][3] = 3
b[8][4] = 4
b[8][5] = 0
b[8][6] = 0
b[8][7] = 0

def gestion(etat,action):
    nouvel_etat=b[action][etat]
    print "action=", action, "etat=", etat
    if nouvel_etat == 0:
        fonctions.menu_principal()
    elif nouvel_etat == 1:
        fonctions.credit()
    elif nouvel_etat == 2:
        fonctions.selection_personnage
    elif nouvel_etat == 3:
        fonctions.meilleurs_scores()
    elif nouvel_etat == 4:
        fonctions.jeu()
    elif nouvel_etat == 5:
        fonctions.pause()
    elif nouvel_etat == 6:
        fonctions.gagne()
    elif nouvel_etat == 7:
        fonctions.game_over()

    return nouvel_etat

# etat et action (ints) à définir dans le ficher de test :)
