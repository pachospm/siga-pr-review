# Importamos Flask para crear la API y jsonify para responder con JSON
from flask import Flask, jsonify

# Creamos la app Flask usando el nombre de esta modulo
app = Flask(__name__)

# Vinculamos la dirección /salud con esta función para  solicitudes GET

@app.route("/salud", methods=["Get"])
def salud():
  # Devuelve una respuesta mínima y el código HTTP 200: correcto
  return jsonify({"estado":"ok"}), 200
