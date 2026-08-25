# 🍔 Science Burger — Backend

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)

Projeto acadêmico desenvolvido em grupo para a faculdade, simulando o site de uma lanchonete fictícia (Science Burger). O projeto foi construído com apoio de IA generativa como ferramenta de estudo e assistência técnica ao longo do desenvolvimento.

Fiquei responsável pela parte de **backend**, presente neste repositório: uma API em Python com FastAPI para cadastro e login de clientes, com senhas protegidas por criptografia (bcrypt) e persistência em banco de dados MySQL.

---

## 🛠️ Tecnologias utilizadas

- **Python 3**
- **FastAPI** — framework web para criação da API
- **Uvicorn** — servidor ASGI
- **SQLAlchemy** — ORM para comunicação com o banco de dados
- **MySQL** — banco de dados relacional
- **Pydantic** — validação de dados de entrada e saída
- **bcrypt** — criptografia de senhas

## ✅ Funcionalidades

- Cadastro de clientes, com validação de dados e verificação de email duplicado
- Login de clientes, com verificação segura de senha (hash + salt via bcrypt)
- Documentação interativa automática (Swagger UI) gerada pelo FastAPI

## 📡 Endpoints

| Método | Rota                    | Descrição                     |
|--------|--------------------------|--------------------------------|
| POST   | `/api/clientes/`         | Cadastra um novo cliente       |
| POST   | `/api/clientes/login`    | Realiza login de um cliente    |

Com o servidor rodando, a documentação completa (com exemplos de cada campo) fica disponível em `/docs`.

## 📁 Estrutura do projeto

```
backend/
├── app/
│   ├── database/    # Conexão com o banco de dados (SQLAlchemy)
│   ├── models/       # Modelos das tabelas do banco
│   ├── routes/         # Rotas da API
│   ├── schemas/          # Validação de dados (Pydantic)
│   ├── services/           # Regras de negócio
│   └── main.py               # Ponto de entrada da aplicação
├── requirements.txt
└── .env                       # Variáveis de ambiente (não incluído no repositório)
```

## ▶️ Como rodar o projeto

1. Clone o repositório e entre na pasta `backend`
2. Crie um ambiente virtual e instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Crie um arquivo `.env` na raiz do `backend` com a variável de conexão com o banco:
   ```
   DATABASE_URL=mysql+mysqlconnector://usuario:senha@localhost/nome_do_banco
   ```
4. Rode o servidor:
   ```bash
   uvicorn app.main:app --reload
   ```
5. Acesse `http://127.0.0.1:8000/docs` para testar a API

## 👥 Sobre o projeto

Trabalho em grupo da faculdade, com o frontend do site desenvolvido por outro integrante do grupo. Esta parte (backend) foi desenvolvida por mim, José Augusto, com apoio de IA generativa como ferramenta de aprendizado e suporte técnico durante o processo — da modelagem do banco de dados até a criação e o teste das rotas da API.
