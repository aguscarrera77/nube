
# 1 crear la imagen o plano que va activar el archivo cuando lo guarde en el docker.
FROM python:3.10-slim

#2 Definir la carpeta o espacio de trabajo desde donde voy a traer mis archivos.

WORKDIR /app

#3.Copiar el nombre del codigo en donde host o servidor arranca a funcionar y va estar guardado en el contenedor.

COPY servidor.py .

#4.instalar flask dentro del enterno de mi contenedor.

RUN pip install flask 

#5 indico el puerto donde se conecta el contenedor.

EXPOSE 5000 

#6 Comnando completo para iniciar el contenedor.

CMD [ "python","servidor.py"]








