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

    