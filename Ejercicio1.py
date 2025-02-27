def calculadora_iva(nombre_producto, precio):
    iva = 0,21
    precio_con_iva = precio * (1 + iva)
    return f"{nombre_producto}, {precio_con_iva:.2f};"

def archivo_listado(nombre_archivo, datos):
    try:
        with open(nombre_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(datos + "\n")

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()

        print("ALUMNADO CON UT2 SUPERADA")
        return contenido
    except Exception as e:
        return f"Error al manejar el archivo: {e}"
    

nombre = "Caña de pescar"
precio = 50.00


datos_producto= calculadora_iva(nombre, precio)

contenido_actualizado= archivo_listado("listado_de_precios.txt", datos_producto)

print(contenido_actualizado)

        