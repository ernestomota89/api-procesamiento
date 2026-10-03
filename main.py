import os
import random
from flask import Flask, jsonify

app = Flask(__name__)

def clasificar_temperatura(temperatura: float):
    """
    Clasifica el estado y la acción según el valor de temperatura:
    - Menor a 60 °C: Normal ("Operacion normal")
    - De 60 a menos de 70 °C: Advertencia ("Revisar sistema de enfriamiento")
    - 70 °C o más: Alarma ("Detener maquina y revisar")
    """
    if temperatura < 60.0:
        estado = "Normal"
        accion = "Operacion normal"
    elif temperatura < 70.0:
        estado = "Advertencia"
        accion = "Revisar sistema de enfriamiento"
    else:
        estado = "Alarma"
        accion = "Detener maquina y revisar"
    return estado, accion

@app.route("/", methods=["GET"])
@app.route("/procesar", methods=["GET"])
def procesar_temperatura():
    # Simulación de lectura de sensor de temperatura entre 40 y 80 °C
    temperatura = round(random.uniform(40.0, 80.0), 2)
    estado, accion = clasificar_temperatura(temperatura)

    payload = {
        "repositorio": 1,
        "proceso": "procesamiento_temperatura_cnc",
        "maquina": "CNC-01",
        "temperatura_c": temperatura,
        "estado": estado,
        "accion": accion
    }
    return jsonify(payload), 200

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=False)
