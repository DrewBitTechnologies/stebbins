from abc import ABC, abstractmethod
from typing import Union

class IStorage(ABC):

    @abstractmethod
    async def save_file(self, path: str, filename: str) -> bool:
        pass

    @abstractmethod
    async def read_file(self, path: str, filename: str) -> Union[bytes | None]:
        pass
