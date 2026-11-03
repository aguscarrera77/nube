from flask import Flask, jsonify

# Inicializamos la aplicación web
app = Flask(__name__)

# Definimos una ruta (endpoint) y el método HTTP permitido (por defecto GET)
@app.route('/')
def home():
    return jsonify({"mensaje":"Nuevo mensaje","programdor":"Agustin Carrera","mensaje":"Nueva Aplicacion funcionando"
    })

# Bloque de ejecución principal
if __name__ == '__main__':
    # host='0.0.0.0' hace que escuche en todas las interfaces de red
    # port=5000 es el puerto lógico donde atenderá el servicio
    app.run(host='0.0.0.0', port=5000, debug=True)



