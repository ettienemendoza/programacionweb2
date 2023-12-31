def agregar_compra(compras):
 compra = int(input("Ingrese el monto de la compra: "))
 compras.append(compra)
 print("Compra agregada correctamente.")

def mostrar_compras(compras):
    if len(compras) > 0:
        for i, tarea in enumerate(compras, start=1):
            print(f"{i}. ${tarea}.00  ")
    else:
        print("Error, no hay compras registradas")
def mostrar_total(compras):
    total_gastado=0
    for x in compras:
        total_gastado = total_gastado + x
    print(f"Total gastado: ${total_gastado}.00")
def main():
    compras = []
    while True:
     print("Menú:")
     print("1. Agregar compra")
     print("2. Mostrar compras")
     print("3. Mostrar total gastado")
     print("4. Salir")
     opcion = input("Seleccione una opción: ")

     if opcion == "1":
        agregar_compra(compras)

     elif opcion == "2":
        mostrar_compras(compras)

     elif opcion == "3":
        mostrar_total(compras)

     elif opcion == "4":
        print("FIN DEL PROGRAMA.")
        break
     else:
        print("Error la opcion ingresada noes valida.")

main()