'''
Noviembre de 2022
Proyecto de Curso
Integrantes:
  Jonatan David Chavarriaga Chavarriaga

  Fredy Hernando Quintero Salazar

  Gabriel Arturo Oquendo Hernández

  Ferney Enrique Avila Benitez
  Métodos Numéricos Grupo 505 - 506
===================================================================
===================================================================
DESCRIPCIÓN DE LA TAREA
=======================
PROYECTO DE CURSO: Por medio del método de diferencias finitas resolver los diversos casos presentados en el documento

  - Se plantea la EDP de Laplace mediante el método de diferencias finitas presentado en clase, el método consta de 3 aproximaciones, pero para el caso
  se resolverá utilizando la discretización centrada de los dos términos de la ecuación. Para ello fue necesario mediante un analísis simplificar dicha ecuación
  asociandola al problema dado.

===================================================================
===================================================================
'''

import Casos as ca

def case(c):
  msg = ''
  if c == 1:
    # Se definen las condiciones de frontera
    print(ca.casoa(1, 0, 0, 0))
  elif c == 2:
    print('\nDigite las condiciones de forntera a continuación:')
    a = float(input('\ta: '))
    b = float(input('\tb: '))
    c = float(input('\tc: '))
    d = float(input('\td: '))
    print(ca.casob(a, b, c, d))
  elif c == 3:
    print(ca.casoc(1, 0, 0, 0))
  elif c == 4:
    print('\nDigite las condiciones de forntera a continuación:')
    a = float(input('\ta: '))
    b = float(input('\tb: '))
    print(ca.casod(a, b, 0, 0))
  elif c == 5:
    msg = '\n\tHas salido del programa.'
    return msg

print('A continuación se ejecutará el método de diferencias finitas para resolver la EDP de Laplace, para ello se plantean diferentes condiciones de frontera que están especificadas en el documento propuesto. Seleccione alguno de los casos a ejecutar.')
print('\n\t1. Caso a\n\t2. Caso b\n\t3. Caso c\n\t4. Caso d\n\t5. Salir')
opcion = int(input('\nSeleccione una opción: '))
print(case(opcion))
while opcion != 5:
  print('Selecciones alguno de los casos a ejecutar. ')
  print('\n\t1. Caso a\n\t2. Caso b\n\t3. Caso c\n\t4. Caso d\n\t5. Salir')
  opcion = int(input('\nSeleccione una opción: '))
  print(case(opcion))
