numero_magico = 12345679
numero_usuario = int(input("Dame un número entre 1 y 8:"))
if  numero_usuario > 8 :
  print("ERROR")
  
elif numero_usuario < 1 :
  print("ERROR")

nuevo_numero = (9*numero_usuario)*(numero_magico)

print(nuevo_numero)