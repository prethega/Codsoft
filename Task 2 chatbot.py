

data={
    "hi":"Hi there! I'm a friendly chatbot here to assist you?",
    "hello":"Hii! How can I help you today?",
    "hey":"Hi! Im here to assist you",
    "what is your name":"I'm Jade,you can call me Jade.",
    "where are you from":"I'm from the digital world,always ready to chat and assist you!",
    "how are you":"I'm just a chatbot,Im always fine,wat about you.",
    "do you have any hobbies or interests?":"I'm always busy helping users, so my hobby is chatting with people like you!",
    "what did you eat today?":"I don't eat,but I can help you find delicious recipes and food-related information.",
    "what's your favorite color?":"I'm a chatbot,so I don't have personal preferences for colors.",
    "do you enjoy listening to music?":"I can't listen to music,but I'm here to chat about it, recommend you with some good music!",
    "bye":"Bye! Take care and have a great day!",
    "jade":"hi,how can i assist you ?",
}
def get_response(user_input):
    for pattern,response in data.items():
        if pattern in user_input:
            return response
    return "I'm sorry,I didn't understand that.Can you please rephrase your sentence?"
print("Bonita: Hi! I'm a simple chatbot,I'm here to assist you!")
while True:
    user_input=input("Me: ")
    if user_input=='bye':
       print("Jade: Goodbye! Have a great day!")
       break
    response=get_response(user_input)
    print("Jade:",response)
