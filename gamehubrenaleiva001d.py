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
    
                                            