import pickle

class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}

    def agregar_libro(self, titulo, autor):
        if titulo in self.libros:
            self.libros[titulo]['cantidad'] += 1
        else:
            self.libros[titulo] = {'autor': autor, 'cantidad': 1, 'disponible': True}

    def mostrar_libros(self):
        for titulo, info in self.libros.items():
            disponibilidad = "Disponible" if info['disponible'] else "No disponible"
            print(f"{titulo} - {info['autor']} - Cantidad: {info['cantidad']} - {disponibilidad}")

    def prestar_libro(self, titulo, usuario):
        if titulo in self.libros and self.libros[titulo]['disponible']:
            if usuario in self.usuarios:
                self.usuarios[usuario].append(titulo)
                self.libros[titulo]['cantidad'] -= 1
                self.libros[titulo]['disponible'] = False
                print(f"El libro '{titulo}' ha sido prestado a {usuario}.")
            else:
                print(f"El usuario '{usuario}' no está registrado.")
        else:
            print(f"El libro '{titulo}' no está disponible.")

    def registrar_usuario(self, usuario):
        if usuario not in self.usuarios:
            self.usuarios[usuario] = []

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

    def listar_usuarios(self):
        print("Usuarios registrados:")
        for usuario in self.usuarios:
            print(usuario)

    def listar_libros_usuario(self, usuario):
        if usuario in self.usuarios:
            print(f"Libros prestados a {usuario}:")
            for libro in self.usuarios[usuario]:
                print(libro)
        else:
            print(f"El usuario '{usuario}' no está registrado o no tiene libros prestados.")

    def devolver_libro(self, titulo, usuario):
        if usuario in self.usuarios and titulo in self.usuarios[usuario]:
            self.usuarios[usuario].remove(titulo)
            self.libros[titulo]['cantidad'] += 1
            self.libros[titulo]['disponible'] = True
            print(f"El libro '{titulo}' ha sido devuelto por {usuario}.")
        else:
            print(f"El usuario '{usuario}' no tiene prestado el libro '{titulo}'.")


biblioteca = Biblioteca()
biblioteca.cargar_datos()

# Agregar libros
while True:
    agregarLibro = input('desea agregar un libro [s]i o [n]o ')
    if agregarLibro == 's':
        biblioteca.agregar_libro(input('agregar autor: '),input('agregar titulo: '))
    else:
        break

# Mostrar libros
biblioteca.mostrar_libros()

# Registrar usuario
biblioteca.registrar_usuario(user = input(''))

# Prestar libro
biblioteca.prestar_libro(prestarLibro = input(' '), aUsuario = input(''))

# Guardar datos
biblioteca.guardar_datos()