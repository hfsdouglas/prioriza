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

    def test_delete_task(self, client, sample_task, sample_auth_headers):
        """
        Cenário: Deleta uma tarefa
        Ação: Envia informações para /tasks com método HTTP Patch
        Resultado: Recebe json com informações de sucesso 
        """

        response = client.delete(f'/tasks/{sample_task.id}', 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert "message" in data and data['message'] == 'Tarefa deletada com sucesso!'

    def test_delete_task_with_invalid_id(self, client, sample_auth_headers):
        """
        Cenário: Tenta deletar uma tarefa com id inválido
        Ação: Envia informações para /tasks com método HTTP Delete
        Resultado: Recebe json com informações de tarefa não encontrada 
        """

        response = client.delete('/tasks/01226', 
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 400
        assert "message" in data and data['message'] == 'Tarefa não encontrada!'


    def test_get_tasks(self, client, sample_task, sample_auth_headers):
        """
        Cenário: Busca por todas as tarefas
        Ação: Envia informações para /tasks
        Resultado: Recebe json com informações de tarefa não encontrada 
        """ 

        response = client.get('/tasks',
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert isinstance(data, list)

        if data:
            user = data[0]

            assert 'user_id' in user
            assert 'user_name' in user
            assert 'user_email' in user
            assert 'user_tasks' in user

            assert isinstance(user['user_tasks'], list)

            if user['user_tasks']:
                task = user['user_tasks'][0]

                assert 'task_id' in task
                assert 'description' in task
                assert 'completed' in task
    
    def test_get_tasks_by_user(self, client, sample_task, sample_user, sample_auth_headers):
        """
        Cenário: Busca por todas as tarefas
        Ação: Envia informações para /tasks
        Resultado: Recebe json com informações de tarefa não encontrada 
        """ 

        response = client.get(f'/users/{sample_user.id}/tasks',
            headers=sample_auth_headers
        )

        data = response.get_json()

        assert response.status_code == 200
        assert isinstance(data, list)

        if data:
            task = data[0]

            assert 'id' in task
            assert 'description' in task
            assert 'completed' in task