def menu():
    print("\n\n---------------------------MENU DE LA LISTA DE PROTOCOLO---------------------------")
    print("1. Crear un archivo")
    print("                                    --------------------------                                   ")
    print("2. Ingresar datos al archivo creado")
    print("                                    --------------------------                                   ")
    print("3. Eliminar elemento")
    print("                                    --------------------------                                   ")
    print("4. Añadir un elemento a la lista")
    print("                                    --------------------------                                   ")
    print("5.Salir")
    print("                                    --------------------------                                   ")
    
while True:
    menu()
    op=int(input("Escoge una opcion: "))
    if op == 1:
        archivo1 = open("Protocolo.txt","w")
        print("\nEl archivo se ha creado con EXITO")
        archivo1.close()
        
    elif op == 2:
        longitud =int(input("¿Cuantos PUNTOS quiere almacenar en el protocolo? (No hay listas con decimales) "))
        Lnom=[]
        i=0
        print("\nESCRIBA LOS PUNTOS QUE DESEE INGRESAR: ")
        while i < longitud:
            Enom = input("Punto #"+str(i+1)+ ": ")
            Lnom.append(Enom)
            i = i + 1
            
        print("\nLa lista de PUNTOS ingresados es: ")
        for j in range (0,(len(Lnom))):
                print("Punto #"+str(j+1)+" : "  +Lnom[j]+".")
                archivo1 = open("Protocolo.txt","a")
                archivo1.write("Punto #"+str(j+1)+" : "+Lnom[j]+"." + "\n")
                archivo1.close()
        
    elif op == 3:
        delete=int(input("\nEscriba el numero del PUNTO que deseas eliminar del protocolo: \nConsidera que cuenta desde el 0 :))) sorry\n"))
        Lnom.pop(delete)

        archivo1=open("Protocolo.txt","a")
        archivo1.write("-----------------------------------------------------------\n")
        archivo1.close()
        
        print("\nLa lista modificada es: ")
        for m in range (0,(len(Lnom))):
            print("Punto #"+str(m+1)+" : "  +Lnom[m]+".")
            archivo1 = open("Protocolo.txt","a")
            archivo1.write("Punto #"+str(m+1)+" : "+Lnom[m]+"." + "\n")
            archivo1.close()

    elif op == 4:
        newN=input("\nEscriba un nuevo PUNTO que desee insertar en el protocolo: ")
        Lnom.append(newN)

        archivo1=open("Protocolo.txt","a")
        archivo1.write("-----------------------------------------------------------\n")
        archivo1.close()
            
        print("\nLa lista modificada es: ")
        for k in range (0,(len(Lnom))):
            print("Punto #"+str(k+1)+" : "  +Lnom[k]+".")
            archivo1=open("Protocolo.txt","a")
            archivo1.write("Punto #"+str(k+1)+" : "+Lnom[k]+"." + "\n")
            archivo1.close()

    elif op == 5:
        print("Hasta luego")
        break
    else:
        print("Opcion invalida") 
