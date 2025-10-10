from flasgger import Swagger

def swagger_instance(app):
    # Configuração do Swagger
    app.config['SWAGGER'] = {
        'title': 'Prioriza API',
        'description': 'Prioriza é uma API simples e poderosa para gerenciamento de tarefas. Com ela, você pode cadastrar usuários, criar e organizar tarefas, definir prioridades e acompanhar o progresso diretamente na sua aplicação. ⚡📂',
        'version': '1.0.0',
        'uiversion': 3,
        'specs_route': '/docs/'
    }

    swagger = Swagger(app)

    return swagger