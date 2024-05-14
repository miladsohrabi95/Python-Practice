import random

# Define responses for different types of user input
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!"],
    "can you help me": ["Sure! Shoot!", "I'm at your service!", "What seems to be the problem?"],
    "can you help me?": ["Sure! Shoot!", "I'm at your service!", "What seems to be the problem?"],
    "how are you doing": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!"],
    "how are you doing?": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!"],
    "how are you": ["I'm good, thank you!", "I'm doing well, thanks for asking.", "All good!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm sorry, I don't understand.", "Could you please rephrase that?", "I'm not sure what you mean."],
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    if user_input in responses:
        return random.choice(responses[user_input])
    else:
        return random.choice(responses["default"])

# Main function to run the chatbot
def main():
    print("Chatbot: Hi! I'm a simple chatbot. You can start chatting with me or type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            response = get_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
