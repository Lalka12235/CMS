import pytest
from app.db.orm import RemoteUser,RemoteArticle,InitDB
from app.tests.conftest import *

class TestDB:

    @staticmethod
    @staticmethod
    def test_create_table():
        # Создаем таблицы в базе данных
        InitDB.create_table()

    @staticmethod
    def test_register_user(test_user_for_register):
        username = test_user_for_register['username']
        result = RemoteUser.register_user(username)
        assert result
