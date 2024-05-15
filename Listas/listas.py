#             0     1  2   
#            -3      -2    -1
lista = ["Sergio",80,1.92]
print(lista)

lista_cursos = ["Python", "Django", "Flask", "Rubi", "Java"]

primer_curso = lista_cursos[0]
print(primer_curso)

segundo_curso = lista_cursos[1]
print(segundo_curso)

ultimo_curso = lista_cursos[-1]
print(ultimo_curso)


print(lista_cursos[-3]) #Flask


lista_cursos[-1] = 'Rust'
print(lista_cursos[4])


sub_lista = lista_cursos[0:3]
print(sub_lista)

#[start:] -> Obtenemos los último elementos de la lista
#[:end] -> Obtenemos los primeros elementos de la lista
#[start:end:step] 

sub_lista = lista_cursos[2:]
print(sub_lista)


sub_lista = lista_cursos[0:4:2]
print(sub_lista)

