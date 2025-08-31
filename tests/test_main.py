import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_create_and_get_question():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Создаем вопрос
        response = await ac.post("/questions/", json={"text": "Что такое Python?"})
        assert response.status_code == 200
        question = response.json()
        assert question["text"] == "Что такое Python?"

        question_id = question["id"]
        # Получаем вопрос по ID
        response = await ac.get(f"/questions/{question_id}")
        assert response.status_code == 200
        fetched_question = response.json()
        assert fetched_question["id"] == question_id
        assert fetched_question["text"] == "Что такое Python?"