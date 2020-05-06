#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from constantes import *



class Niveau:
        def __init__(self, fichier):
            self.fichier = fichier
            self.structure = 0

        def generer(self):
                with open(self.fichier, "r") as fichier:
                        structure_niveau = []
                        for ligne in fichier:
                                ligne_niveau = []
                                for sprite in ligne:
                                        if sprite != '\n':
                                                ligne_niveau.append(sprite)
                                structure_niveau.append(ligne_niveau)
                        self.structure = structure_niveau
                      #  print(structure_niveau)


        def afficher(self, fenetre):
                mur = pygame.image.load(image_mur).convert()
                sucette = pygame.image.load(image_sucette).convert()
                transColor = sucette.get_at((0,0))
                sucette.set_colorkey(transColor)
                piece = pygame.image.load(image_piece).convert()
                transColor = piece.get_at((0,0))
                piece.set_colorkey(transColor)
                #perso = pygame.image.load("bas.jpg").convert_alpha()
                

                num_ligne = 0
                for ligne in self.structure:
                        num_case = 0
                        for sprite in ligne:
                                x = num_case * taille_sprite
                                y = num_ligne * taille_sprite
                                if sprite == '#':
                                        fenetre.blit(mur, (x,y))
                                elif sprite == '0':
                                        fenetre.blit(sucette, (x,y))
                                elif sprite == '$':
                                        fenetre.blit(piece, (x,y))
                                elif sprite == '%':
                                        fenetre.blit(pieceok,(x,y))
                                num_case = num_case + 1
                        num_ligne = num_ligne + 1







class Perso:
        def __init__(self, droite, gauche, haut, bas, niveau, choix):
                
                #self.droite = pygame.image.load(droite).convert()  #on charge les images
                self.droite = pygame.image.load(droite)
                #transColor = self.droite.get_at((0,0))
                #self.droite.set_colorkey(transColor)
                self.gauche = pygame.image.load(gauche)
                #transColor = self.gauche.get_at((0,0))
                #self.gauche.set_colorkey(transColor)
                self.haut = pygame.image.load(haut)
                #transColor = self.haut.get_at((0,0))
                #self.haut.set_colorkey(transColor)
                self.bas = pygame.image.load(bas)
                #transColor = self.bas.get_at((0,0))
                #self.bas.set_colorkey(transColor)
                self.piece = pygame.image.load(image_piece).convert_alpha()
                self.pieceok = pygame.image.load(image_pieceok).convert_alpha()
                self.direction = self.haut                     #skin du personngae avant le 1er deplacement
                self.niveau = niveau
                if choix == 'assets/map1.txt':
                        self.case_x = 7                 #Position du personnage en cases et en pixels
                        self.case_y = 6
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                elif choix == 'assets/map2.txt':
                        self.case_x = 4
                        self.case_y = 2
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                elif choix == 'assets/map3.txt':
                        self.case_x = 1
                        self.case_y = 5
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                elif choix == 'assets/map4.txt':
                        self.case_x = 6
                        self.case_y = 5
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                elif choix == 'assets/map5.txt':
                        self.case_x = 1
                        self.case_y = 6
                        self.x = self.case_x * taille_sprite
                        self.y = self.case_y * taille_sprite
                
                
                
                        
                        
                #self.xpiece = x['$']            #la position en pixel et le nombre de piece est defini dans chaque niveau par "$" puis afficher par "fenetre.blit(piece, (x,y))" (l.39)  
                #self.ypiece = y['$']
                #self.xsucette = x['0']
                #self.ysucette = y['0']
                #self.direction = self.haut       #skin du personngae avant le 1er deplacement
                #self.niveau = niveau


        def deplacer(self, direction):
            deplacement = 0
           #k=0  ce compteur servira plus tard, dans la 2eme methode avec la touche "K_r" dans la page "sokobon2" de python
            #liste = []





            if direction == 'droite':
                                self.direction = self.droite
                                k = 0
                                if self.niveau.structure[self.case_y][self.case_x+1] != '#' :
                                        #on empeche le personnage de se deplacer a ça droite si sur ça droite il y a un mur OU 2pieces collé/aligné horizontalement(sens de deplacement, vers la droite) OU une piece puis un mur collé/aligné horizontalement 
                                        if self.niveau.structure[self.case_y][self.case_x+1] == '$' and (self.niveau.structure[self.case_y][self.case_x+2] == 'v' or self.niveau.structure[self.case_y][self.case_x+2] == '0'):
                                                self.case_x = self.case_x + 1
                                                self.x = self.case_x * taille_sprite
                                                deplacement += 1              # le compteur de deplacement du personnage
                                                self.niveau.structure[self.case_y][self.case_x] = 'v'        
                                                self.niveau.structure[self.case_y][self.case_x+1] = '$'
                                                #if choix == 'map1.txt':
                                                        #if self.niveau.strucure[self.case_y][self.case_x] != '0':
                                                               # fenetre.blit(sucette,(2,7))
                                                               # fenetre.blit(sucette,(7,5))
                                                               # fenetre.blit(sucette,(6,9))
                                                        
                                                
                                                #fenetre.blit(sucette,(2,7))
                                                              #  fenetre.blit(sucette,(7,5))
                                                               # fenetre.blit(sucette,(6,9))
                                                                             
                                                              
                                                        
                                                
                          
                                                        
                                                        
                                                        
                                                #liste.append(droite)
                                        
                                        elif    self.niveau.structure[self.case_y][self.case_x+1] == 'v' or self.niveau.structure[self.case_y][self.case_x+1] == '0':    
                                                self.case_x = self.case_x + 1
                                                self.x = self.case_x * taille_sprite
                                                deplacement += 1             
                                                #liste.append(droite)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$':
                                                       #self.niveau.structure[self.case_y][self.case_x] = 'v'
                                                       #self.niveau.structure[self.case_y][self.case_x+1] = '$'
                                                       #k = 1
                                                #if self.niveau.structure[semf.case_y]
                                                #if [piece_y][piece_x] == [sucette_y][sucette_x]:       #si la coordonnée d'une piece et la même qu'une sucette elle devient une pieceok
                                                 #               piece = pieceok
                                                  #              k = 2
                                                  
                                        #else:
                                         #        bloque.play()          
                                #else:
                                 #       bloque.play()
                
                                 
           
            if direction == 'gauche':
                                self.direction = self.gauche
                                k = 0
                                if self.niveau.structure[self.case_y][self.case_x-1] != '#' :
                                        #on empeche le personnage de se deplacer a ça droite si sur ça droite il y a un mur OU 2pieces collé/aligné horizontalement(sens de deplacement, vers la droite) OU une piece puis un mur collé/aligné horizontalement 
                                        if self.niveau.structure[self.case_y][self.case_x-1] == '$' and (self.niveau.structure[self.case_y][self.case_x-2] == 'v' or self.niveau.structure[self.case_y][self.case_x-2] == '0'):
                                                self.case_x = self.case_x - 1
                                                self.x = self.case_x * taille_sprite
                                                deplacement += 1              # le compteur de deplacement du personnage
                                                self.niveau.structure[self.case_y][self.case_x] = 'v'        
                                                self.niveau.structure[self.case_y][self.case_x-1] = '$'                
                                                #liste.append(gauche)
                                        
                                        elif    self.niveau.structure[self.case_y][self.case_x-1] == 'v' or self.niveau.structure[self.case_y][self.case_x-1] == '0':    
                                                self.case_x = self.case_x - 1
                                                self.x = self.case_x * taille_sprite
                                                deplacement += 1             
                                                #liste.append(gauche)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$':
                                                        #self.niveau.structure[self.case_y][self.case_x] = 'v'
                                                        #self.niveau.structure[self.case_y][self.case_x-1] = '$'
                                                        #k = 1
                                                #if [piece_y][piece_x] == [sucette_y][sucette_x]:       #si la coordonnée d'une piece et la même qu'une sucette elle devient une pieceok
                                                                #piece = pieceok
                                                                #k = 2
            
                                                  
                                      #  else:
                                       #          bloque.play()          
                                #else:
                                 #       bloque.play()
                                                
            if direction == 'bas':
                               
                               self.direction = self.haut
                               k = 0
                               if self.niveau.structure[self.case_y+1][self.case_x] != '#' :
                                        #on empeche le personnage de se deplacer a ça droite si sur ça droite il y a un mur OU 2pieces collé/aligné horizontalement(sens de deplacement, vers la droite) OU une piece puis un mur collé/aligné horizontalement 
                                        if self.niveau.structure[self.case_y+1][self.case_x] == '$' and (self.niveau.structure[self.case_y+2][self.case_x] == 'v' or self.niveau.structure[self.case_y+2][self.case_x] == '0'):
                                                self.case_y = self.case_y + 1
                                                self.y = self.case_y * taille_sprite
                                                deplacement += 1              # le compteur de deplacement du personnage
                                                self.niveau.structure[self.case_y][self.case_x] = 'v'        
                                                self.niveau.structure[self.case_y+1][self.case_x] = '$'                
                                                #liste.append(bas)
                                        
                                        elif    self.niveau.structure[self.case_y + 1][self.case_x] == 'v' or self.niveau.structure[self.case_y + 1][self.case_x] == '0':    
                                                self.case_y = self.case_y + 1
                                                self.y = self.case_y * taille_sprite
                                                deplacement += 1             
                                                #liste.append(bas)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$':
                                                        #self.niveau.structure[self.case_y][self.case_x] = 'v'
                                                        #self.niveau.structure[self.case_y + 1][self.case_x] = '$'
                                                        #k = 1
                                                #if [piece_y][piece_x] == [sucette_y][sucette_x]:       #si la coordonnée d'une piece et la même qu'une sucette elle devient une pieceok
                                                                #piece = pieceok
                                                                #k = 2
            if direction == 'haut':
                               
                               self.direction = self.bas
                               k = 0
                               if self.niveau.structure[self.case_y - 1][self.case_x] != '#' :
                                        #on empeche le personnage de se deplacer a ça droite si sur ça droite il y a un mur OU 2pieces collé/aligné horizontalement(sens de deplacement, vers la droite) OU une piece puis un mur collé/aligné horizontalement 
                                        if self.niveau.structure[self.case_y - 1][self.case_x] == '$' and (self.niveau.structure[self.case_y - 2][self.case_x] == 'v' or self.niveau.structure[self.case_y - 2][self.case_x] == '0'):
                                                self.case_y = self.case_y - 1
                                                self.y = self.case_y * taille_sprite
                                                deplacement += 1              # le compteur de deplacement du personnage
                                                self.niveau.structure[self.case_y][self.case_x] = 'v'        
                                                self.niveau.structure[self.case_y - 1][self.case_x] = '$'                
                                                #liste.append(haut)
                                        
                                        elif    self.niveau.structure[self.case_y - 1][self.case_x] == 'v' or self.niveau.structure[self.case_y - 1][self.case_x] == '0':    
                                                self.case_y = self.case_y - 1
                                                self.y = self.case_y * taille_sprite
                                                deplacement += 1             
                                                #liste.append(haut)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$':
                                                        #self.niveau.structure[self.case_y][self.case_x] = 'v'
                                                        #self.niveau.structure[self.case_y - 1][self.case_x] = '$'
                                                        #k = 1
                                                #if [piece_y][piece_x] == [sucette_y][sucette_x]:       #si la coordonnée d'une piece et la même qu'une sucette elle devient une pieceok
                                                                #piece = pieceok
                                                                #k = 2

            #if direction == 'haut':
                                #self.direction = self.bas
                                #k = 0
                                #if self.niveau.structure[self.case_y-1][self.case_x] != '#' :  
                                        #if self.niveau.structure[self.case_y-1][self.case_x] == '$' and self.niveau.structure[self.case_y-2][self.case_x] != '$' or '#':
                                                #self.case_y = self.case_y-1
                                                #self.y = self.case_y * taille_sprite
                                                #deplacement += 1             
                                                #self.direction = self.bas
                                                #liste.append(haut)
                                        
                                        #elif    sefl.niveau.structure[self.case_y-1][self.case_x] == 'v':    
                                                #self.case_y = self.case_y-1
                                                #self.x = self.case_x * taille_sprite
                                                #deplacement += 1             
                                                #self.direction = self.bas
                                                #liste.append(haut)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$' and ( self.niveau.structure[self.case_y-1][self.case_x] != '$' or self.niveau.strucute[self.case_y-1][self.case_x] != '#'):
                                                        #[piece_y][piece_x] = [piece_y-1][piece_x]
                                                        #k = 1
                                                        #if [piece_y][piece_x] == [sucette_y][sucette_x]:       
                                                                #piece = pieceok
                                                                #k = 2
                                                  
                                       # else:
                                        #         bloque.play()          
                                #else:
                                 #       bloque.play()
                    
                                

            #if direction == 'bas':
                                #k = 0
                                #if self.niveau.structure[self.case_y+1][self.case_x] != '#' :  
                                        #if self.niveau.structure[self.case_y+1][self.case_x] == '$' and self.niveau.structure[self.case_y+2][self.case_x] != '$' or '#':
                                                #self.case_y = self.case_y+1
                                                #self.y = self.case_y * taille_sprite
                                                #deplacement += 1             
                                                #self.direction = self.haut
                                               # liste.append(bas)
                                        
                                        #elif    sefl.niveau.structure[self.case_y+1][self.case_x] == 'v':    
                                                #self.case_x = self.case_x + 1
                                                #self.x = self.case_x * taille_sprite
                                                #deplacement += 1             
                                                #self.direction = self.haut
                                                #liste.append(bas)
                                                
                                                #if self.niveau.structure[self.case_y][self.case_x] == '$' and ( self.niveau.structure[self.case_y+1][self.case_x] != '$' or self.niveau.structure[self.case_y+1][self.case_x] != '#'):
                                                        #[piece_y][piece_x] = [piece_y+1][piece_x]
                                                        #k = 1
                                                        #if [piece_y][piece_x] == [sucette_y][sucette_x]:       
                                                                #piece = pieceok
                                                                #k = 2
                                                  
                                      #  else:
                                       #          bloque.play()          
                                #else:
                                 #       bloque.play()
                                







        
          
                                



                
                                
                    
                
            
			
	
                    
