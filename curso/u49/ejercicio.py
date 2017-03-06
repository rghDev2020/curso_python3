#!/usr/bin/env python
import csv
def LeerPartidos():
	datos=[]
	keys=["fecha","equipo1","equipo2","final","mitad"]
	fichero = open("liga.csv")
	contenido = csv.reader(fichero)
	for row in list(contenido)[1:]:
		partido=dict(zip(keys,row))
		datos.append(partido)
	fichero.close()
	return datos

def Equipos(liga):
	return(tuple(set([partido["equipo1"] for partido in liga])))

def InfoEquipos(liga,*equipos):
	resultados=[]
	for equipo in equipos:
		resultado = [0,0,0]
		for partido in liga:
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==1:
				resultado[0]+=1
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==-1:
				resultado[1]+=1
			if partido["equipo1"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==-1:
				resultado[0]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==1:
				resultado[1]+=1
			if partido["equipo2"]==equipo and QuienGana(partido["final"])==0:
				resultado[2]+=1
		resultado.append(Puntos(resultado))
		resultado.insert(0,equipo)
			
		resultados.append(tuple(resultado))
	return resultados

	
def QuienGana(resultado):
	golescasa=int(resultado.split("-")[0])
	golesvisitante=int(resultado.split("-")[1])
	if golescasa==golesvisitante:
		return 0
	elif golescasa>golesvisitante:
		return 1
	else:
		return -1

def Puntos(info):
	return 3*info[0]+info[2]

def Clasificacion(datos):
	datos_ordenados=datos[:]
	datos_ordenados.sort(key=lambda datos: datos[4],reverse=True)
	return datos_ordenados

def impClasificacion(liga):
	datos=InfoEquipos(liga,*Equipos(liga))
	print(datos)
	print(Clasificacion(datos))
	contador=1
	line = '-' * 61
	print(line)
	print("|   №    |     Equipo      |   PG   |   PP  |  PE   |Puntos |")
	print(line)
	for dato in Clasificacion(datos):
		print('| {0:^6} | {1:^15} | {2:^6} |{3:^6} |{4:^6} |{5:^6} |'.format(contador,dato[0],dato[1],dato[2],dato[3],dato[4]))
		contador+=1
	print(line)


if __name__ == '__main__':
	liga=LeerPartidos()
	impClasificacion(liga)






