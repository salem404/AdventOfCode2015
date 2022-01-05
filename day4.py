
import hashlib

keyy="iwrupvqb"

""" Ejemplo de uso haslib

md5=hashlib.md5(keyy.encode())

print(md5.hexdigest())

"""


for numero in range(0,1000000000000000000000000000000000000):
    prueba=keyy+str(numero)
    md5T=hashlib.md5(prueba.encode())
    md5=(md5T.hexdigest())
    if md5.startswith("000000"):
        break

print(numero)