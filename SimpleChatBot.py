# Function to generate chatbot response
def chatbot_response(user_input) :
    user_input = user_input.lower()
    if user_input in ["hello", "hi", "hey", "hii"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye","see you"]:
        return "Goodbye! "
    return "sorry, I don't understand that."
# Main chatbot loop
def run_chatbot():
    print("welcome to the sing  le chatbot! (Type 'bye' to exit)" )
    while True:
        user_message = input("You: ")
        reply = chatbot_response(user_message)
        print("chatbot:", reply)
        if user_message.lower() in ["bye", "goodbye","see you"]:
            break
# Run the chatbot
run_chatbot()
