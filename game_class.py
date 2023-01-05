from random import choice

class Puzzle:
	def __init__(self):
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
		if pieza in self.movPos[self.tablero.index(" ")]:
			self.tablero[self.tablero.index(" ")] = self.tablero[pieza]
			self.tablero[pieza] = " "
			self.intentos +=1
		
	def revolver(self):
		for i in range(100):
			var = choice(self.movPos[self.tablero.index(" ")])
			self.mover(var)
		self.intentos = 0

	def verificar(self):
		return True if self.tablero == [1, 2, 3, 4, 5, 6, 7, 8, " "] else False