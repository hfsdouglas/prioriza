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
    
    @pytest.mark.parametrize("email,password,status,message,token", [
        ("johndoe@email.com", "123456", 200, "Olá, John! Seja bem-vindo ao Prioriza!", True),
        ("johndoe@email.com", "john1234", 401, "Credenciais inválidas", False),
        ("john", "123", 400, "", False)
    ])
    def test_login(self, client, sample_user, email, password, status, message, token):
        """
        Cenário: Realizar login
        Ação: Enviar dados válidos para /auth/login
        Resultado esperado: Recebe json com message e token
        """
        response = client.post('/auth/login', json={
            'email': email,
            'password': password
        })

        data = response.get_json()

        if status == 400:
            assert "email" in data or "password" in data
        else:
            assert "message" in data and data["message"] == message
            assert ("token" in data) == token