lista = [1,2,5,7,6,12,8]
lista.sort()
el=int(input("¿Que elemento quieres añadir?"))

def agregar_una_vez(lista,el):
  val=1
  for i in range(len(lista)):
    if el not in lista:
      lista.append(el)
  else:
    print("Error: Imposible añadir elementos duplicados =>",el)
    
    

  return lista



lista_unica = agregar_una_vez(lista,el)
print(lista_unica)
