import pandas as pd

verificar_acceso = lambda nombre, apellido, base_datos: any(base_datos.apply(lambda row: row['Nombre'].strip().capitalize() == nombre.strip().capitalize() and row['Apellido'].strip().capitalize() == apellido.strip().capitalize(), axis=1))

def main():
    print("Bienvenido al sistema de pedidos de Cantina de UTN FRVM")
    print("Validaremos su identidad")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    
    base_datos = pd.read_excel('C:/Users/TuUsuario/Desktop/baseDatos.xlsx')

    if verificar_acceso(nombre, apellido, base_datos):
        print("Acceso concedido. Ahora puedes realizar tu pedido")
    else:
        print("Acceso denegado. No perteneces al personal de la facultad.")
        
main()
