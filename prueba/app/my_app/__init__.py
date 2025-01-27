from flask import Flask # Clases de tercero primero

from my_app.task.config import DevConfig # Clases internas después

from my_app.task.controllers import taskRoute # llamé al blueprint con la importación desde los controladores

app = Flask (__name__)
app.register_blueprint(taskRoute) # Registre el blueprint dentro del contexto de la aplicación.
app.config.from_object(DevConfig) # La más recomendada, ya que permite separaciónes de las distintas configuraciones del proyecto y de la codificación misma del proyecto.
# app.debug = True #----> Sería lo mismo que la línea anterior, distintas formas con el mismo resultado

@app.route('/')
def hola_mundo() -> str:
    return 'Hola brothers!'

