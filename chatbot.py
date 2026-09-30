def chatbot():
    print("===== BASIC CHATBOT =====")
    print("Chatbot: Hello! How can I help you?")
    print("Chatbot: Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")

        elif user_input == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()