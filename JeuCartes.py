#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 17:37:03 2019

@author: yasmine
"""
from PaquetCartes import PaquetCartes
from Carte import Carte

class JeuCartes(PaquetCartes):

    def __init__(self,nombreDeCartes):
        super().__init__()
        figures54 ={"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Valet":11,"Dame":12,"Roi":13,"AS":14}
        figures32 ={"7":7,"8":8,"9":9,"10":10,"Valet":11,"Dame":12,"Roi":13,"AS":14}
        couleurs = ("Coeur","Carreau","Trefle","Pique")
        self.nombreCarte=nombreDeCartes
        self.PaquetCartes= self.listeCartes
        if self.nombreCarte== 32:
            for couleur in couleurs:
                for k,v in figures32:
                    carte= Carte(k,couleur,v)
                    self.ajouterCarteDansPaquet(carte)
        else:
            for couleur in couleurs:
                for k,v in figures54:
                    carte= Carte(k,couleur,v)
                    self.ajouterCarteDansPaquet(carte)
        
        
        
j= JeuCartes(32)
print(j)
        