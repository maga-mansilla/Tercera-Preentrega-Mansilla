#las clases en py se nombran en pascal case (primera letra de c palabra en mayus)
#inicializo mis clases con los atributos y un proceso)
class Celular:
    def __init__(self, modelo, marca, memoria, precio):
        self.modelo = modelo
        self.marca = marca
        self.memoria = memoria
        self.precio = precio
        self.en_produccion = False
#hago 3 metodos (accion del objeto)
def iniciar_produccion(self):
    self.en_produccion = True
    print(f"Print produccion del celular {self.modelo} ha finalizado")
def finalizar_produccion(self):
    self.en_produccion = False
    print(f"produccion del celular {self.modelo} ha finalizado")
def obtener_info(self):
    return (f"{self-marca} - {self.modelo} - {self-memoria}GB - ${self.precio}")