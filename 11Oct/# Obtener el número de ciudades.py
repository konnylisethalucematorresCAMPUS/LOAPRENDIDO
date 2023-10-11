# Obtener el número de ciudades
N = int(input("Número de ciudades: "))

# Inicializar una matriz de adyacencia para representar las conexiones entre ciudades
matCiudades = [[0] * N for _ in range(N)]

# Función para agregar una conexión entre dos ciudades
def agregar_conexion(ciudad_origen, ciudad_destino):
    matCiudades[ciudad_origen][ciudad_destino] = 1
    matCiudades[ciudad_destino][ciudad_origen] = 1

# Función para verificar si hay una vía directa entre dos ciudades
def hay_via_directa(ciudad_origen, ciudad_destino):
    return matCiudades[ciudad_origen][ciudad_destino] == 1

# Leer la información de las conexiones entre ciudades
for i in range(N):
    ciudad = input("Nombre de la ciudad {}: ".format(i + 1))
    num_conexiones = int (input("Número de ciudades enlazadas con {}: ").format(ciudad))
    
    for _ in range(num_conexiones):
        ciudad_enlazada = input("Nombre de ciudad enlazada: ")
        # Suponemos que tienes una forma de mapear los nombres de las ciudades a sus índices
        ciudad_origen = i
        ciudad_destino = mapear_ciudad_a_indice(ciudad_enlazada)
        agregar_conexion(ciudad_origen, ciudad_destino)

# Realizar consultas sobre vías directas
while True:
    ciudad_origen = input("Ciudad de origen (o 'salir' para terminar): ")
    if ciudad_origen == 'salir':
        break
    ciudad_destino = input("Ciudad de destino: ")
    
    # Suponemos que tienes una forma de mapear los nombres de las ciudades a sus índices
    origen = mapear_ciudad_a_indice(ciudad_origen)
    destino = mapear_ciudad_a_indice(ciudad_destino)
    
    if hay_via_directa(origen, destino):
        print("Sí hay una vía directa entre {} y {}.".format(ciudad_origen, ciudad_destino))
    else:
        print("No hay una vía directa entre {} y {}.".format(ciudad_origen, ciudad_destino))