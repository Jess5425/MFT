import json

try:
    with open('usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)
    print(json.dumps(usuarios, indent=4))
except FileNotFoundError:
    print("El archivo 'usuarios.json' no se encuentra.")
