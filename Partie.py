#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:59:23 2019

@author: yasmine
"""
from JeuCartes import JeuCartes
class Partie:
    def __init__(self,listeJoueurs,nomDuJeu,nbreCartes=32,nbreMaxPli=1000):
        self.listeJoueurs= listeJoueurs
        self.nomDuJeu= nomDuJeu
        self.jeu= JeuCartes(nbreCartes)
        self.nbreMaxPli= nbreMaxPli
        
    
    
    def getNbreJoueur(self):
        return len(self.listeJoueurs)
    
    
    def getNomDuJeu(self):
        return self.nomDuJeu
    

    def run(self):
        pass
    
    def distribuerCartes(self):
      raise NotImplementedError('cette méthode n est pas definie dans cette classe')
      
      
    def jouerUnPli(self):
        raise NotImplementedError('cette méthode n est pas definie dans cette classe')


    def finPartie(self,perdant=None,gagnant=None):
        if perdant == None:
            print('Pas de gagant')
        else:
            perdant.incDefaiteJoueur()
            gagnant.incVictoireJoueur()
        
        
    def __str__(self):
        return "le jeu est : {} , et les joueurs sont : {}".format(self.getNomDujeu(), self.listeJoueurs)