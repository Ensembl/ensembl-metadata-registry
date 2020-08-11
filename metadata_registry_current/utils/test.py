from typing import NamedTuple
import json

DATA = [{
    'field1': 1,
    'field2': ['a', 'b', 'c']
}]

class OldObject(NamedTuple):
    field1: int
    field2: list

class NewObject(NamedTuple):
    new_field: list

def load_data(data: dict) -> OldObject:
    return OldObject(**data)

def convert(old_data: OldObject) -> NewObject:
    field1_val = old_data.field1
    return NewObject([f'{field1_val}-{field2_val}' for field2_val in old_data.field2])

if __name__ == '__main__':
    for record in DATA:
        print(f'Old Data: {json.dumps(record, indent=2)}')
        old_data = load_data(record)
        new_data = convert(old_data)
        print(f'New Data: {json.dumps(new_data, indent=2)}')

