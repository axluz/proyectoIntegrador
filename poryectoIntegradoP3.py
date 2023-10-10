# Para esta sección del proyecto integrador 
# necesitaremos aprender a manipular la terminal

# Iniciar con un número en 0, leer la tecla `n` del 
# teclado en un bucle, por cada presionada, borrar 
# la terminal y e imprimir el nuevo número hasta el número 50.

# La operación de borrar la terminal e imprimir el nuevo número 
# debe estar en su propia función.

import readchar
import os
def cls():
    for i in range(51):
        key = readchar.readkey()
        os.system('cls')
        print(f'presionaste:{key}', f'conta:{i}')

cls()
   
    