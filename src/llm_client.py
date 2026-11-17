
import requests
import time
import os

from dotenv import load_dotenv

from src.prompt_manager import PromptManager
from src.conversation_memory import ConversationMemory


# Load project configuration
load_dotenv()


class OllamaClient:

    def __init__(self):

        self.model = os.getenv(
            "OLLAMA_MODEL",
            "llama3.2:1b"
        )

        self.base_url = os.getenv(
            "OLLAMA_BASE_URL",
            "http://localhost:11434"
        )

        self.api_url = f"{self.base_url}/api/chat"

        # Initialize prompt manager
        self.prompt_manager = PromptManager()

        # Initialize conversation memory
        self.memory = ConversationMemory()

    @property
    def conversation_history(self):
        # Maintain convenient access to conversation history
        return self.memory.get_history()

    def chat(self, question, level="advanced"):

        # Get system prompt
        system_prompt = self.prompt_manager.get_prompt(level)

        # Prepare messages
        messages = [
            {
                "role": "system",
                "content": system_prompt
            }
        ]

        # Add previous conversation
        messages.extend(self.memory.get_history())

        # Add current user question
        messages.append({
            "role": "user",
            "content": question
        })

        # Prepare API payload
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False
        }

        start_time = time.perf_counter()

        try:

            response = requests.post(
                self.api_url,
                json=payload,
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            response_time = round(
                time.perf_counter() - start_time,
                2
            )

            # Extract AI response
            answer = data["message"]["content"]

            # Extract token usage
            input_tokens = data.get(
                "prompt_eval_count", 0
            )

            output_tokens = data.get(
                "eval_count", 0
            )

            # Save successful conversation
            self.memory.add_message(
                "user",
                question
            )

            self.memory.add_message(
                "assistant",
                answer
            )

            return {
                "answer": answer,
                "model": self.model,
                "input_tokens": input_tokens,
                "output_tokens": output_tokens,
                "total_tokens": (
                    input_tokens + output_tokens
                ),
                "response_time": response_time
            }

        except requests.exceptions.ConnectionError:

            raise RuntimeError(
                "Cannot connect to Ollama. "
                "Please check whether Ollama is running."
            )

        except requests.exceptions.Timeout:

            raise RuntimeError(
                "The AI model took too long to respond."
            )

        except requests.exceptions.HTTPError as error:

            raise RuntimeError(
                f"Ollama API error: {error}"
            )

        except (KeyError, ValueError) as error:

            raise RuntimeError(
                f"Invalid response received from Ollama: {error}"
            )

    def reset_memory(self):

        self.memory.clear()
