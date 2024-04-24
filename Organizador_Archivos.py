#importacion de librerias
import os, shutil

#se crea un diccionario que contendra las extenciones que se desean archivar
extenciones = {
    "Fotos": ['.jpg','.png', '.jpeg', '.gif', '.JPG', '.PNG', '.JPEG'],
    "Videos": ['.mp4','.avi', '.wav'],
    "PDF": ['.pdf', '.PDF'],
    "Audios": ['.mp3'],
    "Comprimidos": ['.rar', '.zip'],
    "Word": ['.docx', '.dotx', '.doc'],
    "Excel" : ['.xls', '.xlsm', '.xlsx'],
    "PowerPoint": ['.ppt','.pptx'],
    "Notas": ['.txt'],
    "Ejecutables": ['.exe'],
    "Doc. Web": ['.htm', '.html'],
    "CSV": ['.csv', '.CSV', '.json', '.JSON']
}

#Definir las funciones

#Crear Capertas 
def crearCarpetas(path):
    exts = obtenerExtenciones(path)
    for i in extenciones.keys():
        for k in exts:
            if k in extenciones[i] and not os.path.exists(path+i):
                os.mkdir(path+i)

def ordenar (path, archivo, ext):
    for i in extenciones.keys():
        if ext in extenciones[i]:
            try:
                shutil.move(path+archivo, path+i)
            except:
                print(f"Ocurrio un error, no se pudo mover el archivo: {archivo}")
                

#Obtener todas las extenciones que existan en la carpeta a ordenar
def obtenerExtenciones(path):
    #se crea una lista vacia que se usara para listar las extenciones
    exts = []
    #Ciclo for que retorna una lista con todos los elementos/archivos que se encuentren en la carpeta
    for i in os.listdir(path):
        #Se separa el nombre del archivo y la extencion almacenando solo la extencion [0]= NombreArchivo [1]=Extencion
        ext = os.path.splitext(i)[1]
        if ext not in exts and ext !="":
            exts.append(ext)
            
    return exts
        

#Esta funcion hara todos los procesos que se le pida
def proceso(path):
    crearCarpetas(path)
    for archivo in os.listdir(path):
        ext = os.path.splitext(archivo)[1]
        ordenar(path, archivo, ext)
        

while True:
    #Se crea una variable para almacenar la direccion de la carpeta que se quiere ordenar
    path = input("Ingrese la direccion de la carpeta que desea ordenar: ")
    #Pregutamos si existe la direccion dada
    if os.path.exists(path):
        path += "/"
        break
    else:
        print("Error, la direccion ingresada no existe")
      
proceso(path)        
print("Proceso Finalizado")
