from random import randint


BILLETES_DISPONIBLES = [[1, 5], [5, 5], [10, 5], [20, 5], [50, 5], [100, 5]]


def generador_aleatorio_cobro():
    # Genera un entero aleatorio desde zero hasta un maximo cobrable determinado por la suma del total de billetes disponibles.
    maximo_cobrable = 0
    for i in BILLETES_DISPONIBLES:
        maximo_cobrable = maximo_cobrable + (i[0] * i[1])
    cobro = randint(0, maximo_cobrable)
    return cobro

def actualizar_billetes_disponibles(billete_pago, cambio):
    # Cambia la cantidad de billetes disponibles en el cajero restando los que fueron dados como cambio y agregando los que fueron recibidos como pago.
    for x in BILLETES_DISPONIBLES:
        for y in cambio:
            if y == x[0]:
                x[1] = x[1] - 1
        for z in billete_pago:
            if z == x[0]:
                x[1] = x[1] + 1
    print(f"Disponible en el Cajero: {BILLETES_DISPONIBLES}")

def procesar_cambio(diferencia : int):
    # Genera una lista de cambio con los billetes disponibles en el cajero.
    cambio = []
    for disponible in reversed(BILLETES_DISPONIBLES):
        while (diferencia - disponible[0]) >= 0 and (disponible[1] > 0):
            cambio.append(disponible[0])
            diferencia = diferencia - disponible[0]
    return cambio

def verificar_pago(pago_requerido : int, pago_recibido : int):
    # Retorna la diferencia total del cobro y el pago recibido.
    diferencia = pago_recibido - pago_requerido
    return diferencia

def recibir_billetes(pago_requerido : int):
    # Genera una lista de billetes recibidos en pago.
    billetes_recibidos = []
    pago = 0
    while pago < pago_requerido:
        billete_individual = input("Ingrese su pago: Q")
        if int(billete_individual) == 1 or int(billete_individual) == 5 or int(billete_individual) == 10 or int(billete_individual) == 20 or int(billete_individual) == 50 or int(billete_individual) == 100:
            billetes_recibidos.append(int(billete_individual))
            pago = pago + int(billete_individual)
        else:
            print("Denominacion Invalida")
    return billetes_recibidos


if __name__ == "__main__":
    salir = True
    try:
        while salir == True:
            print("1. Realizar Cobro")
            print("2. salir")
            opcion = int(input("Que desea hacer? "))
            if opcion == 1:
                cobro = generador_aleatorio_cobro()
                print(f"Cobro a realizar: {cobro}")
                pago = recibir_billetes(cobro)
                diferencia = verificar_pago(int(cobro), int(sum(pago)))
                if diferencia >= 0:
                    vuelto = procesar_cambio(diferencia)
                    print(f"Su cambio: {vuelto}")
                    actualizar_billetes_disponibles(pago, vuelto)
                elif diferencia < 0:
                    raise Exception("Pago Incompleto")
            elif opcion == 2:
                salir = False
    except:
        raise Exception("Opcion Invalida!")
