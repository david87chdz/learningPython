import json

persona = {
    "nombre": "Javier",
    "apellido": "Quinonez",
    "edad": 24
}

# Serializar
# json.dumps(lo que queremos serializar, identación (opcional))
# objeto_json = json.dumps(persona, indent=2)

with open("persona.json", "w") as archivo_json:
    # Serializado
    # archivo_json.write(objeto_json)
    #Sin Serializar
    json.dump(persona, archivo_json)