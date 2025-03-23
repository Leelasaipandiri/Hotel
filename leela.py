import nltk
from nltk.chat.util import Chat, reflections
from datetime import datetime

# Define a list of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"what is your name?",
        ["I am a Chatbot created to assist you!", "You can call me Chatbot."]
    ],
    [
        r"how can you help me?",
        ["I can answer your questions, provide information, and assist with basic tasks."]
    ],
    [
        r"what services do you provide?",
        ["I can provide customer support, answer FAQs, and assist in resolving your issues."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad I could help!"]
    ],
    [
        r"quit|exit",
        ["Goodbye! Have a nice day!", "Bye! Take care!"]
    ],
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! How can I assist you today?"]
    ],
    [
        r"how are you?",
        ["I'm just a chatbot, but I'm here to help! How can I assist you today?"]
    ],
    [
        r"(.*) your (.*) help (.*)",
        ["I can assist you with any queries you have. Feel free to ask me anything!"]
    ],
    [
        r"(.*) what time is it|tell me the time",
        [lambda: f"The current time is {datetime.now().strftime('%H:%M:%S')}."]
    ],
    [
        r"how is the weather today?",
        ["I currently don't have access to weather data. However, you can check it online or through a weather app."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase?", "Can you provide more details?"]
    ]
]

# Initialize user name and logged conversation data
user_name = ""
conversation_log = []

# Function to handle conversation logging
def log_conversation(user_input, bot_response):
    with open("chatbot_conversation_log.txt", "a") as file:
        file.write(f"You: {user_input}\nChatbot: {bot_response}\n\n")

# Function to respond based on the time of day
def time_based_greeting():
    current_hour = datetime.now().hour
    if current_hour < 12:
        return "Good morning!"
    elif 12 <= current_hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Function to run the chatbot
def chatbot_response():
    global user_name
    print(f"Chatbot: {time_based_greeting()} I'm your customer support assistant. Type 'quit' to exit.")
    
    while True:
        user_input = input("You: ").lower()
        
        # Check for exit condition
        if user_input in ["quit", "exit"]:
            print("Chatbot: Goodbye! Have a nice day!")
            log_conversation(user_input, "Goodbye! Have a nice day!")
            break
        
        # Capture user name if provided
        if "my name is" in user_input:
            user_name = user_input.split("my name is")[-1].strip()
            bot_response = f"Nice to meet you, {user_name}! How can I assist you today?"
        else:
            bot_response = chatbot.respond(user_input)
        
        # Log the conversation
        log_conversation(user_input, bot_response)
        
        # Provide time-based greeting and respond
        if not bot_response:
            bot_response = "I'm sorry, I didn't understand that. Can you please rephrase?"
        
        print(f"Chatbot: {bot_response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot_response()
