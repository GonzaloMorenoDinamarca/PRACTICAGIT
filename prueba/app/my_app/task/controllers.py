from flask import Blueprint

taskRoute = Blueprint('task',__name__, url_prefix = '/task')

@taskRoute.route('/')
def index():
    return 'Prueba'

@taskRoute.route('/<int:id>')
def show(id:int):
    return 'Show ' + str(id)

@taskRoute.route('/delete/<int:id>')
def delete(id:int):
    return 'delete ' + str(id)

@taskRoute.route('/create', methods = ('GET', 'POST')) # Según la documentación de flask es mejor pasar los methods como listas []
def create():
    return 'Create '

@taskRoute.route('/update/<int:id>', methods = ['GET', 'POST']) # Recomendada por ser listas
def update(id:int):
    return 'update ' + str(id)





# OJO: En HTML solo podemos hacer peticiones GET y POst, en HTPP podemos hacer los 5 metodos de solicitude.