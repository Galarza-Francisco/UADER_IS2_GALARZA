import json
import sys
from common.recuperadorBase import recuperadorBaseToken

class recuperadorTokenSingleton(recuperadorBaseToken):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(recuperadorTokenSingleton, cls).__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.data = None
            self.initialized = True

    def load_json(self, jsonfile):
        try:
            with open(jsonfile, 'r') as myfile:
                data = myfile.read()
            self.data = json.loads(data)
        except FileNotFoundError:
            print(f"archivo no encontrado: {jsonfile}")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Error decodificacion en archivo: {jsonfile}")
            sys.exit(1)

    def get_token(self, jsonfile, jsonkey):
        if self.data is None:
            self.load_json(jsonfile)
        return self.data.get(jsonkey, "Token no encontroado")