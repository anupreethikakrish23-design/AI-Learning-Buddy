from src.llm_client import OllamaClient

def test_conversation_memory():

    # Create one AI client
    ai = OllamaClient()

    # Clear old memory for a fresh test
    ai.reset_memory()

    print("\n===== AI LEARNING BUDDY MEMORY TEST ======")

    questions = [
        "My name is Anu",
        "I'm learning python"
    ]

    for question in questions:
        print("User: ", question)

        result = ai.chat(question, level="beginner")

        print("AI: ", result['answer'])

    print("\n===== FIRST SESSION COMPLETED =====")
    
     # Create a new client to simulate restarting the application

    ai2 = OllamaClient()

    print("\n===== TESTING PERSISTENT MEMORY =====")

    result = ai2.chat(
        "What is my name and what am I learning?",
        level = "beginner"
    )

    print("AI:", result["answer"])

    print("\n===== MEMORY TEST COMPLETED =====")

    
'''
 
    # Display conversation history
    print("\n=====Conversation History =====")

    for message in ai.conversation_history:

        print(message['role']), ":", message["content"]

    # Display usage report
    print("\n===== USAGE REPORT =====")

    print("Model:", result4["model"])
    print("Input tokens:", result4["input_tokens"])
    print("Output tokens:", result4["output_tokens"])
    print("Total tokens:", result4["total_tokens"])
    print("Response time:", result4["response_time"], "seconds")

    print("\n===== MEMORY TEST COMPLETED =====")
'''

if __name__ == "__main__":
    test_conversation_memory()



'''    # Question 1

    result1 = ai.chat(
        "My name is Anu.",
        level = "beginner"
    )

    print("\nUser: My name is anu.")
    print("AI: ", result1["answer"])

    # Question 2
    result2 = ai.chat(
        "What is my name?",
        level = "beginner"
    )
    print("\nUser: What is my name?")
    print("AI: ", result2["answer"])

    # Question 3
    result3 = ai.chat(
        "I am learning Python. Please remember that.",
        level="beginner"
    )
    print("\nUser: I am learning Python. Please remember that.")
    print("AI:", result3["answer"])

    # Question 4
    result4 = ai.chat(
        "What am I learning?",
        level="beginner"
    )

    print("\nUser: What am I learning?")
    print("AI:", result4["answer"])
'''