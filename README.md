# Visitas comerciais

Projeto Python com SQLAlchemy 2, Alembic, psycopg 3 e PostgreSQL em Docker Compose.

## Requisitos

- Python 3.11 ou superior
- Docker Desktop com Docker Compose

## Início rápido com Docker

1. Copie `.env.example` para `.env` e altere a palavra-passe.
2. Inicie PostgreSQL e aplique as migrações:

   ```powershell
   docker compose up --build
   ```

O serviço `migrate` termina depois de aplicar as migrações; o PostgreSQL continua em execução. Para iniciar apenas a base de dados, use `docker compose up -d db`.

## Desenvolvimento local

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -e .
Copy-Item .env.example .env
docker compose up -d db
alembic upgrade head
```

O `DATABASE_URL` local deve usar o endereço `localhost`, conforme o `.env.example`. Dentro do Compose, a aplicação liga ao serviço `db`.

## Criar migrações

Depois de alterar os modelos em `app/models.py`:

```powershell
alembic revision --autogenerate -m "descricao da alteracao"
alembic upgrade head
```
