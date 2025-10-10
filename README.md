# Prioriza

Prioriza é uma aplicação para gerenciamento de tarefas, permitindo criar, atualizar, listar e organizar tarefas de diferentes usuários. Ideal para quem deseja manter o dia a dia mais produtivo e organizado. ✅📋

## Para fazer a instalação das dependências
Crie um ambiente virtual isolado para as dependências do projeto.
~~~bash
python -m venv venv
~~~

Ative o ambiente virtual.
~~~bash
# Windows (bash)
source venv\Scripts\Activate
~~~

Instale as dependências do requirements.txt
~~~bash
pip install -r requirements.txt
~~~

>Certifique-se de estar dentro da **hierarquia de pastas** do projeto.

## Para rodar a aplicação em ambiente de desenvolvimento
~~~bash
python server.py
~~~

## Documentação
[![Swagger](https://img.shields.io/badge/API-Swagger-green.svg)](http://localhost:5000/docs)<br>

A API está documentada com Swagger UI.

- Documentação interativa: [http://localhost:5000/docs](http://localhost:5000/docs)

## Testes Automatizados

Esta API inclui **testes automatizados** utilizando [pytest](https://docs.pytest.org/).  
Os testes cobrem os principais endpoints da API e usam um banco de dados **em memória** para não interferir no banco real.

### Como rodar os testes
~~~bash
pytest -v
~~~
