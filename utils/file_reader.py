import json
import os


class FileReader:

    @staticmethod
    def read_json(path):

        base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        full_path = os.path.join(base_path, path)

        with open(full_path) as file:
            return json.load(file)