def mostrar_menu():
    print("\n=== SISTEMA DE ADMINISTRACIÓN DE POSTRES ===")
    print("1. Ver todos los postres")
    print("2. Ver ingredientes de un postre")
    print("3. Agregar nuevo postre")
    print("4. Agregar ingredientes a un postre")
    print("5. Eliminar ingrediente de un postre")
    print("6. Eliminar un postre")
    print("7. Eliminar postres repetidos")
    print("8. Salir")
    return input("\nSeleccione una opción (1-8): ")

def ver_postres(POSTRES):
    if not POSTRES:
        print("\nNo hay postres registrados.")
        return
    print("\n=== POSTRES DISPONIBLES ===")
    for i, postre in enumerate(POSTRES, 1):
        print(f"\n{i}. {postre[0]}:")
        for ingrediente in postre[1]:
            print(f"   - {ingrediente}")

def ver_ingredientes(POSTRES):
    ver_postres(POSTRES)
    if not POSTRES:
        return
    try:
        indice = int(input("\nIngrese el número del postre: ")) - 1
        if 0 <= indice < len(POSTRES):
            print(f"\nIngredientes de {POSTRES[indice][0]}:")
            for ingrediente in POSTRES[indice][1]:
                print(f"- {ingrediente}")
        else:
            print("\nNúmero de postre inválido.")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

def agregar_postre(POSTRES):
    nombre = input("\nIngrese el nombre del postre: ").strip()
    # Verificar si el postre ya existe
    if any(postre[0].lower() == nombre.lower() for postre in POSTRES):
        print("\nEste postre ya existe.")
        return
    
    ingredientes = []
    print("\nIngrese los ingredientes (presione Enter sin texto para terminar):")
    while True:
        ingrediente = input("- ").strip()
        if not ingrediente:
            break
        if ingrediente.lower() not in [i.lower() for i in ingredientes]:
            ingredientes.append(ingrediente)
    
    if ingredientes:
        POSTRES.append([nombre, ingredientes])
        POSTRES.sort(key=lambda x: x[0].lower())  
        print(f"\nPostre '{nombre}' agregado exitosamente.")
    else:
        print("\nNo se agregó el postre porque no se ingresaron ingredientes.")

def agregar_ingredientes(POSTRES):
    ver_postres(POSTRES)
    if not POSTRES:
        return
    try:
        indice = int(input("\nIngrese el número del postre: ")) - 1
        if 0 <= indice < len(POSTRES):
            print("\nIngrese los nuevos ingredientes (presione Enter sin texto para terminar):")
            while True:
                ingrediente = input("- ").strip()
                if not ingrediente:
                    break
                if ingrediente.lower() not in [i.lower() for i in POSTRES[indice][1]]:
                    POSTRES[indice][1].append(ingrediente)
                else:
                    print(f"El ingrediente '{ingrediente}' ya existe en este postre.")
            print(f"\nIngredientes actualizados para {POSTRES[indice][0]}")
        else:
            print("\nNúmero de postre inválido.")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

def eliminar_ingrediente(POSTRES):
    ver_postres(POSTRES)
    if not POSTRES:
        return
    try:
        indice = int(input("\nIngrese el número del postre: ")) - 1
        if 0 <= indice < len(POSTRES):
            print("\nIngredientes actuales:")
            for i, ingrediente in enumerate(POSTRES[indice][1], 1):
                print(f"{i}. {ingrediente}")
            
            ing_indice = int(input("\nIngrese el número del ingrediente a eliminar: ")) - 1
            if 0 <= ing_indice < len(POSTRES[indice][1]):
                ingrediente_eliminado = POSTRES[indice][1].pop(ing_indice)
                print(f"\nSe eliminó '{ingrediente_eliminado}' de {POSTRES[indice][0]}")
            else:
                print("\nNúmero de ingrediente inválido.")
        else:
            print("\nNúmero de postre inválido.")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

def eliminar_postre(POSTRES):
    ver_postres(POSTRES)
    if not POSTRES:
        return
    try:
        indice = int(input("\nIngrese el número del postre a eliminar: ")) - 1
        if 0 <= indice < len(POSTRES):
            postre_eliminado = POSTRES.pop(indice)
            print(f"\nSe eliminó el postre '{postre_eliminado[0]}' y todos sus ingredientes.")
        else:
            print("\nNúmero de postre inválido.")
    except ValueError:
        print("\nPor favor, ingrese un número válido.")

def eliminar_repetidos(POSTRES):
    postres_unicos = []
    nombres_vistos = set()
    postres_eliminados = []

    for postre in POSTRES:
        nombre_lower = postre[0].lower()
        if nombre_lower not in nombres_vistos:
            postres_unicos.append(postre)
            nombres_vistos.add(nombre_lower)
        else:
            postres_eliminados.append(postre[0])
    
    POSTRES[:] = postres_unicos  
    
    if postres_eliminados:
        print("\nSe eliminaron los siguientes postres repetidos:")
        for postre in postres_eliminados:
            print(f"- {postre}")
    else:
        print("\nNo se encontraron postres repetidos.")

def main():
    POSTRES = []  
    
    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            ver_postres(POSTRES)
        elif opcion == "2":
            ver_ingredientes(POSTRES)
        elif opcion == "3":
            agregar_postre(POSTRES)
        elif opcion == "4":
            agregar_ingredientes(POSTRES)
        elif opcion == "5":
            eliminar_ingrediente(POSTRES)
        elif opcion == "6":
            eliminar_postre(POSTRES)
        elif opcion == "7":
            eliminar_repetidos(POSTRES)
        elif opcion == "8":
            print("\n¡Gracias por usar el sistema! Hasta luego.")
            break
        else:
            print("\nOpción inválida. Por favor, seleccione una opción válida (1-8).")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()