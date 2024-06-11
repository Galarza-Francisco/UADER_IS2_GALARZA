from abc import ABC, abstractmethod

class recuperadorBaseToken(ABC):
    @abstractmethod
    def get_token(self, jsonfile, jsonkey):
        pass
