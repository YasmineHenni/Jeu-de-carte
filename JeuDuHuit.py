# -*- coding: utf-8 -*-

from Partie import Partie
from Carte import Carte
import matplotlib.pyplot as plt 
class jeuDuHuit(Partie):
    """
    Définit les règles du jeu du huit
    Hérite de Partie. Le joueur qui tire un 8 de Pique gagne si la somme des points > 18
    """
    def __init__(self,joueurs,nbreCartes=32,nbreMaxPli=1000):
        if len(joueurs) !=2:
            raise Exception('Le nombre de joueur doit être égal à 2 .... au revoir')
        super().__init__(joueurs,'jeuduhuit',nbreCartes,nbreMaxPli)
       #self.figJ1=plt.figure('joueur1',(10,4))
        #self.figJ2=plt.figure('joueur2',(10,4))
        self.fig, (self.ax1, self.ax2) = plt.subplots(1, 2, sharey=True,figsize=(9,4),dpi=120)
                
        
    def distribuerCartes(self):
        joueur_1 = self.listeJoueurs[0]
        joueur_2 = self.listeJoueurs[1]
        for i in range (len(self.jeuCartes)):
            carte = self.jeuCartes.tirerCarte()
           
            if i % 2 == 0:
                joueur_1.ajouterCarteDansPaquetJoueur(carte)
            else:
                joueur_2.ajouterCarteDansPaquetJoueur(carte)
       
                
    def jouerUnPli(self):
        joueur_1 = self.listeJoueurs[0]
        joueur_2 = self.listeJoueurs[1]
        
        carte_joueur1 = joueur_1.tirerCarteJoueur()       
        carte_joueur2 = joueur_2.tirerCarteJoueur()      
       
        if carte_joueur1 is None or carte_joueur2 is None:
            self.finPartie()
            return False
        
        self.paquetTable.ajouterCarteDansPaquet(carte_joueur1)
        self.paquetTable.ajouterCarteDansPaquet(carte_joueur2)
            
        print('    - {} : {}'.format(joueur_1.getPrenomJoueur(), str(carte_joueur1)))
        print('    - {} : {}'.format(joueur_2.getPrenomJoueur(),str(carte_joueur2)))
       
        if (carte_joueur1 == Carte('8','Pique') or carte_joueur2 == Carte('8','Pique')) and self.paquetTable.getValeurDuPaquet() > 20 :
            if joueur_1.paquetJoueur.getValeurDuPaquet() > joueur_2.paquetJoueur.getValeurDuPaquet():
                self.finPartie(joueur_2,joueur_1)
                return False
            if joueur_2.paquetJoueur.getValeurDuPaquet() > joueur_1.paquetJoueur.getValeurDuPaquet():
                self.finPartie(joueur_1,joueur_2)
                return False
        elif carte_joueur1 > carte_joueur2:
                joueur_1.ajouterPaquetDansPaquetJoueur(self.paquetTable)
        elif carte_joueur2 > carte_joueur1:
                joueur_2.ajouterPaquetDansPaquetJoueur(self.paquetTable)
     
        return True
           