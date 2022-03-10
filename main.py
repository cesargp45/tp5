from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/tarea_practica', methods = ['GET'])
def consulta():
        return "Software Avanzado - Tarea Práctica 5 - 201801181 - Cesar Garcia"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)