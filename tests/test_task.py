import pytest

class TestTask:
    def test_create_task(self, client, sample_auth_headers):
        """
        Cenário: Cadastro de tarefa
        Ação: Envia informações para /tasks
        Resultado: Recebe json com informações de sucesso 
        """

        response = client.post('/tasks', 
            json={
                "task": "Criar teste de tarefa no prioriza",
            }, 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert 'message' in data and data['message'] == 'Tarefa cadastrada com sucesso!'

    def test_create_task_with_invalid_data(self, client, sample_auth_headers):
        """
        Cenário: Cadastro de tarefa com dados inválidos
        Ação: Envia informações para /tasks
        Resultado: Recebe json de mensagens com detalhes dos dados incorretos 
        """

        response = client.post('/tasks', 
            json={
                "task": "",
            }, 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 400
        assert "task" in data

    def test_update_task(self, client, sample_user, sample_task, sample_auth_headers):
        """
        Cenário: Atualiza de tarefa
        Ação: Envia informações para /tasks com método HTTP Patch
        Resultado: Recebe json com informações de sucesso 
        """

        response = client.patch(f'/tasks/{sample_task.id}', 
            json={
                "task": "Texto para teste de atualização de task",
                "user_id": sample_user.id,
                "completed": 1
            },
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert 'message' in data and data['message'] == 'Tarefa atualizada com sucesso!'

    def test_update_task_with_invalid_data(self, client, sample_task, sample_auth_headers):
        """
        Cenário: Atualização de tarefa com dados inválidos
        Ação: Envia informações para /tasks com HTTP Method Patch
        Resultado: Recebe json de mensagens com detalhes dos dados incorretos 
        """

        response = client.patch(f'/tasks/{sample_task.id}', 
            json={
                "user_id": 1,
                "task": "",
                "completed": "falso" 
            },
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 400
        assert 'user_id' in data or 'task' in data or 'completed' in data