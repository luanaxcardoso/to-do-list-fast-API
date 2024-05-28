## EAplicação Web de Lista de Tarefas com FastAPI

### Este projeto exemplifica como criar uma aplicação web de lista de tarefas usando FastAPI. Ele permite operações CRUD básicas (Criar, Ler, Atualizar, Excluir) em um arquivo JSON utilizado como banco de dados.

### Estrutura do Projeto
* FastAPI: Framework web moderno e rápido.
* Jinja2: Motor de templates para renderizar HTML.
* Starlette: Toolkit ASGI que serve como base para FastAPI.
* Pydantic: Validação de dados usando Python type hints.
* Uvicorn: Servidor ASGI para rodar a aplicação FastAPI.
* Python-multipart: Necessário para lidar com formulários.


### Para executar o projeto, é necessário instalar as dependências:

```bash

pip install fastapi
pip install uvicorn
pip install fastapi
pip install jinja2
pip install starlette
pip install pydantic
pip install python-multipart

```
```bash
uvicorn main:app --reload
```
