
import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

# Initialize the chat messages history
messages = [{"role": "assistant", "content": "How can I help?"}]

# Function to display the chat history
def display_chat_history(messages):
    for message in messages:
        print(f"{message['role'].capitalize()}: {message['content']}")

# Function to get the assistant's response
def get_assistant_response(messages):
    r = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": m["role"], "content": m["content"]} for m in messages],
    )
    response = r.choices[0].message.content
    return response

# Inform user how to exit program
print('Type Exit as prompt to exit the program')

# Main chat loop
while True:
    # Display chat history
    display_chat_history(messages)
    
    # Get user input
    prompt = input("User: ")

    if prompt.lower() == "exit":
        break

    messages.append({"role": "user", "content": prompt})
    
    # Get assistant response
    response = get_assistant_response(messages)
    messages.append({"role": "assistant", "content": response})

