lista = [1,6,4,8,3,14,1,3]

print("Lista inicial",lista)

print("\n")

def modificar(lista):
  lista.sort(reverse=True)

  nueva_lista = []
  for i in lista:
    if i % 2 == 0:
      nueva_lista.append(i)
      
  print("El sumatorio es =",sum(nueva_lista))
  nueva_lista.insert(0,sum(nueva_lista))
  return(nueva_lista)

print(modificar(lista))

new_lista = modificar(lista)
print("La comparación es =",new_lista[0]==sum(new_lista[1:]))