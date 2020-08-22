
lista = []
suma = 0
promedio = 0

nombre = input("Por favor ingrese su nobmre: ")

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
    

print(f"El alumno {nombre} obtuvo las siguientes notas: {lista}")
print(f"El alumno {nombre} obtuvo el siguiente promedio: {promedio}")
print(f"Del alumno {nombre} su nota más baja fue: {min(lista)}")
print(f"Del alumno {nombre} su nota más alta fue: {max(lista)}")

