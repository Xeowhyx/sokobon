#!/usr/bin/python3
# -*- coding: Utf-8 -*

import pygame
from pygame.locals import *
from classes import *
from constantes import *
#import pygame.mixer





pygame.init()

fenetre = pygame.display.set_mode((cote_fenetrex, cote_fenetrey), RESIZABLE)

icone = pygame.image.load(image_icone).convert_alpha()
#icone.set_colorkey((0,0,0))
pygame.display.set_icon(icone)

pygame.display.set_caption(titre_fenetre)
pygame.mixer.init()
musiquejeux = pygame.mixer.Sound('assets/musiquejeux.wav')


choix = 0

continuer = True
while continuer:
    accueil = pygame.image.load(image_accueil).convert()
    fenetre.blit(accueil, (0,0))

    pygame.display.flip()

    continuer_jeu = True
    continuer_accueil = True

    while continuer_accueil:
        pygame.time.Clock().tick(30)
        musiquejeux.stop()

        for event in pygame.event.get():

            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                continuer_accueil = False
                continuer_jeu = False
                continuer = False
                pygame.quit()

                #choix = 0

            elif event.type == KEYDOWN:
                
                if event.key == K_1:
                    continuer_accueil = False
                    choix = 'assets/map1.txt'
                    musiquejeux.play(-1)
                    
                    
                    
                elif event.key == K_2:
                    continuer_accueil = False
                    choix = 'assets/map2.txt'
                    musiquejeux.play(-1)
                    

                elif event.key == K_3:
                    continuer_accueil = False
                    choix = 'assets/map3.txt'
                    musiquejeux.play(-1)
                    
                    
                elif event.key == K_4:
                    continuer_accueil = False
                    choix = 'assets/map4.txt'
                    musiquejeux.play(-1)
                    

                elif event.key == K_5:
                    continuer_accueil = False
                    choix = 'assets/map5.txt'
                    musiquejeux.play(-1)
                    
                    
                #elif continuer_accueil == False:
                    #musiquejeux.play(loops=-1, maxtime=0, fade_ms=0)
                    
                
                    


    if choix != 0:

        fond = pygame.image.load(image_fond).convert()
        #fondoption = pygame.image.load(image_fondoption).convert()

        niveau = Niveau(choix)
        niveau.generer()
        niveau.afficher(fenetre)

        perso = Perso("assets/droite.jpg", "assets/gauche.jpg", "assets/bas.jpg", "assets/haut.jpg", niveau,choix)
        
    pygame.key.set_repeat(400,120)
    while continuer_jeu:

         pygame.time.Clock().tick(30)

         for event in pygame.event.get():

             if event.type == QUIT:
                 continuer_jeu = False
                 continuer = False

             elif event.type == KEYDOWN:
                # deplacement = 0 

                 if event.key == K_ESCAPE:
                     continuer_jeu = False

                     
                 elif event.key ==K_RIGHT:
                      perso.deplacer('droite')
                      if event.key == K_r:                  # la touche r permet de retourner le dernier coup jouer ici notre 1er technique consiste a faire deplacer ceux qui a pu bouger, personnage, piece, pieceok
                          perso.deplacer('gauche')
                          self.direction = self.droite      # dans le sens inverse(ici à gauche) en utilisant la même fonction
                          if piece.deplacer('droite'):      # en redeplacant le personnage a gauche il a effectuer 2 deplacements, en effet il a fait un aller-retour
                              piece.deplacer('gauche')      # c'est pour cela qu'on soustrait le deplacement par 2
                              if pieceok.deplacer('droite'):   ## on change l'orientation du personnage avec self.droite pour que le retour arriere soit plus realiste 
                                  pieceok.deplacer('gauche')   ## et pour que le personnage reprend ça position initial avec ça même orientation
                      deplacement -= 2                             
                        
                 elif event.key == K_LEFT:
                      perso.deplacer('gauche')
                      if event.key == K_r:
                          perso.deplacer('droite')
                          self.direction = self.gauche
                          if piece.deplacer('gauche'):
                              piece.deplacer('droite')
                              if pieceok.deplacer('gauche'):
                                  pieceok.deplacer('droite')     
                      deplacement -= 2





                 elif event.key == K_DOWN:
                      perso.deplacer('bas')                          # la 2eme technique consiste a faire deplacer comme dans la 1er le personnage dans le sens inverse donc ici en haut
                      if event.key == K_r:
                          self.direction = self.haut
                          self.case_y = self.case_y-1                # sauf qu'il faut savoir si une piece a etait deplacé s'est pour cela que j'ai mis dans "classe_sokobon2", ligne71 
                          self.case_y = self.case_y * taille_sprite  # un "k" qui va nous dire si il y a eu un deplacement de piece avec k=1 ou si une piece est devenu une pieceok avec k=2
                          if k==1:                                   # ou si une piece ne s'est pas deplacé avec k=0
                              y['$'] = y-1['$']                      # on sait que le seul moyen de deplacer une piece est de la pousser, donc si k=1 il faut retourner le personnage à sa
                              if k==2:                               # position d'avant et la piece dans le même sens, ainsi l'utilisataire aura l'impression de "tiré" la piece (inverse de pousser) 
                                  pieceok = piece                    # donc de cette maniere on peut deviner la position qu'avait la piece avant d'être poussé
                                  y['$'] = y-1['$']
                      deplacement -=1                                # ici deplacement a augmenter que de 1 donc on enleve 1 comme ça le personnage retourne a ça position et conserve
                                                                     # le même nombre de deplacement
                              
                              


                 elif event.key == K_UP:
                      perso.deplacer('haut')
                      if event.key == K_r:
                          self.direction = self.bas
                          self.case_y = self.case_y+1
                          self.case_y = self.case_y * taille_sprite
                          if k==1:
                              y['$'] = y+1['$']
                              if k==2:
                                  pieceok = piece
                                  y['$'] = y+1['$']
                      deplacement -= 1
                          


         fenetre.blit(fond, (0,0))
         #fenetre.blit(fond, (500,0))
         #fenetre.blit(fond, (0,500))
         #fenetre.blit(fond, (500,500))
         #fenetre.blit(fondoption, (1070,0))
         niveau.afficher(fenetre)
         fenetre.blit(perso.direction, (perso.x, perso.y))
         pygame.display.flip()



         for sprite in 'assets/map1.txt':                   # le but étant de mettre toutes les piece soit sur une sucette (symbole %, voir "constante_sokobon2")
             if sprite == '%':                   # comme dans map1 il y a 3piece, tant qu'il n'y a pas 3pieceok le jeux continue
                 n += 1
                 if n==3:                        # sinon le joueur gagne puis on affiche une image            
                     continuer_jeu = False
                     print(deplacement)
                     fenetre = image_victoire
                     gagne.play()
                 else:
                     continuer_jeu = True



         for sprite in 'assets/map2.txt':
              if sprite == '%':
                  n += 1
                  if n==3:
                      continuer_jeu = False
                      print(deplacement)
                      fenetre = image_victoire
                      gagne.play()
                  else:
                      continuer_jeu = True


         for sprite in 'assets/map3.txt':
            if sprite == '%':
                n += 1
                if n==3:
                    continuer_jeu = False
                    print(deplacement)
                    fenetre = image_victoire
                    gagne.play()
                else:
                    continuer_jeu = True 



         

        


                
                     
             
             
                
         

         
         
             
                      

    
                      
         
                    

                    























            
