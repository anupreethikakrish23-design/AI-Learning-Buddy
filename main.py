
from src.llm_client import OllamaClient 
#from src.prompt_manager import PromptManager


def main():

    # Create an AI client
    ai = OllamaClient()

    print("\n===================================")
    print("           AI Learning Buddy         ")
    print("=====================================")

    print("Model: ", ai.model)
    print("/exit  -   Exit application")
    print("/reset  -   Clear conversation history")

    print("Start chatting with your AI Buddy! ")

    while True:
        question = input("You: ").strip()

        if not question:
            continue

        if question.lower() == "/exit":
            print("Thankyou for using AI Learning Buddy! ")
            break

        if question.lower() == "/reset":
            ai.reset_memory()
            continue

        try: 
            result = ai.chat(
                question,
                level = "beginner"
            )

            print("AI Buddy: ", result["answer"])

            print('\n==========USAGE REPORT==========')
            print("Model", result['model'])
            print("Input tokens", result['input_tokens'])
            print("Output tokens", result['output_tokens'])
            print("Total tokens", result['total_tokens'])
            print("Response time", result['response_time'], 'seconds')

        except RuntimeError as error:
            print("\nError: ", error)


if __name__ == "__main__":
    main()









   
   
    '''
    # Get AI response

    result = ai.chat(
        question,
        level = "advanced" 
        )

    # Display AI answer

    print("\n==========AI ANSWER==========")
    print(result["answer"])

    # Display Usage information
    print('\n==========USAGE REPORT==========')

    print("Model", result['model'])
    print("Input tokens", result['input_tokens'])
    print("Output tokens", result['output_tokens'])
    print("Total tokens", result['total_tokens'])
    print("Response time", result['response_time'], 'seconds') 





manager = PromptManager()

prompt = manager.get_prompt("beginner")

print(prompt) '''