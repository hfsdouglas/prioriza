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
    
    def update_task_specs():
        return {
            'parameters': [
                {
                    'name': 'task_id',
                    'in': 'path',
                    'required': True,
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'task': {
                                'type': 'int',
                                'example': '1'
                            }
                        }
                    }
                },
                {
                    'name': 'body',
                    'in': 'body',
                    'required': True,
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'task': {
                                'type': 'string',
                                'example': 'Eu tenho que fazer alguma coisa, qualquer coisa.'
                            },
                            'user_id': {
                                'type': 'string',
                                'example': '7b0d9f92-d0bf-4b1e-abe0-eb6829167757'
                            },
                            'completed': {
                                'type': 'boolean',
                                'example': True
                            }
                        },
                        'required': ['task', 'user_id', 'completed']
                    }  
                }
            ],
            'responses': {
                200: {
                    'description': 'Caso a tarefa seja atualizada, retorna mensagem de sucesso.',
                    'examples': {
                        'application/json': {
                            'message': 'Tarefa atualizada com sucesso!'
                        }
                    }
                },
                400: {
                    'description': 'Caso os dados da tarefa estejam inválidos, retorna lista de erros.',
                    'examples': {
                        'application/json': {
                            'errors': {
                                'task': [
                                    'Missing data for required field.',
                                    'Shorter than minimum length 10.'
                                ],
                                'user_id': [
                                    'Missing data for required field.',
                                    'Not a valid UUID.'
                                ],
                                'completed': [
                                    'Missing data for required field.',
                                    'Not a valid boolean.'
                                ]
                            }
                        }
                    }
                },
                404: {
                    'description': 'Caso a tarefa não seja encontrada, mediante o id enviado, retorna mensagem de erro.',
                    'examples': {
                        'application/json': {
                            'message': 'Tarefa não encontrada!'
                        }
                    }
                }
            }
        }