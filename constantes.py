#!/usr/bin/python3
# -*- coding: Utf-8 -*


import pygame
from pygame.locals import *

#on defini repere orthonormal d'unite de pixel=70 pour un carreaux
nombre_sprite_cotex = 20   #nombre carreaux horizontable
nombre_sprite_cotey = 17
taille_sprite = 70         # dimension d'un carreaux ici orthonormal donc 70x70
cote_fenetrex = nombre_sprite_cotex * taille_sprite  #la longeur de la fenetre vaut le nombre de pixel * ça dimmension
cote_fenetrey = nombre_sprite_cotey * taille_sprite
deplacement = 0

titre_fenetre = "Sokobon"           #on charge les images
image_icone = "assets/sucette.png"


image_accueil = "assets/accueil.jpg"
#image_fond = "fond.jpg"
image_fondoption = "assets/fond_option.png"
image_mur = "assets/mur.png"
image_piece = "assets/piece.png"
image_pieceok = "assets/pieceok.png"
image_sucette = "assets/sucette.png"
image_victoire = "assets/victoire.jpg"
image_fond= "assets/fond.jpg"


#pygame.mixer.init(22050, -16, 4096)
#musiquefond = "musiquefond.wav"     #on charge les sons
#bloque = pygame.mixer.Sound("tada.wav")
gagne = "gagne.wav"
musiquejeux = "musiquejeux.wav"




mur='#' #wall                       #on defini les symboles pouvant se trouver dans nos niveau        
piece='$' #box
sucette='0' #goal
joueur='@' #player
pieceok='%' #boxok

joueurxsucette='ù' #P_AND_GOAL  #pas encore utilisé dans nos niveau
vide = "v"    #il faut ne pas avoir de "trou" pour la recherche en ligne avec "\n"
              #et donc completer les "trou" par un caractere, on a donc pas besoin de le definir...







#BONJOUR
#LES INSTRUCTIONS DUPROGRAMME ET DU JEU :
                                

# on essaye de donné des fonctions differente à chaque symbole :
# les mur # sont des obstacle et empeche le personnage de se deplacer car ça position ne peut pas être la même qu'un mur
# les sucette 0 n'agit pas avec le personnage et donc sont "transparent" dans ses deplacements
# les piece $ peuvent être poussé par le personnage si le personnage se deplace en la position d'une piece,
#               mais ne peut pas être poussé si le sprite derriere la piece est "occupé" par un mur ou par une autre piece
# les piece devienent des pieceok si elles ont la même coordonnée qu'une sucette
# le bute est de deplacer toutes les pieces jusqu'aux sucette pour n'obtenir que des pieceok






# QUESTIONS : regardez aussi classes_sokobon2 et sokobon2


# Nous avons recommencé tout notre programme car nous etions bloqué a cause de deplacement..
# depuis ce nouveau programme je n'arrive pas a le lancer (et donc le tester) j'ai cette erreur : 
# Traceback (most recent call last):
#   File "C:\Python27\Nouveau dossier\sokobon2.py", line 3, in <module>
#     from classes_sokobon2 import *
#   File "C:\Python27\Nouveau dossier\classes_sokobon2.py", line 77
# SyntaxError: Non-ASCII character '\xe7' in file C:\Python27\Nouveau dossier\classes_sokobon2.py on line 77, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details



# Je voudrais savoir quelle est aussi la meilleur façon de faire un "retour" ("sokobon2" avec la touche K_r") pour que le personnage retourne en arriere
# indefiniment sans qu'il tourne en rond..



# On voudrais faire un menu à partir d'un dessin qu'on a deja en ajoutant avec pygame : jouer / instruction / meilleur score / niveau etc
# et que l'utilisateur puisse choisir une des proposition avec un systeme de "surlignage" en utilisant que la touche "bas, haut entré"



# On voudrais aussi afficher le nombre de deplacement en temps reel.
# et creer une sauvegarde des meilleurs scores (avec nombre de deplacement le plus faible)
