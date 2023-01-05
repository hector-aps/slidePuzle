# slidePuzle

Recreación simple del clásico puzle en donde tienes que deslizar varias piezas para resolver el patrón numérico, escrito en Python con la librería Tkinter para la UI.

![](https://github.com/hector-aps/slidePuzle/blob/master/README%20Images/Captura%20de%20pantalla%20(452).png?raw=true)

## Funcionamiento de clase:

### Funcion constructora:

```python
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
```

### Funcion mover pieza:

```python
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
```

### Funcion para revolver las piezas:

```python
	def revolver(self):
		'''
		Funcion encargada de revolver el tablero realizando 100 movimientos aleatorios y reestableciendo
		el contador de intentos a 0
		'''
		for i in range(100):
			var = choice(self.movPos[self.tablero.index(" ")])
			self.mover(var)
		self.intentos = 0
```

### Funcion para verificar si el jugador ha ganado:

```python
	def verificar(self):
		'''
		Esta funcion se encarga de verificar si el tablero ha sido completado, en cuyo caso retorna True
		'''
		return True if self.tablero == [1, 2, 3, 4, 5, 6, 7, 8, " "] else False
```

Esto es todo el codigo de la clase que maneja el juego, ya que para este proyecto se utilizo la programacion orientada a objetos, el archivo principal (Que aqui no se muestra) se encarga de dibujar la interfaz grafica y la interaccion del usuario con la parte interna del programa.

## Imagen de mensaje al ganar:

![](https://github.com/hector-aps/slidePuzle/blob/master/README%20Images/Captura%20de%20pantalla%20(453).png?raw=true)
