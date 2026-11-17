import json
from pathlib import Path

class ConversationMemory:

    def __init__(self):
        # Create a permanent location for conversation memory
        project_folder = Path(__file__).resolve().parent.parent

        # Create the permanent memory file location
        self.file_path = project_folder / "data" / "conversation_memory.json"

        # Create an empty conversation history
        self.history = []

        # Load previous conversation when application starts
        self.load_memory()

    def add_message(self,role,content):

        message = {
            "role": role,
            "content": content
        }

        self.history.append(message)

        # Save every new message
        self.save_memory()

    def get_history(self):
        # Return a copy of conversation history
        return [message.copy() for message in self.history]

    def save_memory(self):

        # Create data folder if it does not exist
        self.file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(self.file_path, "w", encoding='utf-8') as file:
            json.dump(
                self.history,
                file,
                indent=4,
                ensure_ascii=False
            )

    def load_memory(self):

        if self.file_path.exists():

            try:
                with open(self.file_path, 'r',encoding='uft-') as file:
                    self.history = json.load(file)

                print("Previous conversation memory loaded!")

            except json.JSONDecodeError as error:
                print(f"Could not load previous memory:{error}, Starting fresh")
                self.history = []

        else:
            print("No previous memory found. Starting fresh")

    def clear(self):

        self.history.clear()
        self.save_memory()

        print("Conversation memory cleaned! ")
































'''

class ConversationMemory:

    def __init__(self):
        # Create an empty conversation history
        self.history = []

    def add_message(self, role, content):

        message = {
            "role": role,
            "content": content
        }

        self.history.append(message)

    def get_history(self):

        # Return a copy of conversation history
        return [message.copy() for message in self.history]

    def clear(self):

        self.history.clear()

        print("Conversation memory cleared!") '''
