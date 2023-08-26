
'''
valor_1=10
valor_2=5

print(f"el primer valor es {valor_1} y el segundo valor es {valor_2}")
print(f" La suma de los valores es {valor_1+ valor_2}")
'''

Cadena='''
Por favor, ingresa una frase, el programa contará el número de caracteres
'''
print (Cadena)

frase=input("Por favor ingrese una frase")

print (frase)

frase_con_espacio=len(frase)
frase_sin_espacio=len(frase.replace(" ",""))
palabras =(frase_con_espacio-frase_sin_espacio)+1

print ("mi frase sin espacios tiene", frase_sin_espacio, "caracteres")
print("mi frase con espacios tiene", frase_con_espacio, "caracteres")
print (f"la frase ingresada tiene {palabras} palabra(s)")


cad= "Nueva cadena de texto"
print ("x" in cad)
print (type("x" in cad))