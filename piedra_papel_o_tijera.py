from random import choice as escoge

opciones = ["piedra", "papel", "tijera"]
usuario = input("Ingrese piedra, papel o tijera: ").lower()

if usuario not in opciones:
    print("Elige una de las opciones marcadas!")
else:
    computadora = escoge(opciones)
    print(f"La computadora eligió: {computadora}")
    
    if usuario == "piedra" and computadora == "tijera" or \
    usuario == "papel" and computadora == "piedra" or \
    usuario == "tijera" and computadora == "papel":
        print("----------->  Ganaste!")
    
    elif usuario == computadora:
        print("-----------> Empate!")
        
    else:
        print("-----------> Perdiste!")
    