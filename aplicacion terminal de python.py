import pickle

class Libro:
    def __init__(self, titulo, autor, cantidad=1, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.cantidad = cantidad
        self.disponible = disponible

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = []

    def agregar_libro(self, titulo, autor):
        if titulo in self.libros:
            self.libros[titulo].cantidad += 1
        else:
            self.libros[titulo] = Libro(titulo, autor)

    def mostrar_libros(self):
        print("Lista de libros:")
        for libro in self.libros.values():
            disponibilidad = "Disponible" if libro.disponible else "No disponible"
            print(f"{libro.titulo} - {libro.autor} - Cantidad: {libro.cantidad} - {disponibilidad}")

    def prestar_libro(self, titulo, nombre_usuario):
        for usuario in self.usuarios:
            if usuario.nombre == nombre_usuario:
                if titulo in self.libros and self.libros[titulo].disponible and self.libros[titulo].cantidad > 0:
                    usuario.libros_prestados.append(titulo)
                    self.libros[titulo].cantidad -= 1
                    self.libros[titulo].disponible = False
                    print(f"El libro '{titulo}' ha sido prestado a {nombre_usuario}")
                    return
                else:
                    print("El libro no está disponible para préstamo")
                    return
        print("Usuario no encontrado")

    def registrar_usuario(self, nombre):
        self.usuarios.append(Usuario(nombre))
        print(f"Usuario {nombre} registrado con éxito")

    def listar_usuarios(self):
        print("Lista de usuarios:")
        for usuario in self.usuarios:
            print(usuario.nombre)

    def guardar_datos(self):
        with open('datos_biblioteca.pkl', 'wb') as archivo:
            pickle.dump((self.libros, self.usuarios), archivo)

    def cargar_datos(self):
        try:
            with open('datos_biblioteca.pkl', 'rb') as archivo:
                self.libros, self.usuarios = pickle.load(archivo)
        except FileNotFoundError:
            self.libros = {}
            self.usuarios = {}

# Ejemplos de uso
biblioteca = Biblioteca()

biblioteca.agregar_libro("Cien años de soledad", "Gabriel García Márquez")
biblioteca.agregar_libro("Don Quijote de la Mancha", "Miguel de Cervantes")
biblioteca.agregar_libro("El Principito", "Antoine de Saint-Exupéry")
print('\n')

while True:
    agregarLibro = input('Desea agregar un libro? (s)i o (n)o?: ')
    if agregarLibro == 's':
        biblioteca.agregar_libro(input("Titulo: "), input("Autor: "))
    else:
        break
print('\n')

biblioteca.mostrar_libros()
print('\n')


biblioteca.registrar_usuario(input('Nuevo Usuario: '))
print('\n')


#biblioteca.prestar_libro("El Principito", "Juan")
while True:
    prestarLibro = input('Desea prestar un libro [s]i o [n]o: ')
    if prestarLibro == 's':
        biblioteca.prestar_libro(input("titulo a prestar: "),input("a que usuario: "))
    else:
        break
print('\n')

biblioteca.listar_usuarios()
biblioteca.mostrar_libros()
biblioteca.guardar_datos()
