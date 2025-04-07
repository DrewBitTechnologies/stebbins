from .meta.sql_db_interface import ISQLDatabase
from typing import Union
import aiosqlite

class Sqlite3db(ISQLDatabase):

    def __init__(self, database: str):
        self.database = database
    
    async def set_text(self, text, table, column, id=1) -> bool:
        try:
            query = f"UPDATE {table} SET {column} = ? WHERE id = ?"
            
            async with aiosqlite.connect(self.database) as db:
                async with db.cursor() as cursor:
                    await cursor.execute(query, (text, id,))
                    await db.commit()
                
            return True
        except Exception as e:
            print(e)
            return False
        
    async def get_text(self, table, column, id=1) -> Union[str | None]:
        try:
            query = f"SELECT {column} FROM {table} WHERE id = ?"

            async with aiosqlite.connect(self.database) as db:
                async with db.cursor() as cursor:
                    ret = await cursor.execute(query, (id,))
                    result = await ret.fetchone()
                    return result[0] if result else None
                                
        except Exception as e:
            print(e)
            return None
    
    async def set_reserve_status(self, text: str) -> bool:
        return await self.set_text(text=text, table="home_screen", column="reserve_status_text")
    
    async def get_reserve_status(self) -> Union[str | None]:
        return await self.get_text(table="home_screen", column="reserve_status_text")
    