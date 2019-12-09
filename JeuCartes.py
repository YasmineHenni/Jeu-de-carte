from PaquetCartes import PaquetCartes
from Carte import Carte



class JeuCartes(PaquetCartes):
    """
    Crée un jeu de 32 ou 54 cartes
    On considère qu'un jeu de carte est un paquet de cartes
    """  
    
    def __init__(self,nombreDeCartes):
        super().__init__()
        # On crée 2 dictionnaires pour les jeux à 32 ou 54 cartes et on associe à chaque clé (figure) sa valeur
        if nombreDeCartes not in [32,54]:
            raise ValueError('Nombre de cartes incorrect .... au revoir')  
        dicoFigures={
            54:{"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"Valet":11,"Dame":12,"Roi":13,"AS":14},
            32:{"7":7,"8":8,"9":9,"10":10,"Valet":11,"Dame":12,"Roi":13,"AS":14}
                    }
        
        couleurs = ("Coeur","Carreau","Trefle","Pique") 
    
        figures = dicoFigures[nombreDeCartes]
        for fig in figures:    # On balaie toutes les figures et couleurs
            for coul in couleurs:   # et on les met dans le jeu (avec la valeur)
                self.ajouterCarteDansPaquet(Carte(fig,coul,figures[fig]))
                
        self.melanger()     # on mélange le jeu
    

if __name__ == '__main__':
    jeu=JeuCartes(54)
    jeu.plot()
    