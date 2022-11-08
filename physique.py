from math import *
import csv
f = open("résultat.cvs","a", newline="")
writer = csv.writer(f)



#les variables 
h = float(input("entrez l'altitude de départ en [m] : "))
vi = float(input("entrez la vitesse initiale en [m/s] :"))
dh = 0.1 #la précision

# le code 
if h > 0:
    
    #verification
    an1 = input(print(f"Le calcule va commencer avec {h} pour  hauteur initiale et {vi} pour vitesse initiale, si c'est bon entrez Y sinon N : "))
    if an1 == "Y":
        
        #début du calcule
        while h >= 0:
            
            
            
            a = 667/((1335+h)**2)
            da = (667/((1335+h+dh)**2))-a 
            
            
            v = a * dh
            
            
            
            t = dh/v
           
            
            #print(h)
            #print(a)
            #print(t)
            #print(v, "\n")
            h = h - dh
        h = 0 
        a =  667/((1335+h)**2)
        da = ((667/1335+h+dh)**2)-a 
        v = da * dh
        t = dh/v
        print(h)
        print(a)
        print(t)
        print(v, "\n c'est fini!")







f.close()