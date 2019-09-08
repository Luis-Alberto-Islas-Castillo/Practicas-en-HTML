import json
datos = [{
	"nombre":"Luis",
	"id":413,
	"profesor":True,
	"idCursos":(59,875,215),
	"cursos":
		{
			"marketing":"Mi primer lenguaje de Programacion",
			"programacion":
				(
				"C",
				"C++",
				"Java")
		}
}]

print (json.dumps(datos))
