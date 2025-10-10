class Task_Specs():
    def create_task_specs():
        return {
            'parameters': [
                {
                    'name': 'Nova tarefa',
                    'in': 'body',
                    'required': True,
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'task': {
                                'type': 'string',
                                'example': 'Eu tenho que fazer alguma coisa, qualquer coisa.'
                            }
                        }
                    }
                }
            ], 
            'responses': {
                201: {
                    'description': 'Caso a tarefa seja criada, retorna mensagem de sucesso.',
                    'examples': {
                        'application/json': {
                            'message': 'Tarefa cadastrada com sucesso!'
                        }
                    }
                },
                400: {
                    'description': 'Caso os dados estejam inválidos, retorna lista de erros.',
                    'examples': {
                        'application/json': {
                            'errors': {
                                'task': [
                                    'Missing data for required field.',
                                    'Shorter than minimum length 10.'
                                ]
                            }
                        }
                    }
                },
            }
        }
    
    
    
