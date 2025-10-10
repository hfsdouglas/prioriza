class AuthSpecs():
    def login_specs():
        return {
            'parameters': [
                {
                    'name': 'Login',
                    'in': 'body',
                    'required': True,
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'email': {
                                'type': 'string',
                                'example': 'email@email.com.br'
                            },
                            'password': {
                                'type': 'string',
                                'example': 'Anything@123'
                            }
                        }
                    }
                }
            ],
            'responses': {
                200: {
                    'description': 'Login realizado com sucesso',
                    'examples': {
                        'application/json': {
                            'message': 'Olá, John Doe! Seja bem-vindo ao Prioriza!',
                            'token': 'jwt_token'
                        }
                    }
                },
                400: {
                    'description': 'Dados inválidos',
                    'examples': {
                        'application/json': {
                            'errors': {
                                'email': ['Not a valid email address.'],
                                'password': ['Shorter than minimum length 6.']
                            }
                        }
                    }
                },
                401: {
                    'description': 'Credenciais inválidas',
                    'examples': {
                        'application/json': {
                            'message': 'Credenciais inválidas'
                        }
                    }
                }
            }
        }
        
    def signin_specs():
        return {
            'parameters': [
                {
                    'name': 'Sign In',
                    'in': 'body',
                    'required': True,
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'name': {
                                'type': 'string',
                                'example': 'John Doe'
                            },
                            'email': {
                                'type': 'string',
                                'example': 'email@email.com.br'
                            },
                            'password': {
                                'type': 'string',
                                'example': 'Anything@123'
                            }
                        }
                    }
                }
            ],
            'responses': {
                301: {
                    'description': 'Caso o usuário seja cadastrado com sucesso, retorna status_code 301 e redireciona para /login',
                    'headers': {
                        'Location': {
                            'description': 'URL para onde o cliente será redirecionado',
                            'schema': { 
                                'type': 'string', 
                                'example': '/login' 
                            }
                        }
                    }
                },
                400: {
                    'description': 'Caso os dados do usuário estejam inválidos, retorna mensagens de erro.',
                    'examples': {
                        'application/json': {
                            'errors': {
                                'name': [
                                    'Missing data for required field.',
                                    'Shorter than minimum length 8.'
                                ],
                                'email': [
                                    'Not a valid email address.'
                                ],
                                'password': [
                                    'Missing data for required field.',
                                    'Shorter than minimum length 6.'
                                ]
                            }
                        }
                    }
                }
            }
        }