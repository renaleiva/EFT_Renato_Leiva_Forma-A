def validar_titulo(titulo):
    if titulo.strip() != "":
        return True
    else:
        return False
    
def validar_plataforma(plataforma):
    if plataforma.strip() != "":
        return True
    else:
        return False

def validar_genero(genero):
    if genero.strip() != "":
        return True
    else:
        return False

def validar_clasificacion(clasificacion):
    aux = clasificacion.upper().strip()
    if aux == "E" or aux == "T" or aux == "M":
        return True
    else:
        return False

def validar_multiplayer(es_multi):
    aux = es_multi.lower().strip()
    if aux == "si" or aux == "no":
        return True
    else:
        return False

def validar_editor(editor):
    if editor.strip() != "":
        return True
    else:
        return False

def validar_precio(precio):
    if precio > 0:
        return True
    else:
        return False

def validar_stock(stock):
    if stock > 0:
        return True
    else:
        return False

def leer_opcion():
    try:
        entrada = input("Ingrese una opcion del 1 al 6: ")
        opcion = int(entrada)
        if opcion >= 1 and opcion <=6:
            return opcion
        else:
            return "fuera_rango"
    except ValueError:
            return "no_disp"

def buscar_codigo(codigo, juegos):
    if codigo in juegos:
        return True
    else:
        return False
    
def stock_plataforma(plataforma, inventario, juegos):
    plataforma = plataforma.lower().strip()
    total_acumulado = 0
    encontrado = False

    for cod, datos in juegos.items():
        if datos [1].lower() == plataforma:
            encontrado = True
            stock_disp = inventario[cod][1]
            total_acumulado += stock_disp
            print(f"El total de stock disponible es '{stock_disp}'") 
    if encontrado == True:
        print(f"El stock por plataforma es de: '{stock_plataforma}' El stock total acumulado es de: {total_acumulado}")
        return True
    else:
        return False

def busqueda_precio(p_min, p_max, inventario, juegos):
    lista_filtrada = []
    for codigo, datos in inventario.items():
        dentro_rango = datos[0]
        stock_disp = datos[1]
    if p_min <= dentro_rango <= p_max and stock_disp>0:
        titulo_juego = juegos[codigo][0]
        lista_filtrada.append ([titulo_juego, codigo, stock_disp])
    if len(lista_filtrada) == 0:
        return False
    
    for i in range(len(lista_filtrada)):
        for j in range(len(lista_filtrada)):
            if lista_filtrada[i][0] < lista_filtrada[j][0]:
                lista_filtrada[i], lista_filtrada[j] = lista_filtrada[j], lista_filtrada[i]

    for juego in lista_filtrada:
        print(f"Juego: {juego[0]} y Juego: ({juego[1]}) dentro del rango de precios.")
        print(f"Stock disponible: {juego[0]} = {juego[2]}")
        return True            
    
def actualizar_precio(codigo, nuevo_precio, inventario):
    inventario[codigo][0] = nuevo_precio

def agregar_juego(juegos, inventario, codigo, titulo, plataforma, genero, clasificacion, es_multi, editor, precio, stock):
    if es_multi.lower().strip() == "si":
        valor_multi = True
    else:
        valor_multi = False

    juegos[codigo] = [titulo, plataforma, genero, clasificacion, valor_multi, editor]  
    inventario[codigo] = [precio, stock] 

def eliminar_juego(codigo, inventario, juegos):
    juegos.pop(codigo)
    inventario.pop(codigo) 


def main():

    juegos = {
  'G001': ['Eclipse Runner', 'PC', 'accion', 'T', True, 'NovaStudio'],
  'G002': ['Puzzle Atlas', 'Switch', 'puzzle', 'E', False, 'BrightWorks'],
  'G003': ['Sky Legends', 'PS5', 'aventura', 'T', True, 'OrionGames'],
  'G004': ['Racing Pulse', 'PC', 'carreras', 'E', True, 'VelocityLab'],
  'G005': ['Mystic Farm', 'Switch', 'simulacion', 'E', False, 'GreenSeed'],
  'G006': ['Shadow Tactics', 'Xbox', 'estrategia', 'M', False, 'IronGate'],
 
          }
    
    inventario = {
  'G001': [9990, 7],
  'G002': [19990, 0],
  'G003': [42990, 3],
  'G004': [14990, 5],
  'G005': [17990, 9],
  'G006': [39990, 2],

          }
    
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Stock por plataforma")
        print("2. Búsqueda de juegos por rango de precio")
        print("3. Actualizar precio de juego")
        print("4. Agregar juego")
        print("5. Eliminar juego")
        print("6. Salir")
        print("=====================================")

        
        opcion = leer_opcion()
        if opcion == "no_disp":
         print("Error, la opcion debe ser un numero mayor a 0.")
         continue
        elif opcion == "fuera_rango":
            print("Error, la opcion debe ser un numero entero valido")
            continue

        
        if opcion == 1:
            stock = input("Ingrese la plataforma que desea consultar: ")
            if stock_plataforma (stock, inventario, juegos) == False:
                print("Error, no se ha encontrado el titulo.")

        
        elif opcion == 2:
            try:
                p_min = int(input("Ingrese el precio minimo: "))
                p_max = int(input("Ingrese el precio maximo: "))

                if busqueda_precio(p_min, p_max, juegos, inventario) == False:
                    print("Error, no hay peliculas dentro de ese rango de precio.")
            except ValueError:
                print("Error, el precio deben ser numeros enteros validos.")

        
        elif opcion == 3:
            codigo = input("Ingrese el codigo del juego para ingresar al precio: ")
            if buscar_codigo(codigo, juegos) == False:
                print("No se ha encontrado el codigo del juego.")
                continue
            try:
                nuevo_precio = int(input("Ingrese el nuevo precio que desea actualizar: "))
                if validar_precio(nuevo_precio) == True:
                    actualizar_precio(codigo, nuevo_precio, juegos)
                    print("El precio se ha actualizado con exito")
                else:
                    print("No se ha podido actualizar el precio.")
            except ValueError:
                print("Debe ingresar un precio valido para poder actualizar.")

        
        elif opcion == 4:
            try:
                codigo = input("Ingrese el codigo del juego a ingresar: ")
                titulo = input("Ingrese el nombre del videojuego: ")
                plataforma = input("Ingrese la plataforma del videojuego: ")
                genero = input("Ingrese el genero del videojuego: ")
                clasificacion = input("Ingrese la clasificacion del videojuego(E, T, M): ")
                multiplayer = input("Ingrese si el videojuego es multiplayer (si/no): ")
                editor = input("Ingrese la empresa que edito el videojuego: ")
                precio = int(input("Ingrese el precio del videojuego: "))
                stock = int(input("Ingrese el stock del videojuego: "))

            except ValueError:
                print("Error debe ingresar datos validos.")
                continue
            if(codigo != "" and not buscar_codigo(codigo, juegos)) and validar_titulo(titulo) and validar_plataforma(plataforma) and validar_genero(genero) and validar_clasificacion(clasificacion) and validar_multiplayer(multiplayer) and validar_editor(editor) and validar_precio(precio) and validar_stock(stock):
              agregar_juego(codigo, titulo, plataforma, genero, clasificacion, multiplayer, editor, precio, stock) 
              print (f"Exito, VideoJuego: {titulo}, agregado con exito.")
            else:
                print("Error, los datos no son compatibles para agregar el videojuego.")                                            

        
        elif opcion == 5:
            codigo = input("Ingrese el codigo de la pelicula que desea eliminar: ")
            if eliminar_juego(codigo, inventario, juegos) == True:
                print("La pelicula ha sido eliminada con exito.")
            else:
                print("Error, los datos no son validos o el codigo de la pelicula no existe.")

        
        elif opcion == 6:
            print("Programa finalizado.")
            break
main()                


    


        


