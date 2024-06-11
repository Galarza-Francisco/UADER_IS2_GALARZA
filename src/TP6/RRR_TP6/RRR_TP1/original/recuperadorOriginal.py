import json
import sys
from common.recuperadorBase import recuperadorBaseToken

class recuperadorTokenOriginal(recuperadorBaseToken):
    def get_token(self, jsonfile, jsonkey):
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return obj.get(jsonkey, "token no encontrado")
