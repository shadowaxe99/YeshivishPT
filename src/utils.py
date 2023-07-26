```python
import json
from typing import Any, Dict

def load_json_file(filepath: str) -> Dict[str, Any]:
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def save_json_file(filepath: str, data: Dict[str, Any]) -> None:
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def format_message(message_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    return {
        "message_name": message_name,
        "data": data
    }

def validate_user_input(input: str) -> bool:
    if not input:
        return False
    return True
```