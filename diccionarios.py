persona =  {
    "nombre": "carlos",
    "edad": 25,
    "ciudad": "San Miguel   "
}

print(persona)
print(persona["nombre"])



estudiante = {
    "nombre": "Ana",
    "edad": 21,
    "cursos": ["Python", "Estructura de datos"]
}

print(estudiante["edad"])


estudiante['edad'] = 22
estudiante['carrera'] = 'Ing. Software'


del estudiante['edad']

persona.pop("ciudad")