def separar_pares(lista):
  nueva_lista = []
  for num in lista:
    if num % 2 == 0:
      nueva_lista.append(num)
  return nueva_lista

def separar_impares(lista):
  new_lista = []
  for num in lista:
    if num % 2 == 1:
      new_lista.append(num)
  return new_lista
lista = [1,5,7,8,12,24,11]
lista_pares = separar_pares(lista)
lista_impares = separar_impares(lista)

print(str(lista_pares))
print(str(lista_impares))