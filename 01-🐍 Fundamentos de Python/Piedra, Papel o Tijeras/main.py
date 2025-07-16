import random
def opciones():
    opciones_jugador = input("Elige piedra, papel o tijeras: ").lower()
    opciones_validas = ["piedra", "papel", "tijeras"]
    opciones_computadora = random.choice(opciones_validas)
    opciones = {
        "jugador": opciones_jugador,
        "computadora": opciones_computadora
    }
    return opciones

def resultado(jugador, computadora):
    if jugador == computadora:
        return "¡Es un empate!"
    elif (jugador == "piedra" and computadora == "tijeras") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijeras" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def main():
    opciones_juego = opciones()
    jugador = opciones_juego["jugador"]
    computadora = opciones_juego["computadora"]

    if jugador not in ["piedra", "papel", "tijeras"]:
        print("Opción no válida. Por favor, elige piedra, papel o tijeras.")
        return

    print(f"Jugador: {jugador}")
    print(f"Computadora: {computadora}")
    print(resultado(jugador, computadora))
if __name__ == "__main__":
    main()
    
# Piedra, Papel o Tijeras
# Un juego simple donde el jugador compite contra la computadora.
# El jugador elige entre piedra, papel o tijeras, y la computadora elige aleatoriamente.
# El resultado se determina según las reglas del juego:
# - Piedra aplasta tijeras (piedra gana)
# - Papel cubre piedra (papel gana)
# - Tijeras cortan papel (tijeras gana)
# - Si ambos eligen lo mismo, es un empate.     