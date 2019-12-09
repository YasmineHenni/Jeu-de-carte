import matplotlib.pyplot as plt
from Carte import Carte
import random
class PaquetCartes:
    def __init__(self):
        self.listeCartes=[]
        self.nombreCarte=0
        
    def __str__(self):
        tmp=''
        for i in self.listeCartes:
            tmp=tmp + i.__str__()+'\n'
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
        self.listeCartes.append(carte)
    
    def ajouterPaquetDansPaquet(self,paquet):
        for c in paquet:
            self.ajouterCarteDansPaquet(c)
            
    def getValeurDuPaquet(self):
        val=0
        for c in self.listeCartes:
            val= val + c.getValeur()
        return val 
    
    
    def __len__(self):
        return len(self.listeCartes)
    def clearListeCartes(self):
        self.listeCartes.clear()


    def plot(self,fig=None):
        ''' Affiche l'ensemble des cartes du paquet en les décalant
        '''
        
        if fig==None:
            fig=plt.figure()
            dx=0.01
            dy=0
        left,bottom,width,height=0.,0.1,0.2,0.2
        for c in self.listeCartes:           
            c.plot(fig.add_axes((left,bottom,width,height)))
            left+=0.05
            if left >0.9:
                left=0
                bottom +=0.3
            
if __name__ == '__main__':

    C1=Carte('as','pique',10)
    C2=Carte('as','coeur',10)
    C3=Carte('Valet','Trefle',10)
    P=PaquetCartes()
    P.ajouterCarteDansPaquet(C1)   
    P.ajouterCarteDansPaquet(C2)
    P.ajouterCarteDansPaquet(C3)
    print(P)
    P.plot()