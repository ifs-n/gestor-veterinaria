mascotas = [{
    "nombre":"Olivo", "especie":"Ninfa", "edad":2, "peso":0.09, "estado": True
}]

def verificar_largo(string):
    verificar = True
    while verificar:
        if len(string) <= 0 or string.startswith(" ") == True:
            return False
        else:
            return True

def verificar_entero(numero):
    if isinstance(numero, int) and numero > 0:
        return True
    else:
        return False

def verificar_flotante(numero):
    if isinstance(numero, float) and numero > 0:
        return True
    else:
        return False

def verificar_estado(x):
    if x["estado"] == True:
        return "Saludable"
    else:
        return "No saludable"

def imprimir_menu():
    print("==== Menú Principal ===\n")
    print("1. Agregar mascota")
    print("2. Buscar mascota")
    print("3. Eliminar mascota")
    print("4. Actualizar estados")
    print("5. Mostrar mascotas")
    print("6. Salir\n")
    print("=======================")

def selector_opciones():
    try:
        invalida = "Opción inválida"
        opcion_selector = int(input("Ingrese una opción: \n"))
        if opcion_selector >= 1 and opcion_selector <= 6:
            return opcion_selector
        else:
            return invalida
    except:
        return "La opción ingresada no es un número entero válido."

def agregar_mascota():
    print("== REGISTRAR MASCOTA ==")
    
    nombre = input("Ingrese el nombre de la mascota: \n").title()
    while verificar_largo(nombre) == False:
        nombre = input("El nombre de la mascota no puede quedar vacío.\nIngrese el nombre nuevamente:\n").title()
    
    especie = input("Ingrese la especie:\n").title()
    while verificar_largo(especie) == False:
        especie = input("La especie no puede quedar vacía.\nIngrese la especie nuevamente:\n").title()
    
    edad = int(input("Ingrese la edad de la mascota:\n"))
    while verificar_entero(edad) == False:
        edad = int(input("La edad debe ser un número entero mayor a cero:\n"))

    peso = float(input("Ingrese el peso de la mascota:\n"))
    while verificar_flotante(peso) == False:
        peso = float("El peso debe ser un número mayor a cero: \n")
    
    mascota = {
        "nombre":nombre,
        "especie":especie,
        "edad":edad,
        "peso":peso,
        "estado":False,
    }
    mascotas.append(mascota)

def buscar_mascota():
    print("== BUSCAR MASCOTA ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        buscar = input("Ingrese el nombre de la mascota a buscar: \n").title()
        while verificar_largo(buscar) == False:
            buscar = input("El campo de búsqueda no puede estar vacío: \n").title()
        encontrado = False
        for m in mascotas:
            if m["nombre"] == buscar:
                encontrado = True
                print("== Mascota encontrada ==")
                print(f"Nombre: {m["nombre"]}")
                print(f"Especie: {m["especie"]}")
                print(f"Edad: {m["edad"]}")
                print(f"Peso: {m["peso"]}Kg")
                print(f"Estado: {verificar_estado(m)}")
            if encontrado == False:
                print("La mascota buscada no esta ingresada.")

def eliminar_mascota():
    print("== ELIMINAR REGISTRO DE MASCOTA ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas")
    else:
        eliminar = input("Ingrese el nombre de la mascota que desea eliminar:\n").title()
        while verificar_largo(eliminar) == False:
            eliminar = input("El campo de busqueda para eliminar no puede estar vacío: \n")
        eliminado = False
        for m in mascotas:
            if m["nombre"] == eliminar:
                mascotas.remove(m)
                print(f"El registro de la mascota de nombre {eliminar} ha sido borrado 💀")
                eliminado = True
        if eliminado == False:
            print("No existe una mascota registrada con el nombre ingresado.")

def actualizar_estados():
    print("== ACTUALIZAR ESTADOS ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        actualizados = 0
        for m in mascotas:
            verificado = False
            if m["estado"] == False:
                if m["peso"] > 2 and m["edad"] < 15:
                    m["estado"] = True
                    verificado = True
                    actualizados += 1
            if verificado == False:
                m["estado"] = False
                actualizados += 1


def mostrar_mascotas():
    actualizar_estados()
    print("== MOSTRAR MASCOTAS ==")
    if len(mascotas) == 0:
        print("No hay mascotas registradas.")
    else:
        for m in mascotas:
            print(f"*** Mascota N°{mascotas.index(m) + 1} ***")
            print(f"Nombre: {m["nombre"]}")
            print(f"Especie: {m["especie"]}")
            print(f"Edad: {m["edad"]}")
            print(f"Peso: {m["peso"]} kg")
            print(f"Estado: {verificar_estado(m)}")
            print("*************************")

