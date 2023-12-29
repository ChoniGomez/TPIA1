# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import matplotlib.pyplot as plt
import networkx as nx

class Arista:
  def __init__(self,maze1_F, maze1_C,maze2_F, maze2_C, maze1_Val, maze2_Val):
			self.maze1_F = maze1_F
			self.maze1_C = maze1_C
			self.maze2_F = maze2_F
			self.maze2_C = maze2_C
			self.maze1_Val = maze1_Val
			self.maze2_Val = maze2_Val

class Nodo:
  nivel: int
  ubiX: int
  ubiY: int
  nombre: str
  nombrePadre: str
  def __init__(self,nodoF, nodoC, nodoPadreF, nodoPadreC, estado, val):
			self.nodoF = nodoF
			self.nodoC = nodoC
			self.nodoPadreF = nodoPadreF
			self.nodoPadreC = nodoPadreC
			self.estado = estado
			self.val = val
			

def primeroEnAmplitud(aristas_G):
		ini=Nodo(9,9,"null","null","Libre","I")
		fin=Nodo(0,0,"null","null", "Libre","F")
		listaExplorar=[]				# Lista de Nodos a Explorar por el Algoritmo
		listaVerificados=[]				# Lista de Nodos Verificados/Explorados por el Algoritmo
		listaExplorar.append(ini)
		i=0
		a=1
		wall = 'x'
		listaEvolucion=[]
		listaEvolucion.append("*****************************")
		listaEvolucion.append("Iteración Nº"+str(a))
		listaEvolucion.append("Lista Verificados")
		listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
		listaEvolucion.append("Lista a Explorar")
		listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))
		while i<len(listaExplorar):
			if a>1 :
				listaEvolucion.append("*****************************")
				listaEvolucion.append("Iteración Nº"+str(a))
				listaEvolucion.append("Lista Verificados")
				listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
				listaEvolucion.append("Lista a Explorar")
				listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))

			nodoCambioEstado=listaExplorar.__getitem__(0)
			nodoCambioEstado.estado="Ocupado"
			listaVerificados.append(nodoCambioEstado)
			nodoActual=listaExplorar.__getitem__(0)
			del listaExplorar[0]
			if(nodoActual.val != wall):
				if nodoActual.nodoF==fin.nodoF and nodoActual.nodoC==fin.nodoC: 	#Verificación de el nodo actual es el nodo solución
					a=a+1
					listaEvolucion.append("*****************************")
					listaEvolucion.append("Iteración Nº"+str(a))
					listaEvolucion.append("Lista Verificados")
					listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
					listaEvolucion.append("Lista a Explorar")
					listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))
					resultado=[]
					resultado.append(listaExplorar)
					resultado.append(listaVerificados)
					resultado.append(listaEvolucion)
					return(resultado)	
				else:
					listaHijosOrdenada=[]
					listaHijosOrdenada.extend(buscarNodosHijos(nodoActual,aristas_G))		#Busqueda de los hijos del nodo actual de forma ordenada y sin hijo que haga volver hacia el Padre
					if len(listaHijosOrdenada) != 0:										#Verifica que posea hijos el nodo actual	
						listaRecibida=controlDeBucle1(listaExplorar,listaHijosOrdenada,listaVerificados)		#Se devuelve la LE anexado con los nodos Hijos que no estén en LV ni LE
						listaExplorar.clear()
						listaExplorar.extend(listaRecibida)
			a=a+1
		resultado=[]
		resultado.append(listaExplorar)
		resultado.append(listaVerificados)

		return(resultado)	

def conversor_Lista_Nodo_A_Texto(lista):
	linea="["
	indice=0
	for j in lista:
		if indice==0:
			linea=linea+str(j.nodoF)+","+str(j.nodoC)
			indice=1
		else:	
			linea=linea+"|"+str(j.nodoF)+","+str(j.nodoC)
	linea=linea+"]"
	return (linea)

def primeroEnProfundidad(aristas_G):
		ini=Nodo(9,9,"null","null","Libre","I")
		fin=Nodo(0,0,"null","null", "Libre","F")
		listaExplorar=[]				# Lista de Nodos a Explorar por el Algoritmo
		listaVerificados=[]				# Lista de Nodos Verificados/Explorados por el Algoritmo
		listaExplorar.append(ini)
		i=0
		a=1
		wall = 'x'
		listaEvolucion=[]
		listaEvolucion.append("*****************************")
		listaEvolucion.append("Iteración Nº"+str(a))
		listaEvolucion.append("Lista Verificados")
		listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
		listaEvolucion.append("Lista a Explorar")
		listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))
		while i<len(listaExplorar):
			if a>1 :
				listaEvolucion.append("*****************************")
				listaEvolucion.append("Iteración Nº"+str(a))
				listaEvolucion.append("Lista Verificados")
				listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
				listaEvolucion.append("Lista a Explorar")
				listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))

			nodoCambioEstado=listaExplorar.__getitem__(0)
			nodoCambioEstado.estado="Ocupado"
			listaVerificados.append(nodoCambioEstado)
			nodoActual=listaExplorar.__getitem__(0)
			del listaExplorar[0]
			if(nodoActual.val != wall):
				if nodoActual.nodoF==fin.nodoF and nodoActual.nodoC==fin.nodoC:		#Verificación de el nodo actual es el nodo solución
					a=a+1
					listaEvolucion.append("*****************************")
					listaEvolucion.append("Iteración Nº"+str(a))
					listaEvolucion.append("Lista Verificados")
					listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaVerificados))
					listaEvolucion.append("Lista a Explorar")
					listaEvolucion.append(conversor_Lista_Nodo_A_Texto(listaExplorar))
					resultado=[]
					resultado.append(listaExplorar)
					resultado.append(listaVerificados)
					resultado.append(listaEvolucion)
					return(resultado)	
				else:
					listaHijosOrdenada=[]
					listaHijosOrdenada.extend(buscarNodosHijos(nodoActual,aristas_G))
					if len(listaHijosOrdenada) != 0:
						listaRecibida=controlDeBucle2(listaExplorar,listaHijosOrdenada,listaVerificados)
						listaExplorar.clear()
						listaExplorar.extend(listaRecibida)
			a=a+1
		
		resultado=[]
		resultado.append(listaExplorar)
		resultado.append(listaVerificados)
		return(resultado)

def controlDeBucle1(listaExplorar2,listaHijosOrdenada2,listaVerificados2):
	listaExplorarSinBucle=[]
	
	for x in listaExplorar2: 	#Control de LH con LE
		a=0
		for j in listaHijosOrdenada2:
			if x.nodoF==j.nodoF and x.nodoC==j.nodoC:
				listaHijosOrdenada2.pop(a)
			a=a+1
		

	for k in listaVerificados2:		#Control de LH con LV
		a=0
		for j in listaHijosOrdenada2:
			if k.nodoF==j.nodoF and k.nodoC==j.nodoC:
				listaHijosOrdenada2.pop(a)
			a=a+1

	listaExplorarSinBucle.extend(listaExplorar2)
	listaExplorarSinBucle.extend(listaHijosOrdenada2)
	return(listaExplorarSinBucle)

def controlDeBucle2(listaExplorar2,listaHijosOrdenada2,listaVerificados2):
	listaVerificada=[]
	a=0
	for x in listaExplorar2:
		for j in listaHijosOrdenada2:
			if x.nodoF==j.nodoF and x.nodoC==j.nodoC:
				listaExplorar2.pop(a)
		a=a+1

	for k in listaVerificados2:
		a=0
		for j in listaHijosOrdenada2:
			if k.nodoF==j.nodoF and k.nodoC==j.nodoC:
				listaHijosOrdenada2.pop(a)
			a=a+1
	
	listaVerificada.extend(listaHijosOrdenada2)
	listaVerificada.extend(listaExplorar2)
	return(listaVerificada)

def buscarNodosHijos(nodoActual,aristas_G):
	wall = 'x'
	cell = '0'
	salida = 'F'
	listaHijos=[]
	listaHijosOrdenada3=[]
	for x in aristas_G:		#Busqueda de hijos en donde el nodo Actual puede aparecer del lado Izq como Der del par ordenado de aristas
		
		if nodoActual.nodoF==x.maze1_F and nodoActual.nodoC==x.maze1_C:
			if(x.maze2_Val==cell or x.maze2_Val==salida):
				nodoHijo=Nodo(x.maze2_F,x.maze2_C,nodoActual.nodoF,nodoActual.nodoC,"Libre",x.maze2_Val)
				listaHijos.append(nodoHijo)
			else:
				if (x.maze2_Val == wall):
					nodoHijo=Nodo(x.maze2_F,x.maze2_C,nodoActual.nodoF,nodoActual.nodoC,"Bloqueado",x.maze2_Val)
					listaHijos.append(nodoHijo)
		if nodoActual.nodoF==x.maze2_F and nodoActual.nodoC==x.maze2_C:
			if(x.maze1_Val==cell or x.maze1_Val==salida):
				nodoHijo=Nodo(x.maze1_F,x.maze1_C,nodoActual.nodoF,nodoActual.nodoC,"Libre",x.maze1_Val)
				listaHijos.append(nodoHijo)
			else:
				if (x.maze1_Val == wall):
					nodoHijo=Nodo(x.maze1_F,x.maze1_C,nodoActual.nodoF,nodoActual.nodoC,"Bloqueado",x.maze1_Val)
					listaHijos.append(nodoHijo)
	
	if len(listaHijos) != 0:		#Ordenamiento de la lista de hijos en Izq,Arr,Der,Abj
			izquierda=nodoActual.nodoC-1
			for j in listaHijos:
				if j.nodoC==izquierda:
					listaHijosOrdenada3.append(j)

			arriba=nodoActual.nodoF-1
			for j in listaHijos:
				if j.nodoF==arriba:
					listaHijosOrdenada3.append(j)

			derecha=nodoActual.nodoC+1
			for j in listaHijos:
				if j.nodoC==derecha:
					listaHijosOrdenada3.append(j)

			abajo=nodoActual.nodoF+1
			for j in listaHijos:
				if j.nodoF==abajo:
					listaHijosOrdenada3.append(j)
			a=0
			for j in listaHijosOrdenada3:		#Control entre el nodo hijo y nodo Padre del nodo Actual 
				if j.nodoF==nodoActual.nodoPadreF and j.nodoC==nodoActual.nodoPadreC:
					listaHijosOrdenada3.pop(a)
				a=a+1

	return (listaHijosOrdenada3)


# Find number of surrounding cells
def surroundingCells(rand_wall,maze1):
	s_cells = 0
	if (maze1[rand_wall[0]-1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze1[rand_wall[0]+1][rand_wall[1]] == '0'):
		s_cells += 1
	if (maze1[rand_wall[0]][rand_wall[1]-1] == '0'):
		s_cells +=1
	if (maze1[rand_wall[0]][rand_wall[1]+1] == '0'):
		s_cells += 1

	return s_cells
	

def generarLaberinto():
	wall = 'x'
	cell = '0'
	entrada = 'I'
	salida = 'F'
	unvisited = 'u'
	height = 10
	width = 10
	maze = []

	# Denote all cells as unvisited
	for i in range(0, height):
		line = []
		for j in range(0, width):
			line.append(unvisited)
		maze.append(line)

	# Randomize starting point and set it a cell
	starting_height = int(9)
	starting_width = int(9)
	if (starting_height == 0):
		starting_height += 1
	if (starting_height == height-1):
		starting_height -= 1
	if (starting_width == 0):
		starting_width += 1
	if (starting_width == width-1):
		starting_width -= 1

	# Mark it as cell and add surrounding walls to the list
	maze[starting_height][starting_width] = cell
	walls = []
	walls.append([starting_height - 1, starting_width])
	walls.append([starting_height, starting_width - 1])
	walls.append([starting_height, starting_width + 1])
	walls.append([starting_height + 1, starting_width])

	# Denote walls in maze
	maze[starting_height-1][starting_width] = 'x'
	maze[starting_height][starting_width - 1] = 'x'
	maze[starting_height][starting_width + 1] = 'x'
	maze[starting_height + 1][starting_width] = 'x'

	while (walls):
		# Pick a random wall
		rand_wall = walls[int(random.random()*len(walls))-1]

		# Check if it is a left wall
		if (rand_wall[1] != 0):
			if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == '0'):
				# Find the number of surrounding cells
				s_cells = surroundingCells(rand_wall,maze)

				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])


					# Bottom cell
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):	
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
				

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check if it is an upper wall
		if (rand_wall[0] != 0):
			if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == '0'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					# Upper cell
					if (rand_wall[0] != 0):
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

					# Leftmost cell
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])

					# Rightmost cell
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Check the bottom wall
		if (rand_wall[0] != height-1):
			if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == '0'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[1] != 0):
						if (maze[rand_wall[0]][rand_wall[1]-1] != '0'):
							maze[rand_wall[0]][rand_wall[1]-1] = 'x'
						if ([rand_wall[0], rand_wall[1]-1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]-1])
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)


				continue

		# Check the right wall
		if (rand_wall[1] != width-1):
			if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == '0'):

				s_cells = surroundingCells(rand_wall,maze)
				if (s_cells < 2):
					# Denote the new path
					maze[rand_wall[0]][rand_wall[1]] = '0'

					# Mark the new walls
					if (rand_wall[1] != width-1):
						if (maze[rand_wall[0]][rand_wall[1]+1] != '0'):
							maze[rand_wall[0]][rand_wall[1]+1] = 'x'
						if ([rand_wall[0], rand_wall[1]+1] not in walls):
							walls.append([rand_wall[0], rand_wall[1]+1])
					if (rand_wall[0] != height-1):
						if (maze[rand_wall[0]+1][rand_wall[1]] != '0'):
							maze[rand_wall[0]+1][rand_wall[1]] = 'x'
						if ([rand_wall[0]+1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]+1, rand_wall[1]])
					if (rand_wall[0] != 0):	
						if (maze[rand_wall[0]-1][rand_wall[1]] != '0'):
							maze[rand_wall[0]-1][rand_wall[1]] = 'x'
						if ([rand_wall[0]-1, rand_wall[1]] not in walls):
							walls.append([rand_wall[0]-1, rand_wall[1]])

				# Delete wall
				for wall in walls:
					if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
						walls.remove(wall)

				continue

		# Delete the wall from the list anyway
		for wall in walls:
			if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
				walls.remove(wall)
		


	# Mark the remaining unvisited cells as walls
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				maze[i][j] = 'x'

	# Set entrance and exit
	for i in range(0, width):
		if (maze[1][i] == '0'):
			maze[0][i] = '0'
			break

	for i in range(width-1, 0, -1):
		if (maze[height-2][i] == '0'):
			maze[height-1][i] = '0'
			break
	al = random.randint(2,7)
	for i in range(1,al):
		maze[al][i] = cell

	maze[0][0] = salida
	maze[9][9] = entrada
	maze[0][1] = cell
	maze[9][8] = cell

	return maze

def crearAristas(maze):
	wall = 'x'
	entrada = 'I'
	salida = 'F'
	cell = '0'
	aristas_G2=[]
	for f in range(10):			#Creación del par ordenado de aristas con las posiciones
		for c in range(10):
			if maze[f][c]==cell:
				abajo=f+1
				derecha=c+1
				if derecha <= 9 and	maze[f][derecha]==cell:
					a=Arista(f,c,f,derecha,cell,cell)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==cell:
					a=Arista(f,c,abajo,c,cell,cell)
					aristas_G2.append(a)

				if derecha <= 9 and	maze[f][derecha]==wall:
					a=Arista(f,c,f,derecha,cell,wall)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==wall:
					a=Arista(f,c,abajo,c,cell,wall)
					aristas_G2.append(a)

				if derecha <= 9 and	maze[f][derecha]==entrada:
					a=Arista(f,c,f,derecha,cell,entrada)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==entrada:
					a=Arista(f,c,abajo,c,cell,entrada)
					aristas_G2.append(a)
			
			if maze[f][c]==wall:
				abajo=f+1
				derecha=c+1
				if derecha <= 9 and	maze[f][derecha]==cell:
					a=Arista(f,c,f,derecha,wall,cell)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==cell:
					a=Arista(f,c,abajo,c,wall,cell)
					aristas_G2.append(a)

				if derecha <= 9 and	maze[f][derecha]==entrada:
					a=Arista(f,c,f,derecha,wall,entrada)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==entrada:
					a=Arista(f,c,abajo,c,wall,entrada)
					aristas_G2.append(a)

			if maze[f][c]==salida:
				abajo=f+1
				derecha=c+1
				if derecha <= 9 and	maze[f][derecha]==cell:
					a=Arista(f,c,f,derecha,salida,cell)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==cell:
					a=Arista(f,c,abajo,c,salida,cell)
					aristas_G2.append(a)

				if derecha <= 9 and	maze[f][derecha]==wall:
					a=Arista(f,c,f,derecha,salida,wall)
					aristas_G2.append(a)

				if abajo <= 9 and maze[abajo][c]==wall:
					a=Arista(f,c,abajo,c,salida,wall)
					aristas_G2.append(a)
	
	return aristas_G2

def asignarNivel(listaVerificados):
	nivel=0
	listaAux=[]
	listaNivel=[]
	listaActulizada=[]
	nodoAgregar = listaVerificados.__getitem__(0)
	nodoAgregar.nivel=nivel
	listaNivel.append(nodoAgregar)
	listaVerificados.pop(0)
	listaVerificadosSacar=[]
	listaActulizada.append(nodoAgregar)
	nivel=nivel+1
	#Asignación del nivel a todos los nodos de LV
	while len(listaVerificados)>0:
		for j in listaNivel:
			for k in listaVerificados:
				if j.nodoF == k.nodoPadreF and j.nodoC == k.nodoPadreC:
					listaVerificadosSacar.append(k)
					nodoAgregar=k
					nodoAgregar.nivel=nivel
					listaAux.append(nodoAgregar)
					listaActulizada.append(nodoAgregar)
			for l in listaVerificadosSacar:
				for i in listaVerificados:
					if l.nodoF==i.nodoF and l.nodoC==i.nodoC:
						listaVerificados.remove(i)

		listaNivel.clear
		listaNivel.extend(listaAux)
		listaAux.clear
		nivel=nivel+1
	
	return listaActulizada

def asignarPosicionEjes(listaActualizada):
	nivel=0
	cant_nodo_x_nivel=0
	listaPos=[]
	listaNodoSacar=[]
	#Asignación de la posición en los ejes X e Y de acuerdo al nivel y la cantidad de nodos por nivel
	while len(listaActualizada)>0:
		for j in listaActualizada:	#Contador de nodos por nivel
			if j.nivel==nivel:
				cant_nodo_x_nivel=cant_nodo_x_nivel+1

		if cant_nodo_x_nivel==1:	#Caso de solo haber 1 nodo en el nivel
			for k in listaActualizada:
				if k.nivel==nivel and k.nodoF==9 and k.nodoC==9:	#Ubicar al nodo inicial en la Pos (0,0)
					listaNodoSacar.append(k)
					k.ubiX=0
					k.ubiY=0
					listaPos.append(k)
				if k.nivel==nivel and nivel>0:	# Caso de 1 solo nodo y no es el nivel 0; Modifico el eje Y
					listaNodoSacar.append(k)
					k.ubiX=0
					k.ubiY=nivel*-5
					listaPos.append(k)
					
			for l in listaNodoSacar:		#Remover los nodos del nivel de la LA
				for i in listaActualizada:
					if l.nodoF==i.nodoF and l.nodoC==i.nodoC:
						listaActualizada.remove(i)
		else:
			if cant_nodo_x_nivel % 2 == 0:		#Caso de que la cantidad de nodos del nivel es Par
				num=cant_nodo_x_nivel/2
				tamaño_ini=num*-5
				tamaño_ini=tamaño_ini+2.5
				for t in listaActualizada:
					if t.nivel==nivel:
						listaNodoSacar.append(t)
						t.ubiX=tamaño_ini
						t.ubiY=nivel*-5
						listaPos.append(t)
						tamaño_ini=tamaño_ini+5

				for l in listaNodoSacar:		#Remover los nodos del nivel de la LA
					for i in listaActualizada:
						if l.nodoF==i.nodoF and l.nodoC==i.nodoC:
							listaActualizada.remove(i)
			else:							#Caso de que la cantidad de nodos del nivel es Impar
				num=cant_nodo_x_nivel/2
				num=num-0.5
				tamaño_ini=num*-5
				for f in listaActualizada:
					if f.nivel==nivel:
						listaNodoSacar.append(f)
						f.ubiX=tamaño_ini
						f.ubiY=nivel*-5
						listaPos.append(f)
						tamaño_ini=tamaño_ini+5

				for l in listaNodoSacar:		#Remover los nodos del nivel de la LA
					for i in listaActualizada:
						if l.nodoF==i.nodoF and l.nodoC==i.nodoC:
							listaActualizada.remove(i)
		
		listaNodoSacar.clear()
		nivel=nivel+1
		cant_nodo_x_nivel=0
	return listaPos

def castingGrafo(listaPos):
	#Casting de valores para y formato de datos para enviar a la Gráfica
	listaNombreNodos=[]
	listaPosActu1=[]
	for j in listaPos:
		nombreF=str(j.nodoF)
		nombreC=str(j.nodoC)
		nombre=nombreF+","+nombreC
		j.nombre=nombre

		if j.nodoPadreF != "null":
			nombrePadreF=str(j.nodoPadreF)
			nombrePadreC=str(j.nodoPadreC)
			nombrePadre=nombrePadreF+","+nombrePadreC
			j.nombrePadre=nombrePadre
		else:
			nombrePadre=j.nodoPadreF+","+j.nodoPadreC
			j.nombrePadre=nombrePadre

		listaPosActu1.append(j)
		listaNombreNodos.append(nombre)

	listaAristas=[]
	for j in listaPosActu1:
		if j.nodoPadreF != "null":
			tupla=(j.nombrePadre,j.nombre)
			listaAristas.append(tupla)

	ubicacion={}
	for j in listaPos:
		tupla=(j.ubiX,j.ubiY)
		ubicacion.update({j.nombre:tupla})

	listaResultado=[]
	listaResultado.append(listaNombreNodos)
	listaResultado.append(listaAristas)
	listaResultado.append(ubicacion)
	return listaResultado

def crearGrafo(listaCasting,listaColores):
	listaNombreNodos = listaCasting[0]
	listaAristas = listaCasting[1]
	ubicacion = listaCasting[2]
	G = nx.Graph() # Se crea un grafo nulo
	vertices_G = listaNombreNodos
	# se crean todos los vertices
	G.add_nodes_from(vertices_G)# se le asignan dichos vertices o nodos al grafo
	aristas_G = listaAristas
	# se crean todas las aristas
	G.add_edges_from(aristas_G)# se le asignan dichas aristas al grafo
	ubica = ubicacion


	nx.draw(G, pos=ubica, node_color=listaColores, with_labels=True, node_size=100)
	# se dibuja el grafo
	plt.show() 
	

def asignarColores(listaCompleta,listaVerificados,listaExplorar):
	i=0
	f=0
	c=0
	entrada = 'I'
	salida = 'F'
	listaCaminoSolucion=[]
	while i==0:
		for l in listaVerificados:
			if (l.nodoF==f and l.nodoC==c):
				listaCaminoSolucion.append(l)
				if (l.nodoPadreF== "null" ):
					i=1
				else:
					f=l.nodoPadreF
					c=l.nodoPadreC
	
	listaColores=[]
	for j in listaCompleta:
		nodoEncontrado="null"
		for k in listaCaminoSolucion:
			if (j.nodoF==k.nodoF and j.nodoC==k.nodoC):
				nodoEncontrado=j
		if(nodoEncontrado != "null"):
			if(nodoEncontrado.val==entrada or nodoEncontrado.val==salida):
				listaColores.append("#00ffff")
			else:
				listaColores.append("#00ff00")
		else:
			nodoEncontrado2="null"
			for t in listaExplorar:
				if (j.nodoF==t.nodoF and j.nodoC==t.nodoC):
					nodoEncontrado2=j
			if(nodoEncontrado2 != "null"):
				listaColores.append("#ffa500")
			elif j.val=='x':
				listaColores.append("#ff0000")
			else:
				listaColores.append("#a0a0a4")
	resultado=[]
	resultado.append(listaColores)
	resultado.append(listaCaminoSolucion)
	return resultado


def algoritmosBusqueda(maze, selector):
	
	aristas_G=[]
	aristas_G.extend(crearAristas(maze)) 
	resultado = []
	listaExplorar5 = []
	listaVerificados5 = []
	listaPos=[]
	listaCasting=[]

	if selector == 0:
		resultado.extend(primeroEnAmplitud(aristas_G))
	elif selector == 1:
		resultado.extend(primeroEnProfundidad(aristas_G))
	
	listaExplorar5 = resultado[0]
	listaVerificados5.extend(resultado[1])
	listaVerificados5.extend(listaExplorar5)
	listaResult=[]
	listaResult.extend(resultado[1])
	listaNivel=[]
	listaNivel.extend(asignarNivel(listaVerificados5))
	listaPos.extend(asignarPosicionEjes(listaNivel))
	listaColores=[]
	listaColores.extend(asignarColores(listaPos,resultado[1],resultado[0]))
	listaCasting.extend(castingGrafo(listaPos))
	crearGrafo(listaCasting,listaColores[0])
	listaSolucion=[]
	listaSolucion.extend(listaColores[1])
	resultado.append(listaSolucion)
	
	return resultado
	

	