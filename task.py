"""Тестовое задание на должность Стажёр-программист Python."""

import asyncio
import hashlib
import logging
import random
import sys

sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.INFO)

LOGGER = logging.getLogger('test_task')
LOGGER.setLevel(logging.DEBUG)
LOGGER.addHandler(sh)


async def output(string):
    """После задержки от 0 до 5 секунд, выводит переданную строку."""
    rnd = random.SystemRandom(0)
    await asyncio.sleep(rnd.randint(0, 5))
    LOGGER.info(string)


async def main():
    """Оператором await запускает сопрограммы output()."""
    await output('Синицын Андрей')
    await output('Стажёр-программист Python / Python Developer Trainee')
    await output('90000 рублей')


def read_stdin():
    """Считывает stdin."""
    inp = sys.stdin.readline()
    hash_inp = hashlib.sha256(inp.encode())
    LOGGER.info(hash_inp.hexdigest())


if __name__ == '__main__':
    asyncio.run(main())
    read_stdin()
