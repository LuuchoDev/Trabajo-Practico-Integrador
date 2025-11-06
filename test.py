import csv
import os

nombre_archivo = "paises.csv"

## Funciones para cargar y guardar datos de países
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
    
## Validaciones pendientes
# Evitar fallos al ingresar filtros inválidos o búsquedas sin resultados.
# Mensajes claros de éxito/error.
#

def imprimir_menu():
    """
    Imprime el menú de opciones para el usuario.

    """
    print("\n" + "=" * 34)
    print("\n--- Gestión de Datos de Países ---")
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
                pass ## Agregar un país
            case "2":
                pass ## Actualizar datos de un país
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