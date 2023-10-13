import csv
from Red import modelo
import random
import tkinter as tk
from tkinter import messagebox
from pomegranate import *
from Logica import *

archivo_usuarios = "C:\\Users\\vanea\\OneDrive - Universidad Nacional de Colombia\\Vanessa\\IA\MatchAI (4)\\Base_de_datos.csv"
archivo_preferencias = "C:\\Users\\vanea\\OneDrive - Universidad Nacional de Colombia\\Vanessa\\IA\\MatchAI (4)\\Preferencias.csv"

def cargar_datos():
    with open(archivo_usuarios, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Salta la primera fila de encabezado
        usuarios = [row for row in reader]

    with open(archivo_preferencias, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Salta la primera fila de encabezado
        preferencias = [row for row in reader]

    return usuarios, preferencias

def crear_modelo_probabilistico(usuarios,usuario_ide, preferencias):
    preferencias_usuario = {} 
    for row in preferencias:
        usuario_id, genero_mio, orientacion_sexual, estado_civil = row
        if int(usuario_ide) == int(usuario_id):
            f = orientacion_sexual  #realmente es orientacion sexual
            t = estado_civil #realmente es estado civil
            g = genero_mio    
    for row in usuarios:
        usario_id,nombre,_,edad,contextura,genero,orientacion_sexual,estatura,estado_civil,_ = row
        v1, v2 = logica_He(f,g,orientacion_sexual,genero)
        v3, v4 = logica_Ho(f,g,orientacion_sexual,genero)
        v5 = estSol(estado_civil)
        v6 = estDiv(estado_civil)
        v7,v8 = estViu(estado_civil)
        
        if f == 'heterosexual' and t == 'soltero':
            if not v1 and v2 and not v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'heterosexual' and t == 'casado':
            if not v1 and v2 and v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'heterosexual' and t == 'divorciado':
            if not v1 and not v6:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'heterosexual' and t == 'viudo':
            if not v1 and not (v7 or v8):
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'homosexual' and t == 'soltero':
            if v3 and v4 and not v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'homosexual' and t == 'casado':
            if v3 and v4 and v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'homosexual' and t == 'divorciado':
            if v3 and v4 and not v6:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'homosexual' and t == 'viudo':
            if v3 and v4 and not (v7 or v8):
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'bisexual' and t == 'soltero':
            if not v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'bisexual' and t == 'casado':
            if v5:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'bisexual' and t == 'divorciado':
            if not v6:
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)
        elif f == 'bisexual' and t == 'viudo':
            if not (v7 or v8):
                preferencias_usuario[usario_id] = (estado_civil, orientacion_sexual, nombre, edad, contextura, estatura)

    return preferencias_usuario

def encontrar_compatibilidad(usuario_id, modelo,  preferencias_usuario ):

    x = list(preferencias_usuario.keys())
    com = {}
    for i in range(len(x)):
        if int(x[i]) == int(usuario_id):
            continue
        estado_civil,orientacion_sexual,nombre,edad,contextura,estatura = preferencias_usuario[x[i]] 
        #print(estado_civil,orientacion_sexual)
        prediccion = modelo.predict_proba({"estado_civil": estado_civil, "orientacion_sexual": orientacion_sexual,"edad":edad,"contextura":contextura,"estatura":estatura})

        L = {}
        for nodo, prediccion in zip(modelo.states, prediccion):
             if nodo.name == 'compatibilidad':
                for valor, probabilidad in prediccion.parameters[0].items(): 
                    L[f"{valor}"] = probabilidad
                v = max(L,key=L.get)
                if str(v) == 'sí':
                    com[x[i]] = (nombre,L[v])
    return com

def main(usuario_id):
    usuarios, preferencias = cargar_datos()
    preferencias_usuario = crear_modelo_probabilistico(usuarios,usuario_id, preferencias)
    # if usuario_id not in list(preferencias_usuario.keys()):
    #         print("Usuario no encontrado. Inténtalo de nuevo.")
    # else:
    compatibilidad = encontrar_compatibilidad(usuario_id, modelo,  preferencias_usuario)
    for i in compatibilidad:
        print(f"Compatibilidad para {i}, con el nombre {compatibilidad[i][0]}: {round(compatibilidad[i][1],2)}")
        #print(f"Compatibilidad para {usuario_id}: {compatibilidad}")
        

if __name__ == "__main__":
    main()





