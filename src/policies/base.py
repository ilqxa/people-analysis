from abc import ABC, abstractmethod
from typing import Any


class Policy(ABC):
    @abstractmethod
    def apply_to(self, o: Any) -> bool:
        ...