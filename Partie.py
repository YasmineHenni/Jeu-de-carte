#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:59:23 2019

@author: yasmine
"""

class Partie:
    def __init__(self,listeJoueurs,nomDuJeu,nbreCartes=32,nbreMaxPli=1000):
        pass
    
    
    def getNbreJoueur(self):
        pass
    
    
    def getNomDuJeu(self):
        pass

    def run(self):
        pass
    
    def distribuerCartes(self):
      raise NotImplementedError('cette méthode n est pas definie dans cette classe')
      
      
    def jouerUnPli(self):
        raise NotImplementedError('cette méthode n est pas definie dans cette classe')


    def finPartie(self,perdant=None,gagnant=None):
        pass

        
        
    def __str__(self):
        pass