"""Unit-тесты клиента"""

import sys
import os
import unittest

sys.path.append(os.path.join(os.getcwd(), '..'))
from common.variables import RESPONSE, ERROR, USER, ACCOUNT_NAME, TIME, ACTION, PRESENCE
from client import create_message, server_response_handler


class TestClientCreateMessage(unittest.TestCase):
    """
    Класс с тестами def create_message()
    """

    def test_not_None(self):
        """Тест create_message не возвращает None"""
        self.assertIsNotNone(create_message(), True)

    def test_return_is_dict(self):
        """Тест возвращаемого типа данных (dict)"""
        self.assertTrue(type(create_message()) is dict, True)

    def test_dict_keys(self):
        """Тест наличия всех ключей словаря в возвращаемых данных"""
        keys = ['action', 'time', 'user']
        self.assertEqual(list(create_message().keys()), keys)

    def test_user_is_dict(self):
        """Тест наличия вложенного словаря по ключу user"""
        self.assertTrue(type(create_message()['user']) is dict, True)

    def test_def_create_message(self):
        """Тест коректного запроса"""
        test = create_message()
        test[TIME] = 1.1  # время необходимо приравнять принудительно
        # иначе тест никогда не будет пройден
        self.assertEqual(test, {ACTION: PRESENCE, TIME: 1.1, USER: {ACCOUNT_NAME: 'Guest'}})


class TestClientServerResponseHandler(unittest.TestCase):
    """
    Класс с тестами def server_response_handler()
    """

    def test_response_200(self):
        """Тест корректтного разбора ответа 200"""
        self.assertEqual(server_response_handler({RESPONSE: 200}), '200 : OK')

    def test_response_400(self):
        """Тест корректного разбора 400"""
        self.assertEqual(server_response_handler({RESPONSE: 400, ERROR: 'Bad Request'}), '400 : Bad Request')

    def test_no_response(self):
        """Тест исключения без поля RESPONSE"""
        self.assertRaises(ValueError, server_response_handler, {ERROR: 'Bad Request'})


if __name__ == '__main__':
    unittest.main()
