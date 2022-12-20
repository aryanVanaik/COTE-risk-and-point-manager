import scipy
from scipy import *

class poss():
    def __init__(self,pos):
        self.pos =pos
    def __str__(self):
        # Fill this in
        return f"{self.pos}"

    def countPointsNCP(self,x):
        total =0
        for i in range(0, len(self.pos)):
            if(i == "1") :total==100
            if(i=="2"): total+=100*(1-x)-50*x
            if(i == "3"):  total+= 75
        return total    
            

    def countPointsCP(self):
        total =0
        for i in range(0, len(self.pos)):
            if(i=="2"): total+=100
            if(i == "3"):  total+= 100
            
        return total

         
            
    def countOccurance(self,num):
        ctr =0
        for i in range(0, len(self.pos)):
            if i ==num:
                ctr+=1
        return ctr  

    def risk(self,x):
        dup = self.countOccurance(2)
        return scipy.stats.binom.pmf(dup, dup, x)          

    def riskNCP(self):
        return self.risk(3)

    def riskCP(self):
        return self.risk(2)    
   

    