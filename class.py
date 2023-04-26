#class
class clase:
    pass
objeto1=clase()
objeto2=clase()
objeto3=clase()

#class persona
class Persona:
        def _init_(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad

        def presentarse(self):
            print(f"¡Hola, mi nombre es {self.nombre} y tengo {self.edad} años!") 
    
persona1=Persona("Juan", 16)
persona2=Persona("Ana", 36)
persona1.presentarse()
persona2.presentarse()

#defcumple
def cumplir_anios(self):
 self.edad += 1
 print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años.")

def cambiar_nombre(self, nuevo_nombre):
    self.nombre = nuevo_nombre
    print(f"Mi nombre ha sido cambiado a {self.nombre}.")
    
def es_mayor_de_edad(self):
    if self.edad >= 18:
        return True
    else:
        return False  
    