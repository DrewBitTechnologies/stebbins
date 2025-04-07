import unittest
import asyncio
from src.sqlite3_db import Sqlite3db

db = Sqlite3db("tests/sqlite.db", "tests")

async def get_set_reserve_status(text: str):
    diff_text = text + "fuck"
    await db.set_reserve_status(text=diff_text)

    await db.set_reserve_status(text=text)

    return await db.get_reserve_status()

class TestSQLite3(unittest.TestCase):

    def test_get_set_reserve_status(self):
        asyncio.run(get_set_reserve_status(text="Hello!")) == "Hello!"