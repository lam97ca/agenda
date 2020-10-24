#Universidad Central de Venezuela
#Programación (0790)
#Autor : Laura M. Castillo G. C.I.: 25210846 github: lam97ca
#Descripción: Agenda telefónica básica

#Para cronometrar la duración de la estadia en partes de la agenda en python se debe importar el siguiente módulo
import time
#Para crear un archivo dentro de la carpeta en python se debe importar el siguiente módulo
import os
import copy

def crear_contacto(agenda_path):
    """Esta función agrega un contacto a una agenda, con nombre, telefono y direccion"""
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el telefono de {} :".format(nombre))
    direccion = input("Ingrese la dirección de {} :".format(nombre))
#datos del contacto dados por el usuario
    contacto = {'Nombre':nombre, 'Telefono': telefono, 'Direccion': direccion}
    #diccionario con los datos del contacto
    agenda = descargar_agenda(agenda_path)
    #se abre la agenda
    if len(agenda.keys()) == 0:
        id_contact = '0-0001'
    else:
        last_contact = int(list(agenda.keys())[-1].split('-')[-1])+1
        last_contact = (4-len(str(last_contact)))*'0'+str(last_contact)
        id_contact = '0-{}'.format(last_contact)
#se crea un numero de identificacion para c/contacto, dependiendo si es el primer contacto o hay mas
    agenda.update( {id_contact:contacto} )
#se guarda el contacto en la agenda
    cargar_agenda(agenda_path,agenda)

def eliminar_contacto(agenda_path):
    """Esta función elimina un contacto de una agenda"""
    Flag = True
    while Flag:
        nombre = input("Indique nombre (o parte del nombre) del contacto que desea eliminar de la agenda: ")
        agenda = descargar_agenda(agenda_path)
        print("Identifique el id del usuario que desea eliminar.")
        for element_key,element in buscar(agenda, nombre.lower()):
            print('id: {}\t nombre: {}'.format(element_key, element))

        ids = input("Ingrese el id del contacto a eliminar de la agenda: ")
        id_list = []
        value_list = []
        if ids in agenda.keys():
        	for key in agenda.keys():
        		id_list.append(key)
        	del agenda[id]
        	for val in agenda.values():
        		value_list.append(val)
        	agenda.clear()
        	for ids_v in range(len(id_list)-1):
        		agenda[id_list[ids_v]] = value_list[ids_v]
        	cargar_agenda(agenda_path,agenda)
        else:
        	raise ValueError("Error id no existe")
        
        continuar =  input("Desea eleminar otro contacto? ( opciones 's' o 'n'):")
        if continuar.lower() == 'n':
            Flag = False
        elif continuar.lower() != 's':
            raise ValueError("Error, las opciones válidas son 's' o 'n'.")

def editar_contacto(agenda_path):
	"""Esta funcion edita un contacto existente dentro de la agenda"""
	contacto_mod = input('Contacto a modificar: ')
	#que contacto quiere modificar el usuario
	agenda = descargar_agenda(agenda_path)
	if contacto_mod not in agenda:
		print ('El contacto no existe, agreguelo desde el menu')
		continue
		#por si el contacto no esta agendado
	for i in range(len(agenda)):
	          if agenda[i][0] == nombre:
	          	index = i
	          	break
	          if index != None:
	          	print('Omite aquellos campos que no quieras editar para conservar los datos')
	          	nombre = input('Nombre:')
	          	telefono = input('Telefono: ')
	          	direccion = input('Dirección')                
	          	contacto[index] = [
                        nombre if len(nombre) > 0 else agenda[index][0],
                        telefono if len(telefono) > 0 else agenda[index][1],
                        direccion if len(direccion) > 0 else agenda[index][2] ]
	          	cargar_agenda(agenda_path, agenda)
	          	print('Editado con exito!')
			             #modificar los datos del contacto que desea el usuario

def cargar_agenda(agenda_path, agenda):
    """La función cargar_agenda crea el archivo de texto donde se
    almacenará una agenda dada y escribe o sustituye su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""

    with open(agenda_path+'.txt', 'wt') as file:
        count = 0
        for id, contenido in zip(agenda.keys(), agenda.values()):
            if count == 0:
                id_tag = 'id:{}'.format(id)
                count += 1
            else:
                id_tag = '\nid:{}'.format(id)

            file.writelines([id_tag,'\n\tContacto:{}'.format(contenido['Nombre']),\
            '\n\tTelefono:{}'.format(contenido['Telefono']),'\n\tDireccion:{}'.format(contenido['Direccion'])])



def descargar_agenda(agenda_path):
    """La función descargar_agenda busca el archivo de texto donde se
    encuentra almacenada una agenda dada y descarga su contenido. Se pasa
    como argumento la ruta donde está la agenda y la variable asociada al
    contacto a modificar."""
    agenda = {}
    with open(agenda_path+'.txt', 'r') as file:
        content = file.read().split('\n')
        if content != ['']:
            for i in range(0,len(content),4):
                id = content[i].split(':')[1]
                nombre = content[i + 1].split(':')[1]
                telefono = content[i + 2].split(':')[1]
                direccion = content[i + 3].split(':')[1]
                contacto = {'Nombre': nombre, 'Telefono': telefono, 'Direccion': direccion}
                agenda.update( {id: contacto} )

    return agenda

def crear_si_no_existe(agenda_path):
    """La funcion crear_si_no_existe funcion crea de forma segura el archivo agenda.txt. La
    implementacion se realiza sin importar ningun modulo de python, además, se
    al final del subprograma en comentarios se adjunto una implementacion
    importando el modulo os."""

    try:
        with open('agenda.txt', 'r') as file:
            pass
    except FileNotFoundError:
        with open('agenda.txt', 'w'):
            pass

def buscar(agenda, nombre):
    """La funcion busca dentro de los datos de la agenda el contacto que el usuario busca"""
    lista_id = []
    lista_nombre = []
    for id in agenda.keys():
        if nombre.lower() in agenda[id]['Nombre'].lower():
            lista_id.append(id)
            lista_nombre.append(agenda[id]['Nombre'])

    return zip(lista_id, lista_nombre)

def main():
    """La función main es la instancia principal del programa, utiliza el tipo
    de dato dict para representar la agenda telefónica, así como para
    representar los contactos. """
    
    crear_si_no_existe('agenda.txt')
    
    while(True):
    	print("Agenda telefónica básica")
    	try:
		    opcion=0
		    agenda=descargar_agenda(agenda_path)
		    while opcion != 6 :
		        print("Elige una opcion:")
		        print("1. Lista de contactos")
		        print("2. Buscar contacto")
		        print("3. Crear contactos")
		        print("4. Borrar contacto")
		        print("5. Editar contacto")
		        print("6. Salir")
		#Menu de la agenda
		        opcion=input("Opcion:")
		        if opcion == "1":
		            print(agenda)
		            time.sleep(4)
		            #muestra agenda
		        elif opcion== "2":
		            bus_cont=input("Introduce nombre a buscar:")
		            buscar(agenda, bus_cont)
		            time.sleep(4)
		            #busca contacto
		        elif opcion== "3":
		            crear_contacto(agenda_path)
		            time.sleep(4)
		            #crea contacto
		        elif opcion== "4":
		            eliminar_contacto (agenda_path)
		            time.sleep(4)
		            #elimina contacto
		        elif opcion == "5":
		        	editar_contacto(agenda_path)
		        	time.sleep(4)
		        	#edita contacto
		        elif opcion == "6":
		            print("He entrado en 6")   
		            break
		            #sale del menu
		        else:
		            print("Esa opción no esta contemplada")
		    print("Se cerro la agenda")
		    print("Fin del programa, gracias por utilizar la agenda")
    	except:
		pass
	
if __name__ == "__main__":
	main()
	
