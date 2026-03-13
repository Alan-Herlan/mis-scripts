import os

# Esto guarda tu nombre en una variable
usuario = os.getlogin()

print(f"Hola, {usuario}. Estoy listo para ayudarte.")
print(f"Tu carpeta de trabajo actual es: {os.getcwd()}")