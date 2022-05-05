import random 
import time

def introduccion():
    print('''Estamos en una tierra llena de dragones. Delante de nuestro
    se ven dos cuevas. En una cueva, el dragon es amigable
    y compartira el tesoro contigo. El otro dragon
    es codicioso y hambriento, y te va a comer ni bien te vea.
    ''')

def elegir_cueva():
    cueva = ''
    while cueva !='1' and cueva !='2':
        cueva = input('a que cueva quieres entrar 1 o 2 ')
    return cueva 

    
def cheqcueva(CambiarCueva,oro):
    puntos = 0
    print ("Te acercas a la Cueva...")
    time.sleep(2)
    print ("Esta oscuro y tenebroso...")
    time.sleep(2)
    print ("Un gran dragon salta delante tuyo, abre su boca y...")
    print ("")
    time.sleep(2)
   
    FriendlyCueva = random.randint (1, 2)
   
    if CambiarCueva == str(FriendlyCueva):
        print ("Te entrega el tesoro...")
        puntos +=100
        oro += puntos
        
        print(f'tu puntaje es {puntos}')
        
    else:
        print ("El dragon te come de un bocado....")
        print(f'tu puntaje es {puntos}')

EmpezarNuevo = ("si")

oro = 0
while EmpezarNuevo == ("s") or EmpezarNuevo == ("si"):
   
    introduccion()
   
    NumCaverna = elegir_cueva()
   
    cheqcueva(NumCaverna,oro)
   
    
    EmpezarNuevo = input("Quieres jugar de nuevo? (si o no) ")