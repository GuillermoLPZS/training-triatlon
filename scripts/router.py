import json, sys

with open("sesiones/nueva_sesion.json") as f:
    d = json.load(f)

tipo = d.get("tipo", "").lower()

campos = {
    "carrera":  ["fecha","objetivo","fatiga_previa","duracion_min","distancia_km",
                 "ritmo_media","ritmo_optimo","fc_media","fc_max",
                 "potencia_media","potencia_max","cadencia",
                 "oscilacion_cm","contacto_ms","ratio_vertical","stamina_final",
                 "te_aerobico","te_anaerobico","notas"],
    "bici":     ["fecha","objetivo","fatiga_previa","duracion_min","distancia_km",
                 "velocidad_media","velocidad_max","fc_media","fc_max",
                 "potencia_media","potencia_max","cadencia_rpm","desnivel_m","tae",
                 "te_aerobico","te_anaerobico","notas"],
    "natacion": ["fecha","objetivo","fatiga_previa","duracion_min","distancia_m",
                 "ritmo_media","ritmo_optimo","fc_media","fc_max",
                 "brazadas_largo","estil","te_aerobico","te_anaerobico","notas"],
    "otros":    ["fecha","deporte","objetivo","duracion_min","fc_media","fc_max",
                 "calorias","te_aerobico","te_anaerobico",
                 "carga_ajenada","body_battery","notas"],
}

tabla_map = {"carrera": "carrera", "bici": "bici", "natacion": "natacion"}
tabla = tabla_map.get(tipo, "otros")

keys = campos.get(tipo, campos["otros"])
out  = {k: d[k] for k in keys if k in d}

with open("/tmp/payload.json", "w") as f:
    json.dump(out, f)

print(tabla)
