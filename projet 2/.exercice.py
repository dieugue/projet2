def main():
    x=seconde()
    print(x)
def seconde():    
    while True:
        try:
           x=int(input(" veuillez donner la veleur de x"))  
        except ValueError:
            print("cette  valeur est ivnvalide")
        else:
             return x
             
main()
from turtle import *
def  triangle(kouleur):
 reset()
 cote=0
 while cote<=3:
   cote+=1
   left(120)
   forward(100)
   color('green')   
   color('red')   
triangle(color)
def monter():
    global a
    a = 15
    a = a+1
    print(a)
a = 15
monter()
def table(base):
    resultat = [] # resultat est d’abord une liste vide
    n = 1
    while n < 11:
        b = n * base
        resultat.append(b) # ajout d’un terme à la liste
        n = n +1 # (voir explications ci-dessous)
        return resultat
t=table(7)
print(t)

def tableau2(nobre):
   resulta=[] 
   n=1
   while n<=11:
        m=n*nobre
        n+=1
   resulta.append(m)
   return resulta
rep=tableau2(1)  
print(rep)



    