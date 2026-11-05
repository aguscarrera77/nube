from flask import Flask
import mysql.connector 

app= Flask(__name__)

@app.route("/")
def home():
    #abrir la puerta de conexion entre mi archivo y app que guarda la base de datos.
    db=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="mi_base"
    )

    cursor=db.cursor()#cursor es el encargado de llevar los datos guardados en db hasta phpmyadmin y generar la conexion.
    #CREAR LA TABLA DONDE VOY A GUARDAR LOS VALORES.
    cursor.execute("CREATE TABLE IF NOT EXISTS personas (nombre VARCHAR(20))")
    #INSERTAR VALORES A LA TABLA.
    cursor.execute("INSERT INTO personas (nombre) VALUES ('Agustin'),('Carlos Gardel')")
    #ahora voy a guardar los cambios.
    db.commit()
    #CONSULTAR A LA TABLA PERSONAS QUE VALORES TIENE DENTRO DE LA TABLA.
    cursor.execute('SELECT nombre FROM personas')
    #guardar en una variable todos los resultados.
    resultados=cursor.fetchall()
    #CERRAR LA CONEXION QUE HICE AL PRINCIPIO.
    db.close()
    #armar un lista con los resultados para que se vea en un navegador. Con un archivo de html.
    html="<h1>Personas de mi base de datos</h1><ul>"
    for fila in resultados:
        html += f"<li>{fila[0]}</li>"#Agrado de cada fila de html que trae los valores guardaods en resultados.
    html +="</ul>"
    return html
if __name__=="__main__":
    app.run(debug=True)


