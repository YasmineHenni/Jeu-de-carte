#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:29:40 2019

@author: yasmine
"""
from PaquetCartes import PaquetCartes

class Joueur:
    def __init__(self,prenom):
        self.nombreVictoire=0
        self.nombreDefaite=0
        self.prenomDuJoueur= prenom
        self.paquetJoueur= PaquetCartes()
        
    def getPrenomJoueur(self):
        return self.prenomDuJoueur
    

        
    def getVictoireJoueur(self):
         return self.nombreVictoire
        
    def incVictoireJoueur(self):
        self.nombreVictoire+=1
        
    def getDefaiteJoueur(self):
        return self.nombreDefaite
    
    def incDefaiteJoueur(self):
        self.defaites+=1
        
    def tirerCarteJoueur(self):
        self.paquetJoueur.pop(i)
    
    def ajouterCarteDansPaquetJoueur(self, carte):
        self.paquetJoueur.append(carte)
        
    def ajouterPaquetDansPaquetJoueur(self,paquetAAjouter):
        self.paquetJoueur.ajouterPaquetDansPaquet(paquetAAjouter)
    
    def __str__(self):
        return 'nom du joueur(se) : {}, son nombre de victoires est: {} et ses defaites :{}'.format(self.getPrenomJoueur(), self.getVictoireJoueur(), self.getDefaiteJoueur())           
    
    def __repr__(self):
        return self.__str__()
    
    def listeCarte(self):
        return self.paquetJoueur
    
    def ClearPaquetJoueur(self):
        self.paquetJoueur.clearListeCartes()
        
        
if __name__=='__main__':
    
    j=Joueur('laurent')
    print(j)
    
    
    
        