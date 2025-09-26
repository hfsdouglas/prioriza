import pytest

class TestTask:
    def test_create_task(self, client, sample_user, sample_auth_headers):
        """
        Cenário: Cadastro de tarefa
        Ação: Envia informações para /tasks
        Resultado: Recebe json com informações de sucesso 
        """

        response = client.post('/tasks', 
            json={
                "task": "Criar teste de tarefa no prioriza",
                "user_id": sample_user.id
            }, 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert 'message' in data and data['message'] == 'Usuário cadastrado com sucesso!'