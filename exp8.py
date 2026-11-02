print("Chatbot: Hello! I am a simple chatbot.")
print("Chatbot: Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you?")

    elif "name" in user:
        print("Chatbot: I am a simple chatbot.")

    elif "how are you" in user:
        print("Chatbot: I am fine. Thank you!")

    elif "help" in user:
        print("Chatbot: I can answer simple questions.")

    elif "bye" in user:
        print("Chatbot: Goodbye!")
        break

    else:
        print("Chatbot: Sorry, I don't understand.")