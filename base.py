import pandas as pd

def verificar_acceso(nombre, apellido, base_datos):
    # Convertir el nombre y apellido a formato adecuado para la comparación
    nombre = nombre.strip().capitalize()
    apellido = apellido.strip().capitalize()

    # Verificar si el usuario está en la base de datos
    resultado = base_datos[(base_datos['Nombre'] == nombre) & (base_datos['Apellido'] == apellido)]

    return not resultado.empty

def main():
    # Solicitar nombre y apellido al usuario
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")

    # Cargar la base de datos desde el archivo Excel
    try:
        base_datos = pd.read_excel('C:/Users/TuUsuario/Desktop/baseDatos.xlsx')
    except FileNotFoundError:
        print("Error: No se encontró el archivo 'baseDatos.xlsx' en el escritorio.")
        return

    # Verificar acceso y mostrar el resultado
    if verificar_acceso(nombre, apellido, base_datos):
        print("Acceso concedido. ¡Eres una persona de la facultad!")
    else:
        print("Acceso denegado. No estás en la lista.")

if __name__ == "__main__":
    main()
