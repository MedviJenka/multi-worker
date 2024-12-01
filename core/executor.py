from typing import Optional
from abc import ABC, abstractmethod


class Executor(ABC):

    """abstract async executor for complex executions"""

    @abstractmethod
    async def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        pass
    