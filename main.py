import os
from time import sleep
from functions import *

os.system("cls")

flag = True

while flag:
    os.system("cls")
    imprimir_menu()
    opcion = selector_opciones()
    
    if opcion == 1:
        os.system("cls")
        agregar_mascota()
    elif opcion == 2:
        os.system("cls")
        buscar_mascota()
        sleep(2)
    elif opcion == 3:
        os.system("cls")
        eliminar_mascota()
        sleep(2)
    elif opcion == 4:
        os.system("cls")
        actualizar_estados()
        sleep(2)
    elif opcion == 5:
        os.system("cls")
        mostrar_mascotas()
        sleep(2)
    elif opcion == 6:
        os.system("cls")
        print("Gracias por utilizar el sistema. Vuelva pronto.")
    else:
        print(opcion)

