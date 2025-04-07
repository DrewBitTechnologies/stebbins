from abc import ABC, abstractmethod
from typing import Union

class ISQLDatabase(ABC):

    @abstractmethod
    async def set_text(self, text: str, table: str, column: str, id: int=1) -> bool:
        pass

    # @abstractmethod
    # async def set_image(self, data: bytes, table: str, column: str, id: int=1) -> bool:
    #     pass

    @abstractmethod
    async def get_text(self, text: str, table: str, column: str, id: int=1) -> Union[str | None]:
        pass

    # @abstractmethod
    # async def get_image_url(self, table: str, column: str, id: int=1) -> Union[str | None]:
    #     pass

    # @abstractmethod
    # async def get_image_bytes(self, table: str, column: str, id: int=1) -> Union[bytes | None]:
    #     pass