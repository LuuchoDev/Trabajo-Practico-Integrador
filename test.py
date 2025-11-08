import csv
import os

nombre_archivo = "paises.csv"

# ================================================
#  Funciones para cargar y guardar datos de países
# ================================================


def cargar_paises(nombre_archivo):
    """
    Cargar los datos de paises desde un archivo CSV.

    Valida la existencia del archivo y el formato numérico de
    población y superficie.
    """
    lista_paises = []
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, mode='r', encoding='utf-8', newline='') as archivo:
            lector_csv = csv.DictReader(archivo)

            for fila in lector_csv:
                # Valida si los campos no estan vacíos
                if not fila['nombre'] or not fila['poblacion'] or not fila['superficie'] or not fila['continente']:
                    print(f"Error: La fila con nombre '{fila['nombre']}' tiene campos vacíos. Omitiendo.")
                    continue

                # Valida si son datos numéricos
                poblacion_str = fila['poblacion']
                superficie_str = fila['superficie']

                if not poblacion_str.isdigit() or not superficie_str.isdigit():
                    print(f"Error: La fila para '{fila['nombre']}' contiene datos no numéricos. Omitiendo.")
                    continue
                
                # Si todas las validaciones pasan, creamos el diccionario
                pais = {
                    "nombre": fila['nombre'],
                    "poblacion": int(poblacion_str),
                    "superficie": int(superficie_str),
                    "continente": fila['continente']
                }
                lista_paises.append(pais)
    return lista_paises

def guardar_paises(nombre_archivo, lista_paises):
    """
    Guarda la lista de países en un archivo CSV.
    """
    with open(nombre_archivo, mode="w", newline='', encoding='utf-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(["nombre", "poblacion", "superficie", "continente"])

        for pais in lista_paises:
            escritor.writerow([pais['nombre'], pais['poblacion'], pais['superficie'], pais['continente']])

# ==========================================
#             Funciones de Validación
# ==========================================

def validar_existencia_pais(lista_paises, nombre):
    """
    Valida si un país ya existe en la lista de países.

    Retorna True si el país existe, False en caso contrario.
    """
    nombre_normalizado = nombre.strip().lower()
    for pais in lista_paises:
        if pais['nombre'].strip().lower() == nombre_normalizado:
            return True
    return False

def buscar_pais_por_nombre(lista_paises, nombre_buscado):
    """
    Busca un país en la lista por su nombre.

    Retorna el diccionario del país si se encuentra, None en caso contrario.
    """
    nombre_normalizado = nombre_buscado.strip().lower()
    for pais in lista_paises:
        if pais['nombre'].strip().lower() == nombre_normalizado:
            return pais
    return None

def validar_cantidad(cantidad):
    ## Valida si la cantidad ingresada es un número entero positivo.
    if cantidad.isdigit() and int(cantidad) >= 0:
        return True
    else:
        print("La cantidad debe ser un número entero positivo.")
        return False

def mostrar_lista_paises(lista_paises):
    """
    Muestra una lista de países (diccionarios) en un formato de tabla legible en consola.
    """
    if not lista_paises:
        print("No hay países para mostrar.")
        return
    print("\n" + "=" * 70)
    print(f"{'Nombre':<20} | {'Población':<15} | {'Superficie (km²)':>15} | {'Continente':>15}")
    print("=" * 70)

    ## Datos de cada país
    for pais in lista_paises:
        ## se formatean los números con separadores de miles
        pob_formateada = f"{pais['poblacion']:,}"
        sup_formateada = f"{pais['superficie']:,}"
        print(f"{pais['nombre']:<20} | {pob_formateada:<15} | {sup_formateada:>15} | {pais['continente']:>15}")
    print("=" * 70)

def obtener_rango_numerico(tipo_dato):
    """
    Pide al usuario un rango numérico (mínimo y máximo) y lo valida usando la funcion "validar_cantidad".
    "tipo_dato" es un string (ej: poblacion) para mostrar en los mensajes.
    Retorna (min_val, max_val) como enteros.
    """
    ## Pedir y validar el valor minimo
    while True:
        min_str = input(f"Ingrese la {tipo_dato} MÍNIMA: ").strip()
        if validar_cantidad(min_str):
            break
    ## Pedir y validar el valor maximo
    while True:
        max_str = input(f"Ingrese la {tipo_dato} MAXIMA: ").strip()
        if validar_cantidad(max_str):
            break
    min_val = int(min_str)
    max_val = int(max_str)

    ## verificar que el minimo no sea mayor que el máximo
    if min_val > max_val:
        print(f"Error: El valor mínimo ({min_val}) no puede ser mayor que el valor máximo ({max_val}). Intercambiando valores.")
        min_val, max_val = max_val, min_val
    return min_val, max_val


# ==========================================
#             Funciones de Menú
# ==========================================

def agregar_pais(lista_paises):
    """
    Agrega un nuevo país a la lista de países.
    Valida los datos uno por uno.
    """
    print("\n--- 1. Agregar un País ---")
    
    # 1. Validar Nombre (no vacío y único)
    nombre = ""
    while True:
        nombre = input("Ingrese el nombre del país: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío.")
        elif validar_existencia_pais(lista_paises, nombre):
            print(f"Error: El país '{nombre}' ya existe en la lista.")
        else:
            break 

    # 2. Validar Población (numérico positivo)
    poblacion_str = ""
    while True:
        poblacion_str = input("Ingrese la población del país: ").strip()
        if validar_cantidad(poblacion_str):
            break 

    # 3. Validar Superficie (numérico positivo)
    superficie_str = ""
    while True:
        superficie_str = input("Ingrese la superficie del país (en km²): ").strip()
        if validar_cantidad(superficie_str):
            break 

    # 4. Validar Continente (no vacío)
    continente = ""
    while True:
        continente = input("Ingrese el continente del país: ").strip()
        if not continente:
            print("Error: El continente no puede estar vacío.")
        else:
            break # Dato válido

    # Una vez todo validado, se agrega el país a la lista
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion_str),
        "superficie": int(superficie_str),
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    guardar_paises(nombre_archivo, lista_paises) # Guardamos
    print(f"\n¡País '{nombre}' agregado exitosamente!")

def actualizar_datos_pais(lista_paises):
    """
    Actualiza los datos de un país existente en la lista de países.

    """
    print("\n--- 2. Actualizar Datos de un País ---")
    mostrar_lista_paises(lista_paises)
    nombre_buscado = input("Ingrese el nombre del paìs a actualizar: ").strip()
    pais_encontrado = buscar_pais_por_nombre(lista_paises, nombre_buscado)

    if not pais_encontrado:
        print(f"El país '{nombre_buscado}' no se encontró en la lista.")
        return
    print(f"Actualizando datos para el país: {pais_encontrado['nombre']}")
    print(f"Datos actuales -> Población: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']}")

    # Pedir y validar nueva población
    nueva_poblacion_str = ""
    while True:
        nueva_poblacion_str = input("Ingrese la NUEVA población: ").strip()

        if validar_cantidad(nueva_poblacion_str):
            break 

    # Pedir y validar nueva superficie
    nueva_superficie_str = ""
    while True:
        nueva_superficie_str = input("Ingrese la NUEVA superficie (en km²): ").strip()
        if validar_cantidad(nueva_superficie_str):
            break

    pais_encontrado["poblacion"] = int(nueva_poblacion_str)
    pais_encontrado["superficie"] = int(nueva_superficie_str)
    guardar_paises(nombre_archivo, lista_paises)

    print(f"Datos del país '{pais_encontrado['nombre']}' actualizados exitosamente.")

def buscar_pais(lista_paises):
    """
    Permite buscar países por nombre, mostrando coincidencias
    exactas o parciales.
    """
    print("\n--- 3. Buscar un País ---")

    pais_buscado = input("Ingrese el nombre del país a buscar: ").strip().lower()
    if not pais_buscado:
        print("Error: El nombre no puede estar vacío.")
        return
    ## Buscamos el pais mediante una busqueda exacta usando una función previa
    pais_exacto = buscar_pais_por_nombre(lista_paises, pais_buscado)
    if pais_exacto:
        print(f"\nSe encontró 1 coincidencia exacta para '{pais_buscado}':")
        mostrar_lista_paises([pais_exacto])
        return
    ## Si no hay coincidencia exacta, buscamos coincidencias parciales
    print(f"\nNo se encontró una coincidencia exacta para '{pais_buscado}'. Buscando coincidencias parciales...")
    coincidencias = []
    pais_buscado_lower = pais_buscado.lower()
    for pais in lista_paises:
        if pais_buscado_lower in pais["nombre"].lower():
            coincidencias.append(pais)
    
    ## Mosntrar resultados
    if coincidencias:
        print(f"\nSe encontraron {len(coincidencias)} coincidencias parciales para '{pais_buscado}':")
        mostrar_lista_paises(coincidencias)
    else:
        print(f"No se encontraron coincidencias para '{pais_buscado}'.")

def filtrar_por_continente(lista_paises):
    """
    Filtra y muestra países por continente.
    """
    print("\n--- 4.1 Filtrar por Continente ---")
    continente_buscado = input("Ingrese el continente a filtrar: ").strip()
    if not continente_buscado:
        print("Error: El continente no puede estar vacío.")
        return
    resultados =[]
    for pais in lista_paises:
        if pais['continente'].strip().lower() == continente_buscado.strip().lower():
            resultados.append(pais)
    mostrar_lista_paises(resultados)

def filtrar_por_rango(lista_paises, clave, unidad):
    """
    Funcion para filtrar rangos númericos.
    "clave" es el nombre del campo en el diccionario (poblacion o superficie).
    "unidad" es el texto que se muestra al usuario (población o superficie).
    """
    print(f"\n --- 4.2 Filtrar por Rango de {unidad.title()} ---")
    (min_val, max_val) = obtener_rango_numerico(unidad)
    
    resultados = []
    for pais in lista_paises:
        if min_val <= pais[clave] <= max_val:
            resultados.append(pais)
    mostrar_lista_paises(resultados)



def filtrar_paises(lista_paises):
    """
    Muestra un sub-menú para elegir el tipo de filtro.
    """
    print("\n--- 4. Filtrar Países ---")
    while True:
        print("\n--- 4. Filtrar Países ---")
        print("1. Filtrar por Continente")
        print("2. Filtrar por Rango de Población")
        print("3. Filtrar por Rango de Superficie")
        print("4. Volver al Menú Principal")
        print("-" * 34)
        
        sub_opcion = input("Seleccione una opción de filtro (1-4): ")
        
        match sub_opcion:
            case "1":
                filtrar_por_continente(lista_paises)
            case "2":
                filtrar_por_rango(lista_paises, "poblacion", "población")
            case "3":
                filtrar_por_rango(lista_paises, "superficie", "superficie")
            case "4":
                # Volver al menú principal
                print("Volviendo al menú principal...")
                break
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")
    


def imprimir_menu():
    """
    Imprime el menú de opciones para el usuario.

    """
    print("\n" + "=" * 34)
    print("--- Gestión de Datos de Países ---")
    print("=" * 34)
    print("1. Agregar un país")
    print("2. Actualizar datos de un país")
    print("3. Buscar un país")
    print("4. Filtrar países")
    print("5. Ordenar países")
    print("6. Mostrar estadísticas")
    print("7. Salir")
    print("-" * 34)

def main():
    paises = cargar_paises(nombre_archivo)
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción (1-7): ")
        match opcion:
            case "1":
                agregar_pais(paises)
            case "2":
                actualizar_datos_pais(paises)
            case "3":
                buscar_pais(paises)
            case "4":
                filtrar_paises(paises) ## Falta implementar
            case "5":
                pass ## Ordenar países
            case "6":
                pass ## Mostrar estadísticas
            case "7":
                print("¡Gracias por usar el programa :D!")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
            
main()