"""Тест task.py."""

import unittest
from unittest.mock import patch

from task import output, read_stdin


class TestClassTask(unittest.IsolatedAsyncioTestCase):
    """Класс тестирования асинхронных функций модуля task."""

    async def test_output(self):
        """Тест корректного вывода output()."""
        with self.assertLogs() as captured:
            await output('Синицын Андрей')
            self.assertEqual(
                captured.records[0].getMessage(), 'Синицын Андрей',
            )


class TestClassTaskInput(unittest.TestCase):
    """Класс тестирования синхронных функций модуля task."""

    def test_read_stdin(self):
        """Тестирование функции read_stdin.

        Проверка на корректную длину после получения
        строки методом hexdigest()
        """
        length_hash = 64
        with patch('sys.stdin.readline', return_value='Tom'):
            with self.assertLogs() as captured:
                read_stdin()
                self.assertEqual(
                    len(captured.records[0].getMessage()), length_hash,
                )


if __name__ == '__main__':
    unittest.main()
