import json
from pydantic import ValidationError

from models import DividendInput


class InputError(Exception):
    def __init__(self, msg, inner_exc=None):
        self.msg = msg
        self.inner_exc = inner_exc

    def __str__(self):
        str_repr = f"{type(self).__name__}: {self.msg}"
        if self.inner_exc:
            str_repr += f"\nInner exception: {self.inner_exc}"
        return str_repr


class InputManager:
    @staticmethod
    def load_input(input_json_file: str) -> DividendInput:
        try:
            with open(input_json_file, 'r') as f_handler:
                input_raw_data = json.loads(f_handler.read())
        except IOError as ex:
            raise InputError(f"File {input_json_file} could not be loaded", ex)
        except json.JSONDecodeError as ex:
            raise InputError(f"File {input_json_file} is not a valid JSON", ex)

        try:
            return DividendInput(**input_raw_data)
        except ValidationError as ex:
            raise InputError(f"JSON from file {input_json_file} is invalid", ex)
