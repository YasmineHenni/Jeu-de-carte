import matplotlib.pyplot as plt
import matplotlib.image as mpimg
class Carte:
    def __init__(self,fig,coul,val=0):
        self.setValeur(val)
        self.setCouleur(coul)
        self.setFigure(fig.upper())
        
        
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

    def plot(self,axes=None):
        # On crée un dictionnaire qui associe à une figure le début du nom de fichier
        figFileName ={"2":"test-02","3":"test-03","4":"test-04","5":"test-05","6":"test-06",
                  "7":"test-07","8":"test-08","9":"test-09","10":"test-10","VALET":"test-V",
                  "DAME":"test-D","ROI":"test-R","AS":"test-01"}
        repertoire = 'cartes/'
        Fichier = repertoire + figFileName[self.figure]+ '-' + self.couleur.lower() + '-img.png'
        
        img=mpimg.imread(Fichier)
        if axes is not None:
            axes.axes.clear()
            axes.imshow(img)
            axes.axis('off')
            
        else:
            plt.clf()
            plt.imshow(img)
            plt.axis('off')

    
    
if __name__ == "__main__":
    carte1=Carte('AS', 'pique',10)
    carte2=Carte('dame','coeur',9)
    
    gt= carte1> carte2
    print(carte1,'\n',carte2, '\n',gt)
    carte2.plot()
    