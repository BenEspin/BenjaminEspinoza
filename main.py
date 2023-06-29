import Libreria

ciclo=True
while ciclo:
    try:
        print("Libreria Mayor")
        print("1)Grabar Libro")
        print("2)Buscar")
        print("3)Imprimir")
        print("4)Salir")
        op=(int(input("seleccione (1-4):")))
        match op:
            case 1:
                print("buscar Libros")
                print("1)Fantasia")
                print("2)Accion")
                print("3)Novela")
                print("4)Ficcion")
                op=int(input("seleccione (1-4):"))
                match op:
                    case 1:
                        if op ==1:

            case 2:

            case 3:

            case 4:
                ciclo=False
        except
        print("Opcion no valida")