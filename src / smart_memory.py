
import json
from pathlib import Path


class SmartMemory:

    ALLOWED_KEYS = {
        "name",
        "level",
        "learning",
        "preference"
    }

    def __init__(self):

        project_folder = Path(__file__).resolve().parent.parent

        self.file_path = project_folder / "data" / "user_memory.json"

        self.memory = {}


 
    def load_memory(self):

        if self.file_path.exists():

            with open(self.file_path, "r", encoding="utf-8") as file:
                self.memory = json.load(file)

        else:
            self.memory = {}

        # Normalize existing keys
        cleaned_memory = {}

        for key, value in self.memory.items():

            normalized_key = self.normalize_key(key)

            cleaned_memory[normalized_key] = value

        self.memory = cleaned_memory

        self.save_memory()

        return self.memory



    def save_memory(self):

        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding="utf-8") as file:

            json.dump(self.memory, file, indent=4, ensure_ascii=False)

    def get_memory(self, key):
        key = self.normalize_key(key)
        return self.memory.get(key)


    def get_all_memories(self):

        return self.memory


    def delete_memory(self, key):

        if key in self.memory:

            del self.memory[key]

            self.save_memory()

            print(f"Memory deleted: {key}")

        else:

            print(f"Memory not found: {key}")

    def normalize_key(self,key):

        key = key.lower().strip().replace("-", "_").replace(" ", "_")

        aliases = {
        "learning_goal": "learning",
        "current_learning": "learning",
        "learning_preference": "preference",
        "long_term_preferences": "preference",
        "long_term_preference": "preference"
        }

        return aliases.get(key, key)



    def add_memory(self, key, value):

        key = self.normalize_key(key)

        if key not in self.ALLOWED_KEYS:
            print(f"Memory rejected: {key} ")
            return

        if not isinstance(value,str) or not value.split():
            print("Invalid memory value.")
            return

        self.memory[key] = value.strip()

        self.save_memory()

        print(f"Memory updated: {key} = {value}")

    def update_memory(self, key, value):

        key = self.normalize_key(key)

        if key not in self.ALLOWED_KEYS:
            print(f"Update rejected: {key}")
            return

        if not isinstance(value, str) or not value.strip():
            print("Invalid value.")
            return

        old_value = self.memory.get(key)

        if old_value == value.strip():
            print(f"No change: {key}")
            return

        self.memory[key] = value.strip()

        






        
