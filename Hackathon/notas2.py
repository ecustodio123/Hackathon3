
lista = []
lista_nombres = []
tupla = ()
suma = 0
promedio = 0

while True:
    try:
       cantidad_alumnos = int(input("¿Cuántos alumnos va Ingresar? "))
       break
    except ValueError:
        print("Debes ingresar un numero, NO texto")

for i in range(cantidad_alumnos):

    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    lista_nombres.append(nombre)

    for i in range(5):
        while True: 
            try:
                nota = int(input("Por favor ingrese la nota: "))
                if(nota > 20 or nota < 0):
                    print("Tiene que ingresar una nota entre 0 al 20")
                else:    
                    lista.append(nota)
                    break
            except ValueError:
                print("Debes ingresar un numero, NO un texto. Por favor intentalo nuevamente")

        suma = suma + lista[i]

    promedio = (suma / len(lista))

    diccionario = {
                    nombre: {
                        "Notas: " : lista,
                        "Promedio: " : promedio,
                        "Nota Min: " : min(lista),
                        "Nota Max: " : max(lista)
                    }
    }

    print("###########################################################")
    print(diccionario)
    print("###########################################################")
    
    # print("###########################################################")
    # print(f"El alumno {nombre} obtuvo las siguientes notas: {lista}")
    # print(f"El alumno {nombre} obtuvo el siguiente promedio: {promedio}")
    # print(f"Del alumno {nombre} su nota más baja fue: {min(lista)}")
    # print(f"Del alumno {nombre} su nota más alta fue: {max(lista)}")
    # print("###########################################################")

    lista.clear()
    suma = 0

tupla = tuple(lista_nombres)

print(tupla)