import json
import sys


import json
import sys

class recuperadorToken:
    def __init__(self, jsonfile):
        self.jsonfile = jsonfile
        self.data = self.load_json()

    def load_json(self):
        try:
            with open(self.jsonfile, 'r') as myfile:
                data = myfile.read()
            return json.loads(data)
        except FileNotFoundError:
            print(f"archivo no encontrado: {self.jsonfile}")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"error al decodificar JSON {self.jsonfile}")
            sys.exit(1)

    def get_token(self, jsonkey):
        return self.data.get(jsonkey, "Token no encontrado")

def main():
    if len(sys.argv) < 3:
        print("Usando: python getJasonNew.py <jsonfile> <jsonkey>")
        return

    jsonfile = sys.argv[1]
    jsonkey = sys.argv[2]

    recuperado = recuperadorToken(jsonfile)
    token = recuperado.get_token(jsonkey)
    print("Token: ", token)

if __name__ == "__main__":
    main()
