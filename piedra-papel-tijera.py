# Desafio
# Se puede mejorar el nombre en la segunda solicitud
# Lo ingresado por el usiario sea lowercase de tal forma de comparar minuscula con minuscula
# Mas de un turno con el bucle while

nombre1 = input("como se llamara el  jugador 1 ")
nombre2 = input("como se llamara el  jugador 2 ")

jugador1 = input("hola jugador 1, que eliges? piedra, papel o tijerta?: ")
jugador2 = input("hola jugador 2, que eliges? piedra, papel o tijerta?: ")

condicion1 = jugador1=="piedra" and jugador2=="tijera"
condicion2 = jugador1=="papel" and jugador2=="piedra"
condicion3 = jugador1=="tijera" and jugador2=="papel"
if jugador1 == jugador2:
    print("¡Ha sido un empate!")
elif condicion1  or condicion2  or condicion3 :
    print("ha ganado", nombre1)
else: 
    print("ha ganado", nombre2)

