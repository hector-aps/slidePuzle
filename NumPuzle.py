from game_class import *
from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(1,1)
root.geometry("400x300")
root.title("NumPuzzle")
window = Frame(root)
window.config(bg="#F6DDCC")
root.config(bg="#F6DDCC")
color = "#F6DDCC"

game = Puzzle()

#----Funcionalidad Interfaz---------------

def actualizar():
	'''
	Funcion que actualiza los valores de los elementos de la interfaz grafica a los valores
	internos del objeto game
	'''
	global intentos
	intentos.config(text = f"Movimientos: {game.intentos}")
	bot1.set(str(game.tablero[0]))
	bot2.set(str(game.tablero[1]))
	bot3.set(str(game.tablero[2]))
	bot4.set(str(game.tablero[3]))
	bot5.set(str(game.tablero[4]))
	bot6.set(str(game.tablero[5]))
	bot7.set(str(game.tablero[6]))
	bot8.set(str(game.tablero[7]))
	bot9.set(str(game.tablero[8]))
	comprobar()
	
def piezaAct(pieza):
	'''
	Funcion que utilizan los botones del juego, reciben la pieza que se intenta mover y
	llama la funcion interna de game para mover la pieza, luego llama a la funcion actualizar()
	'''
	if not game.verificar():
		game.mover(pieza)
		actualizar()

def mezclar():
	'''
	Funcion que llama al metodo revolver() de game y llama a la funcion actualizar(), es utilizada
	por el boton Mezclar
	'''
	game.revolver()
	actualizar()

def comprobar():
	'''
	Verifica mediante el metodo verificar() de game para saber si se ha completado el reto, si es
	asi nos mostrara un mensaje te completado y se mostrara con cuantos intentos se termino
	'''
	if game.verificar():
		messagebox.showinfo("Completado!", f"Completado en {game.intentos} movimientos")


#----Interfaz---------------
#En esta parte se desarrolla la interfaz grafica del juego


Label(window, text = "Numeros", fg = "#6E2C00", bg = color, font = ("Comic Sans MS", 12, "bold")).grid(row=0, column=0, columnspan=3, pady=10, padx=10)

intentos = Label(window, text = "Intentos: 0", fg = "#6E2C00", font = ("Comic Sans MS", 10, "bold"), bg = color)
intentos.grid(row=1, column=0, columnspan=3, pady=10)

bot1 = StringVar()
Button(window, textvariable=bot1, width = 4, height = 2, command = lambda: piezaAct(0)).grid(row=2, column=0)

bot2 = StringVar()
Button(window, textvariable=bot2, width = 4, height = 2, command = lambda: piezaAct(1)).grid(row=2, column=1)

bot3 = StringVar()
Button(window, textvariable=bot3, width = 4, height = 2, command = lambda: piezaAct(2)).grid(row=2, column=2)

bot4 = StringVar()
Button(window, textvariable=bot4, width = 4, height = 2, command = lambda: piezaAct(3)).grid(row=3, column=0)

bot5 = StringVar()
Button(window, textvariable=bot5, width = 4, height = 2, command = lambda: piezaAct(4)).grid(row=3, column=1)

bot6 = StringVar()
Button(window, textvariable=bot6, width = 4, height = 2, command = lambda: piezaAct(5)).grid(row=3, column=2)

bot7 = StringVar()
Button(window, textvariable=bot7, width = 4, height = 2, command = lambda: piezaAct(6)).grid(row=4, column=0)

bot8 = StringVar()
Button(window, textvariable=bot8, width = 4, height = 2, command = lambda: piezaAct(7)).grid(row=4, column=1)

bot9 = StringVar()
Button(window, textvariable=bot9, width = 4, height = 2, command = lambda: piezaAct(8)).grid(row=4, column=2)

Button(window, text = "Mezclar", fg = "#6E2C00", command = mezclar).grid(row=5, column=0, columnspan=3, pady = 10)

mezclar()
actualizar()


window.pack()
root.mainloop()