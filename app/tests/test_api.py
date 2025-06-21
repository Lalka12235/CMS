import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
from app.tests.conftest import *


class TestApi:


    @pytest.mark.asyncio
    async def test_register_user(test_user_for_register):
        async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
            user_data = {
                "username": "testuser",
                "password": "testpassword"
            }
            response = await ac.post('/blogs/register')
            assert test_user_for_register
            assert response == {"Register": "Success"}

    #@pytest.mark.asyncio
    #async def test_make_admin_user_fake(test_user_for_admin):
    #    async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
    #        response = await ac.put('/blogs/remote_user/make_admin_test/{username}')
    #        data = {'Admin': 'Success'}
    #        assert data
#
    #@pytest.mark.asyncio
    #async def test_login_for_access_token   (test_user_for_register):
    #    async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
    #        response = await ac.post('/token')
    #        print(response)
    #        assert response
    #@pytest.mark.asyncio
    #async def test_create_article(test_user_for_create_article):
    #    async with AsyncClient(transport=ASGITransport(app), base_url='http://test') as ac:
    #        response = await ac.post('/blogs/remote_article/create_article/{username}/{title}')
    #        print(response)
    #        assert response