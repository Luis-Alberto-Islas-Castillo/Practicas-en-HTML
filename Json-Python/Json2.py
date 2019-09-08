import json

datos = '''[{"nombre": "Antonio", "profesor": true, "idClases": [53,765,675], "id": 343, "Clases": {"marketing": "Mi primera tienda en linea", "Drupal": ["WordPresss", "Prestashop", "Json"]}}]'''

print (json.loads(datos))
