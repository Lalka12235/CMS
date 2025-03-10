import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from app.tests.conftest import *


class TestApi:


    @pytest.mark.asyncio
    async def test_register_user(test_user_for_register):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.post(f'/blogs/register/{test_user_for_register}')
            assert response.status_code == 200  # Ожидаем успешный ответ
            data = response.json()
            assert data['Register'] == 'Success'

    @pytest.mark.asyncio
    async def test_make_admin_user_fake(test_user_for_register):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            response = await ac.put('/blogs/remote_user/make_admin_test/{username}')
            data = {'Admin': 'Success'}
            assert data