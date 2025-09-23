def test_signin(client):
    response = client.post('/auth/signin', follow_redirects=True, json={
        'name': 'Douglas Faria',
        'email': 'douglas@email.com',
        'password': '123456',
    })

    assert response.status_code == 301
    assert response.request.path == "/login"

def test_login(client):
    response = client.post('/auth/login', json={
        'email': 'johndoe@email.com',
        'password': '123456'
    })

    data = response.get_json()

    assert response.status_code == 200
    assert 'message' in data == 'Olá, John! Seja bem-vindo ao Prioriza!'
    assert 'token' in data