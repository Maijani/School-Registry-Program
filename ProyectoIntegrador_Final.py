#---------
# LISTAS
#---------
lista_materias=[]
lista_alumnos=[]
lista_calificaciones=[]
lista_calificaciones_materias=[]
#---------
# COLOR
#---------
class ANSI(): 
    def color_text(code): 
        return "\33[{code}m".format(code=code)
#------------------
# ALUMNOS DEFS
#------------------
def imprimir_alumnos():
    print("1) Imprimir lista de alumnos \n")
    print ("\n{:<12} {:<10} {:<8} {:<12} {:<10}".format("Matricula","Nombre","Edad","Teléfono","Correo"))
    print ("{:<12} {:<10} {:<8} {:<12} {:<10}".format("--------","------","------","--------","------"))
    for i in range(0, len(lista_alumnos)):
        print("\n{:<12} {:<10} {:<8} {:<12} {:<10}".format(lista_alumnos[i][0],lista_alumnos[i][1],lista_alumnos[i][2],lista_alumnos[i][3],lista_alumnos[i][4]))

def agregar_alumnos():
    print("2) Agregar Alumno \n")
    a = input("Ingrese matricula del alumno. \n R = ")
    b = input("Ingrese nombre del alumno. \n R = ")
    c = input("Ingrese edad del alumno. \n R = ")
    d = input("Ingrese teléfono del alumno. \n R = ")
    e = input("Ingrese correo del alumno. \n R = ")
    lista_alumnos.append([a,b,c,d,e])
    lista_calificaciones.append([0])
    for i in range(0,len(lista_calificaciones_materias)):
        lista_calificaciones_materias[i].append(0)
    print("\nEsta es la información que ha sido agregada. \n\n ",a,b,c,d,e)

def modificar_alumnos():
    print("3) Modificar nombre alumno \n")
    nom=str(input("Ingrese matrícula del nombre de la persona que desea"+
    " modificar. \n R = "))
    new=str(input("Ingrese el nuevo nombre. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            lista_alumnos[i][1]= new
            print("\n",lista_alumnos[i],"\n")
            break 

def eliminar_alumnos():
    print("4) Eliminar Alumno \n")
    nom=str(input("Ingrese mátricula del alumno que desea eliminar. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            lista_alumnos.pop(i)
            lista_calificaciones.pop(i)
            for i in range(0, len(lista_calificaciones_materias)):
                del lista_calificaciones_materias[i][i]
                break
            break

def promedio_alumnos():
    print("5) Promedio de alumno \n")
    y=0
    nom=str(input("Ingrese matrícula del alumno del cual desea saber el" +
    " promedio. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            break
    for j in range(0, len(lista_materias)):
        y+=(lista_calificaciones[i][j])
    y=y/len(lista_materias)
    print("\nPromedio = ",y)

def reprobadas_alumno():
    print("6) Cuantos materias reprobo el alumno \n")
    y=0
    nom=str(input("Ingrese matrícula del alumno del cual desea saber las" +
    " materias que reprobo. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            break
    for j in range(0, len(lista_materias)):
        if lista_calificaciones[i][j]<70:
            y+=1
    print("\nReprobo",y,"materia/s.")
#------------------
# MATERIAS DEFS
#------------------
def imprimir_materias():
    print("1) Imprimir lista de materias \n")
    print ("\n{:<12} {:<10} {:<10} {:<10}".format("Materia","Clave","Maestro","Horario"))
    print ("{:<12} {:<10} {:<10} {:<10}".format("------","------","------","------"))
    for i in range(0, len(lista_materias)):
        print("\n{:<12} {:<10} {:<10} {:<10}".format(lista_materias[i][0],lista_materias[i][1],lista_materias[i][2],lista_materias[i][3]))

def agregar_materia():
    print("2) Agregar materia \n")
    a = input("Ingrese nombre de la materia. \n R = ")
    b = input("Ingrese clave de la materia. \n R = ")
    c = input("Ingrese nombre del maestro. \n R = ")
    d = input("Ingrese horario. \n R = ")
    lista_materias.append([a,b,c,d])
    lista_calificaciones_materias.append([])
    print("\nEsta es la información que ha sido agregada. \n\n ",a,b,c,d)

def modificar_materia():
    print("3) Modificar nombre materia \n")
    materia=str(input("Ingrese clave de la materia que desea modificar el" +
    " nombre \n R = "))
    new=str(input("Ingrese el nuevo nombre. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == materia:
            lista_materias[i][0]= new
            print("\n",lista_materias[i],"\n")
            break 

def eliminar_materia():
    print("\n 4) Eliminar materia \n")
    materia=str(input("Ingrese clave de la materia que desea eliminar \n"))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == materia:
            lista_materias.pop(i)
            lista_calificaciones_materias.pop(i)
            for j in range(0, len(lista_calificaciones)):
                del lista_calificaciones[j][i]
            print("\n",lista_materias,"\n")
            break

def promedio_materia():
    print("5) Promedio de la materia \n")
    y=0
    nom=str(input("Ingrese clave de la materia del cual desea saber el" +
    " promedio. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == nom:
            break
    for j in range(0, len(lista_alumnos)):
        y+=(lista_calificaciones[j][i])
    y=y/len(lista_alumnos)
    print("\nPromedio de",nom,"= ",y)

def reprobaron_materia():
    print("6) Cuantos alumnos reprobaron la materia\n")
    y=0
    nom=str(input("Ingrese clave de la materia del cual desea saber cuantos" +
    " reprobaron. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == nom:
            break
    for j in range(0, len(lista_alumnos)):
        if lista_calificaciones[j][i]<70:
            y+=1
    print("\nReprobaron",y,"alumnos.")

def calificacion_baja():
    print("7) Calificación más baja\n")
    nom=str(input("Ingrese clave de la materia del cual desea saber la " +
    "calificación mas baja. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == nom:
            a=(min(lista_calificaciones_materias[i]))
            for j in range(0,len(lista_materias)):
                if lista_calificaciones_materias[i][j] == a:
                    print ("\n{:<12} {:<10} {:<8}".format("Matricula",
                    "Nombre","Calificación"))
                    print ("{:<12} {:<10} {:<8}".format("------","------",
                    "------"))
                    print ("{:<12} {:<10} {:<8}".format(lista_alumnos[j][0],
                    lista_alumnos[j][1],a))
                    break
                break

def calificacion_alta():
    print("8) Calificación más alta\n")
    nom=str(input("Ingrese clave de la materia del cual desea saber la"+
    "calificación mas alta. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == nom:
            a=(max(lista_calificaciones_materias[i]))
            for j in range(0,len(lista_materias)):
                if lista_calificaciones_materias[i][j] == a:
                    print ("\n{:<12} {:<10} {:<8}".format("Matricula","Nombre","Calificación"))
                    print ("{:<12} {:<10} {:<8}".format("------","------","------"))
                    print ("{:<12} {:<10} {:<8}".format(lista_alumnos[j][0],lista_alumnos[j][1],a))
                    break
                break
#---------------------
# CALIFICACIONES DEFS
#----------------------
def calificaciones_materia():
    print("1) Imprimir calificaciones de materia\n") 
    nom=str(input("Ingrese clave de la materia que desea ver. \n R = "))
    for i in range(0, len(lista_materias)):
        if lista_materias[i][1] == nom:
            print ("\n{:<12} {:<10} {:<8}".format(lista_materias[i][0],
            lista_materias[i][1],lista_materias[i][2]))
            print ("{:<12} {:<10} {:<8}".format("------","------","------"))
            for j in range(0,len(lista_calificaciones)):
                print ("{:<12} {:<10} {:<8}".format(lista_alumnos[j][0],
                lista_alumnos[j][1],lista_calificaciones_materias[i][j]))
            break

def calificaciones_alumnos():
    print("2) Imprimir calificaciones de alumno\n")
    nom=str(input("Ingrese matricula del alumno que desea ver. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            print ("\n{:<10} {:<12}".format(lista_alumnos[i][1],
            lista_alumnos[i][0]))
            print ("{:<10} {:<12}".format("------","------"))
            for j in range(0,len(lista_materias)):
                print ("{:<10} {:<12} {:<8}".format(lista_materias[j][1],
                lista_materias[j][0],lista_calificaciones[i][j]))
            break

def agregar_calificaciones():
    print("3) Agregar calificaciones\n")
    nom=str(input("Ingrese matricula del alumno al que le desea agregar una" +
    " calificación. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            num=input("Ingrese la clave de la materia a la cual le quiere" +
            " agregar la calificación del alumno. \n R = ")
            for j in range(0, len(lista_materias)):
                if lista_materias[j][1] == num:
                    u=input("Escriba la calificación a añadir. \n R = ")
                    lista_calificaciones[i][j] = u
                    lista_calificaciones_materias[j][i] = u
                    print ("\n{:<10} {:<3}".format(lista_alumnos[i][1],
                    lista_alumnos[i][0]))
                    print (lista_calificaciones[i])
                    print ("\n{:<10} {:<3}".format(lista_materias[j][0],
                    lista_materias[j][1]))
                    print (lista_calificaciones_materias[j])
                    break

def modificar_calificaciones():
    print("4) Modificar calificacion\n")
    nom=str(input("Ingrese matricula del alumno al que le desea modificar" +
    " una calificación. \n R = "))
    for i in range(0, len(lista_alumnos)):
        if lista_alumnos[i][0] == nom:
            num=input("Ingrese la clave de la materia a la cual le" +
            " quiere modificar la calificación del alumno. \n R = ")
            for j in range(0, len(lista_materias)):
                if lista_materias[j][1] == num:
                    new=input("Escriba la nueva calificación. \n R = ")
                    lista_calificaciones[i][j]=new
                    lista_calificaciones_materias[j][i]=new
                    print ("\n{:<10} {:<3}".format(lista_alumnos[i][1],
                    lista_alumnos[i][0]))
                    print (lista_calificaciones[i])
                    print ("\n{:<10} {:<3}".format(lista_materias[j][0],
                    lista_materias[j][1]))
                    print (lista_calificaciones_materias[j])
                    break

#------------------
# REPORTES DEFS
#------------------
def menores_edad():
    print("3) Número de alumnos menores de edad.\n")
    a=0
    for i in range(0,len(lista_alumnos)):
        if lista_alumnos[i][2]<18:
            a+=1
    print("Hay",a,"alumno/s con minoria de edad.")

def promedio_edad():
    print("4) Promedio de edad de alumnos.\n")
    a=0
    for i in range(0,len(lista_alumnos)):
        a+=lista_alumnos[i][2]
    a=a/len(lista_alumnos)
    print(f"La edad promedio es {int(a)}.")

def total_alumnos():
    print("5) Total alumnos inscritos.\n")
    print(f"Hay {len(lista_alumnos)} alumnos inscritos.")

def total_materias():
    print("6) Total de materias que existen.\n")
    print(f"Hay {len(lista_materias)} materias.")

def reprobaron_tres():
    print("7) Lista de alumnos que reprobaron 3 materias o más.\n")
    y=0
    print ("\n{:<10} {:<3}".format("Nombre","Matricula"))
    print ("{:<10} {:<3}".format("------","--------"))
    for i in range(0, len(lista_alumnos)):
        for j in range(0,len(lista_materias)):
            if lista_calificaciones[i][j]<70:
                y+=1
                if y == 3:
                    print ("{:<10} {:<3}".format(lista_alumnos[i][1],
                    lista_alumnos[i][0]))
        y=0
#------------------
# SECONDARY MENUS
#------------------
# Menú de alumnos con respectivas funciones.
def alumnos():
    print(ANSI.color_text(35)+"1) Alumnos")
    opc=0
    while opc!= 7:
        print(ANSI.color_text(36)+"\n1) Imprimir lista de alumnos")
        print(ANSI.color_text(35)+"2) Agregar Alumno"
        +ANSI.color_text(31)+"(Agregar todas las materias antes de los alumnos)")
        print(ANSI.color_text(36)+"3) Modificar nombre alumno")
        print(ANSI.color_text(35)+"4) Eliminar Alumno")
        print(ANSI.color_text(36)+"5) Promedio de alumno")
        print(ANSI.color_text(35)+"6) Cuantos materias reprobo el alumno")
        print(ANSI.color_text(30)+"7) Regresar\n")
        opc = int(input(ANSI.color_text(37)+"Elige una de las opciones = "))
        print("\n")
        if opc == 1:
            imprimir_alumnos()
        elif opc == 2:
            agregar_alumnos()
        elif opc == 3:
            modificar_alumnos()
        elif opc == 4:
            eliminar_alumnos()
        elif opc == 5:
            promedio_alumnos()
        elif opc == 6:
            reprobadas_alumno()
        elif opc == 7:
            print("7) Regresar \n")
            break
        else:
            print ("\nERROR. Escribe una opción valida.\n")

# Menú de materias con respectivas funciones.
def materias():
    print(ANSI.color_text(36)+"2) Materias")
    op=0
    while op!= 9:
        print(ANSI.color_text(35)+"\n1) Imprimir lista de materias")
        print(ANSI.color_text(36)+"2) Agregar materia")
        print(ANSI.color_text(35)+"3) Modificar nombre materia")
        print(ANSI.color_text(36)+"4) Eliminar materia")
        print(ANSI.color_text(35)+"5) Promedio de la materia")
        print(ANSI.color_text(36)+"6) Cuantos alumnos reprobaron la materia")
        print(ANSI.color_text(35)+"7) Calificación más baja")
        print(ANSI.color_text(36)+"8) Calificación más alta")
        print(ANSI.color_text(30)+"9) Regresar\n")
        op = int(input(ANSI.color_text(37)+"Elige una de las opciones = "))
        print("\n")
        if op == 1:
            imprimir_materias()
        elif op == 2:
            agregar_materia()
        elif op == 3:
            modificar_materia()
        elif op == 4:
            eliminar_materia()
        elif op == 5:
            promedio_materia()
        elif op == 6:
            reprobaron_materia()
        elif op == 7:
            calificacion_baja()
        elif op == 8:
            calificacion_alta()
        elif op == 9:
            print("9) Regresar \n")
            break
        else:
            print ("\nERROR. Escribe una opción valida.\n")

# Menú de calificaciones con respectivas funciones.
def calificaciones():
    print(ANSI.color_text(35)+"3) Calificaciones")
    opci=0
    while opci!= 5:
        print(ANSI.color_text(36)+"\n1) Imprimir calificaciones de materia")
        print(ANSI.color_text(35)+"2) Imprimir calificaciones de alumno")
        print(ANSI.color_text(36)+"3) Agregar calificaciones")
        print(ANSI.color_text(35)+"4) Modificar calificacion")
        print(ANSI.color_text(30)+"5) Regresar\n")
        opci = int(input(ANSI.color_text(37)+"Elige una de las opciones = "))
        print("\n")
        if opci == 1:
            calificaciones_materia()
        elif opci == 2:
            calificaciones_alumnos()
        elif opci == 3:
            agregar_calificaciones()
        elif opci == 4:
            modificar_calificaciones()
        elif opci == 5:
            print("5) Regresar \n ଘ(੭ˊᵕˋ)੭* ੈ✩‧₊\n")
            break
        else:
            print ("\nERROR. Escribe una opción valida.\n")

# Menú de reportes con respectivas funciones.
def Reportes():
    print(ANSI.color_text(36)+"4) Reportes")
    opcio=0
    while opcio!= 8:
        print(ANSI.color_text(35)+"\n1) Promedio de alumno.")
        print(ANSI.color_text(36)+"2) Promedio de materia.")
        print(ANSI.color_text(35)+"3) Número de alumnos menores de edad.")
        print(ANSI.color_text(36)+"4) Promedio de edad de alumnos.")
        print(ANSI.color_text(35)+"5) Total alumnos inscritos.")
        print(ANSI.color_text(36)+"6) Total de materias que existen.")
        print(ANSI.color_text(35)+"7) Lista de alumnos que reprobaron 3 materias o más.")
        print(ANSI.color_text(30)+"8) Regresar\n")
        opcio = int(input(ANSI.color_text(37)+"Elige una de las opciones = "))
        print("\n")
        if opcio == 1:
            promedio_alumnos()
        elif opcio == 2:
            promedio_materia()
        elif opcio == 3:
            menores_edad()
        elif opcio == 4:
            promedio_edad()
        elif opcio == 5:
            total_alumnos()
        elif opcio == 6:
            total_materias()
        elif opcio == 7:
            reprobaron_tres()
        elif opcio == 8:
            print("8) Regresar \n")
            break
        else:
            print ("\nERROR. Escribe una opción valida.\n")
#---------------
# MENU PRINCIPAL
#---------------
# Imprime el menú principal con 5 opciones. Cada una lleva a otro menú y la última cierra el menú.
# esta colocado hasta abajo para poder leer las funciones.
opcion=0
while opcion!= 5:
    print(ANSI.color_text(36)+"\n1) Alumnos")
    print(ANSI.color_text(35)+"2) Materias")
    print(ANSI.color_text(36)+"3) Calificaciones")
    print(ANSI.color_text(35)+"4) Reportes")
    print(ANSI.color_text(30) + "5) Terminar Programa")
    opcion = int(input(ANSI.color_text(37)+"Elige una de las opciones = "))
    print("\n")
    # Escribir 1 imprime menú de alumnos.
    if opcion == 1:
        alumnos()
    # Escribir 2 imprime menú de materias.
    elif opcion == 2:
        materias()
    # Escribir 3 imprime menú de calificaciones.
    elif opcion == 3:
        calificaciones()
    # Escribir 4 imprime menú de reportes.
    elif opcion == 4:
        Reportes()
    # Escribir 5 termina el menú.
    elif opcion == 5:
        print("\n5) Terminar Programa\n")
        opcion = 5
    # Escribir cualquier otra cosa no avanza a ningun lado.
    else:
        print (ANSI.color_text(31)+"\nERROR. Escribe una opción valida.\n")