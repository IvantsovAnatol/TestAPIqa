Проект представляет собой REST API, реализованный на базе FastAPI, с использованием PostgreSQL в качестве базы данных. Проект настроен для быстрого запуска через Docker Compose.

---

## Стек технологий

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Docker и Docker Compose

---

## Структура проекта

- `app/` — исходный код приложения
- `docker-compose.yml` — конфигурация для запуска сервисов
- `Dockerfile` — инструкция для сборки контейнера приложения
- `requirements.txt` — список зависимостей проекта

---

## Как запустить проект

### 1. Клонирование репозитория

```bash
git clone https://github.com/IvantsovAnatol/TestAPIqa.git
cd TestAPIqa
docker-compose up -d
API, доступно по адресу http://localhost:8000
PostgreSQL, доступный по адресу localhost:5432
или используйте документацию, по адресу http://localhost:8000/docs.
