
    

#algorithme, qui affiche  20   element en le multipliant  par 7 et que  si le resultat est un multiple de 3 
# on met un asterisque

n=0
milt=0
while n<=20:
      n=n+1
      milt=n*7      
      if milt %3==0:        
            print(f"7*{n}={milt}*") 
      else:
            print(f"7*{n}={milt}")               
    

#algorithme conversion de fc en dollars   et en euro

fc,dol,eur =0,0.65,1
while eur<=10:
      fc=fc+1
      fc,dol,eur=dol,fc+dol,dol+0.50 
      print(f"{fc} fc =  {dol} $ = {eur} £")

   
 #algorithme  le triple d' nomune  suite logigue de 12  nombre

n=0
while n<=12:
        n=n+1
        triple=n*3
        print(f"{n} le triple est {triple}")
         




n=0
while n<12:
      n=n+1
      print( n, n**2, n**3)

a,b,i=1,1,1
while i<11:
      a,b,i=b,a+b,i+1
      print(b)     
      
      
# table de multiplication  avec  la boucle for
m=0
for i in range(1,11):# ca  cest juste un exemple  de la table 
                     #  de multiplication de 7
      m=i*7
      print(m)
      
#VOICI ALLORS LA TABLE DE MULTIPLICATION  COMPLETE  DE 10 CHIFFRE PREMIER
# pour faire cette exercice  nous aurons besoins de faire usages de  bou
#imbriquer
m=0
for i in range(1,10):
      for j in range(1,10):
            m=i*j 
            print(m ,end="")
            print()
      
 # creation  d'un piramide avec la boucle for pour une suite de la methode  de la fibonacie

a,b,i="*","*",1
for i in range(1,8):
      a,b=b,b+a 
      print(b)          

# creation des  liste et acced   au  element d'une liste
# avec  des indices positifs
l=[15,6,11,-9,0,14,22,34,-95,2,7,24,10]
print(l)
l2=l[0:13:3] #meme methode 
print(l2)# meme methode
print(l[0::3])# meme methode
print(l[::3])# meme methode

 # creation des  liste et acced   au  element d'une liste
# avec  des indices negativers

l=[15,6,11,-9,0,14,22,34,-95,2,7,24,10]
print(l)
print(l[::-3])# parcourir une liste ave  un pas de 3 dans inverse de la liste

print(l[::-1])#  affichage de la liste dans l'ordre iverse

#EXERCICES

sal=list("hello, wold!")
print(sal)
print(sal[:-8])
print(sal[::-4])
print(sal[-12:6:2])

#affectation  multiple des variable
l1=list(range(1,10,2))
l2=list(range(2,16,5))
l3=l1+l2
l4=l1*2
print(l4==l3)

jour = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
a, b = 0, 0
while a<25:
 a = a + 1
 b = a % 7
 print(a, jour[b])
 print(jour)


semaine = ['dimanche','lundi','mardi','mercredi','jeudi','vendredi','samedi']
num=[1,2,3,4,5,6,7]
for i in range(1,7):
      
      Nombre_j=semaine[::i]
      print(Nombre_j[:],num)
#exercice sur le foncton avec des arguments
def table(base):
      affichage=list()
      n=1
      while n<10:          
            nobre=n*base
            affichage.append(nobre)
            n=n+1
      return affichage()     
ta9 = table(9)
print(ta9)