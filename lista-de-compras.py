# TU LISTA DE COMPRAS

print("BIEVENIDO A TU LISTA DE COMPRAS")
print("Elige una de las siguientes opciones:")
print("1. Agregar producto")
print("2. Ver lista de compras")
print("3. Marcar producto como comprado")
print("4. Salir")


opcion = input(f"Ingresa tu opcion: ")

if opcion == "1":
    producto = input("Ingrese el nombre del producto: ")
    with open("compras.txt", "a") as archivo:
        archivo.write(f"[ ] {producto}\n")
    print(f"✅ Producto '{producto}' agregado.")
 
       
elif opcion == "2":
     try:
         with open("compras.txt", "r") as archivo:
                productos = archivo.readlines()
         if not productos:
                print("🛒 Tu lista está vacía.")
         else:
            print("\n📋 Lista de compras:")
            for i, item in enumerate(productos, start=1):
                print(f"{i}. {item.strip()}")
     except FileNotFoundError:
            print("⚠️ No hay productos guardados aún.")

elif opcion == "3":
      try:
        with open("compras.txt", "r") as archivo:
             productos = archivo.readlines()

        if not productos:
             print("No hay productos en tu lista.")
        else:
             print("\n LISTA DE COMPRAS:")
             for i, item in enumerate(productos, start=1):
                print(f"{i}. {item.strip()}")

             seleccion = int(input("Ingresa el número del producto comprado: "))

        if 1 <= seleccion <= len(productos):
                productos[seleccion - 1] = productos[seleccion - 1].replace("[ ]", "[✔]")

                with open("compras.txt", "w") as archivo:
                    archivo.writelines(productos)

                print("✅ Producto marcado como comprado.")
        else:
                print("⚠️ Número inválido.")

      except FileNotFoundError:
        print("⚠️ No hay productos guardados aún.")
    
      except ValueError:
        print("⚠️ Ingresa un número válido.")
elif opcion == "4":
    print("¡Gracias por usar la lista de compras! 🛍️")


        
     
     

 