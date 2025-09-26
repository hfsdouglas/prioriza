import pytest
class TestAuth:
    def test_signin(self, client):
        """
        Cenário: Cadastro de usuário
        Ação: Enviar dados válidos para /auth/signin
        Resultado esperado: Deve redirecionar para /login
        """
        response = client.post('/auth/signin', follow_redirects=True, json={
            'name': "John Doe",
            'email': "johndoe@email.com",
            'password': "123456",
        })

        assert len(response.history) == 1
        assert response.request.path == '/login'
    
    def test_login(self, client, sample_user):
        """
        Cenário: Realizar login
        Ação: Enviar dados válidos para /auth/login
        Resultado esperado: Recebe json com message e token
        """
        response = client.post('/auth/login', json={
            'email': sample_user.email,
            'password': sample_user.password
        })

        data = response.get_json()

        assert response.status_code == 200
        assert "message" in data and data["message"] == "Olá, John! Seja bem-vindo ao Prioriza!"
    
    def test_login_with_invalid_credentials(self, client):
        """
        Cenário: Realizar login com credenciais inválidas
        Ação: Enviar credenciais inválidas para /auth/login
        Resultado esperado: Recebe json com message status_code 401
        """

        response = client.post('/auth/login', json={
            'email': 'johndoe@email.com',
            'password': 'john1234'
        })

        data = response.get_json()

        assert response.status_code == 401
        assert "message" in data and data["message"] == "Credenciais inválidas"
            
    def test_login_with_invalid_data(self, client):
        """
        Cenário: Realizar login
        Ação: Enviar dados válidos para /auth/login
        Resultado esperado: Recebe json com message e token
        """
        response = client.post('/auth/login', json={
            'email': 'john',
            'password': '123'
        })

        data = response.get_json()

        assert response.status_code == 400
        assert "email" in data or "password" in data