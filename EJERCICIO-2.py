#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

"""monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))"""

#Mostrar el precio del IVA 21% de un producto con un valor de 100 y su precio final.

producto = 325
iva = 21
ivaProducto = (producto / 100 * iva)
precioTotalProducto = (producto + ivaProducto)
print("El IVA del producto es: " + str(ivaProducto))
print("El precio total del producto es: " + str(producto + ivaProducto)) 

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.

materias = () 
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
for materias in subjects:
    print("yo estudio " + materias)