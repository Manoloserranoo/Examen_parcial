lista = [1,3,7,12,6,25]
def separar_lista(lista):
  lista_pares = []
  lista_impares = []
  
  for num in lista:
    if num % 2 == 0 :
      lista_pares.append(num)
    else:
      lista_impares.append(num)
  listas = print(lista_pares ,"\n",lista_impares)
  return listas

nuevas_listas = separar_lista(lista)

