class Carte:
    def __init__(self,fig,coul,val=0):
        self.setValeur(val)
        self.setCouleur(coul)
        self.setFigure(fig)
        
        
    def getFigure (self):
        return self.figure
    
    def setFigure (self,fig):
        self.figure = fig
        
    def getCouleur (self):
        return self.couleur
    
    def setCouleur(self,coul):
        self.couleur = coul
        
    def getValeur(self):
        return self.valeur
    
    def setValeur(self,val):
        self.valeur= val
    
    def __eq__(self,other):
        if self.valeur== other.valeur:
            return True 
        else :
            return False
    
    def __gt__(self,other):
        if self.valeur > other.valeur:
            return True 
        else:
            return False
    
    def __str__(self):
        tmp=("la carte est un {} de {}".format(self.getFigure() , self.getCouleur()))
        return tmp
    
    
    
if __name__ == "__main__":
    carte1=Carte('as', 'pique',10)
    carte2=Carte('dame','coeur',9)
    
    gt= carte1> carte2
    print(carte1,'\n',carte2, '\n',gt)
        