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
                        'type': 'int',
                        'example': '1'
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
    
    def get_tasks_specs():
        return {
            'responses': {
                200: {
                    'description': 'Retorna todas as tarefas de cada usuário.',
                    'examples': {
                        'application/json': [
                            {
                                'user_id': '1',
                                'user_name': 'João da Silva',
                                'user_email': 'joao@exemplo.com',
                                'user_tasks': [
                                    {
                                        'task_id': '101',
                                        'description': 'Finalizar relatório financeiro do mês',
                                        'completed': False
                                    },
                                    {
                                        'task_id': '102',
                                        'description': 'Agendar reunião com a diretoria',
                                        'completed': True
                                    }
                                ]
                            },
                            {
                                'user_id': '2',
                                'user_name': 'Maria Souza',
                                'user_email': 'maria@exemplo.com',
                                'user_tasks': [
                                    {
                                        'task_id': '103',
                                        'description': 'Revisar plano de marketing',
                                        'completed': False
                                    }
                                ]
                            }
                        ]

                    }
                }
            }
        }
    
    def get_task_specs():
        return {
            'parameters': [
                {
                    'name': 'task_id',
                    'in': 'path',
                    'required': True,
                    'schema': {
                        'type': 'int',
                        'example': '1'
                    }
                }
            ],
            'responses': {
                200: {
                    'description': 'Retorna uma tarefa, de acordo com o id enviado.',
                    'examples': {
                        'application/json': {
                            'id': '101',
                            'description': 'Finalizar relatório financeiro do mês',
                            'completed': False,
                            'user': {
                                'id': '1',
                                'name': 'João da Silva'
                            }
                        }
                    }
                },
                404: {
                    'description': 'Caso a tarefa não seja encontrada, retorna mensagem.',
                    'examples': {
                        'application/json': {
                            'message': 'Tarefa não encontrada!'
                        }
                    }
                }
            }
        }
    
    def get_task_by_user_specs(): 
        return {
            'parameters': [
                {
                    'name': 'user_id',
                    'in': 'path',
                    'required': True,
                    'schema': {
                        'type': 'uuid',
                        'example': '7b0d9f92-d0bf-4b1e-abe0-eb6829167757'
                    }
                },
            ],
            'responses': {
                200: {
                    'description': 'Retorna todas as tarefas de um usuário específico.',
                    'examples': {
                        'application/json': [
                            {
                                'id': '101',
                                'description': 'Finalizar relatório financeiro do mês',
                                'completed': False
                            },
                            {
                                'id': '102',
                                'description': 'Agendar reunião com a diretoria',
                                'completed': True
                            },
                            {
                                'id': '103',
                                'description': 'Revisar plano de marketing',
                                'completed': False
                            }
                        ]
                    }
                },
                404: {
                    'description': 'Caso o usuário não seja encontrado, retorna mensagem.',
                    'examples': {
                        'application/json': {
                            'message': 'Usuário não encontrado!'
                        }
                    }
                }
            }
        }