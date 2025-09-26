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

    def test_create_task_with_invalid_user(self, client, sample_auth_headers):
        """
        Cenário: Cadastro de tarefa com usuário inválido
        Ação: Envia informações para /tasks
        Resultado: Recebe json com informações de usuário inválido 
        """

        response = client.post('/tasks', 
            json={
                "task": "Criar teste de tarefa no prioriza",
                "user_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6"
            }, 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 400
        assert 'message' in data and data['message'] == 'Usuário não encontrado!'

    def test_create_task_with_invalid_data(self, client, sample_auth_headers):
        """
        Cenário: Cadastro de tarefa com dados inválidos
        Ação: Envia informações para /tasks
        Resultado: Recebe json de mensagens com detalhes dos dados incorretos 
        """

        response = client.post('/tasks', 
            json={
                "task": "",
                "user_id": "1"
            }, 
            headers=sample_auth_headers
        )

        data = response.get_json()

        print(data)

        assert response.status_code == 400
        assert "task" in data or "user_id" in data
