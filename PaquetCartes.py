#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 16:54:49 2019

@author: yasmine
"""
import random
class PaquetCartes:
    def __init__(self):
        self.listeCartes=[]
        self.nombreCarte=0
        
    def __str__(self):
        for i in self.listeCartes:
            tmp=i.__str__()
            return tmp
        
    def melanger(self):
        random.shuffle(self.listeCartes)
    
    def tirerCarte(self,index):
        n= len(self.listeCartes)
        if n==0 :
            return None
        else:
            return self.listeCartes.pop(index)
            
            
    
    def ajouterCarteDansPaquet(self,carte):
        pass
    
    def ajouterPaquetDansPaquet(self,paquet):
        pass
    def getValeurDuPaquet(self):
        pass
    def __len__(self):
        pass
    def clearListeCartes(self):
        pass
    