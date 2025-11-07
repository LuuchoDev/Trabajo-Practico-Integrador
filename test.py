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
    

# ==========================================
#             Funciones de Menú
# ==========================================

def agregar_pais(lista_paises):
    """
    Agrega un nuevo país a la lista de países.

    Solicita al usuario el nombre, población, superficie y continente del país.
    Valida que el país no exista ya en la lista.
    """
    nombre = input("Ingrese el nombre del país: ").strip()
    poblacion = input("Ingrese la población del país: ").strip()
    superficie = input("Ingrese la superficie del país (en km²): ").strip()
    continente = input("Ingrese el continente del país: ").strip()

    # Validar que el país no exista ya
    if validar_existencia_pais(lista_paises, nombre):
        print(f"El país '{nombre}' ya existe en la lista.")
        return

    # Validar que población y superficie sean números enteros positivos
    if not poblacion.isdigit() or int(poblacion) < 0:
        print("La población debe ser un número entero positivo.")
        return
    if not superficie.isdigit() or int(superficie) < 0:
        print("La superficie debe ser un número entero positivo.")
        return

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": int(poblacion),
        "superficie": int(superficie),
        "continente": continente
    }
    lista_paises.append(nuevo_pais)
    guardar_paises(nombre_archivo, lista_paises)
    print(f"País '{nombre}' agregado exitosamente.")

def actualizar_datos_pais(lista_paises):
    """
    Actualiza los datos de un país existente en la lista de países.

    """
    nombre_buscado = input("Ingrese el nombre del paìs a actualizar: ").strip()
    pais_encontrado = buscar_pais_por_nombre(lista_paises, nombre_buscado)

    if not pais_encontrado:
        print(f"El país '{nombre_buscado}' no se encontró en la lista.")
        return
    print(f"Actualizando datos para el país: {pais_encontrado['nombre']}")
    print(f"Datos actuales -> Población: {pais_encontrado['poblacion']} | Superficie: {pais_encontrado['superficie']}")

    nueva_poblacion = input("Ingrese la nueva población: ").strip()
    nueva_superficie = input("Ingrese la nueva superficie: ").strip()

    # Validar que población y superficie sean números enteros positivos
    if not nueva_poblacion.isdigit() or int(nueva_poblacion) < 0:
        print("La población debe ser un número entero positivo.")
        return
    if not nueva_superficie.isdigit() or int(nueva_superficie) < 0:
        print("La superficie debe ser un número entero positivo.")
        return

    pais_encontrado["poblacion"] = int(nueva_poblacion)
    pais_encontrado["superficie"] = int(nueva_superficie)
    guardar_paises(nombre_archivo, lista_paises)

    print(f"Datos del país '{pais_encontrado['nombre']}' actualizados exitosamente.")


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
                pass ## Buscar un país
            case "4":
                pass ## Filtrar países
            case "5":
                pass ## Ordenar países
            case "6":
                pass ## Mostrar estadísticas
            case "7":
                print("¡Gracias por usar el programa :D!.")
                break
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
            
main()