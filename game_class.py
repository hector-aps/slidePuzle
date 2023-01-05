from random import choice

class Puzzle:
	def __init__(self):
		'''
		Funcion constructora de clase, establece los intentos(movimientos), las posiciones iniciales
		de las fichas en el tablero, y los posibles movimientos de las piezas dependiendo de
		la posicion de la pieza vacia.
		'''
		self.intentos = 0
		
		self.tablero = [1, 2, 3, 4, 5, 6, 7, 8, " "]

		self.movPos = {
			0 : [3, 1],
			1 : [0, 2, 4],
			2 : [1, 5],
			3 : [0, 4, 6],
			4 : [5, 3, 1, 7],
			5 : [2, 4, 8],
			6 : [3, 7],
			7 : [6, 8, 4],
			8 : [5, 7]
		}
		
	def mover(self, pieza):
		'''
		Recibe la pieza que se intenta mover y verifica si esta esta entre los posibles movimientos
		de la pieza vacia, si es asi procede a cambiar las piezas de posicion y agregar un movimiento
		al contador
		'''
		if pieza in self.movPos[self.tablero.index(" ")]:
			self.tablero[self.tablero.index(" ")] = self.tablero[pieza]
			self.tablero[pieza] = " "
			self.intentos +=1
		
	def revolver(self):
		'''
		Funcion encargada de revolver el tablero realizando 100 movimientos aleatorios y reestableciendo
		el contador de intentos a 0
		'''
		for i in range(100):
			var = choice(self.movPos[self.tablero.index(" ")])
			self.mover(var)
		self.intentos = 0

	def verificar(self):
		'''
		Esta funcion se encarga de verificar si el tablero ha sido completado, en cuyo caso retorna True
		'''
		return True if self.tablero == [1, 2, 3, 4, 5, 6, 7, 8, " "] else False