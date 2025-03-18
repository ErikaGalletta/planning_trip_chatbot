# Start your code here!
import os
from openai import OpenAI

# Define the model to use
model = "gpt-3.5-turbo"

# Define the client
api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("API key for OpenAI is not set in the environment variables.")
client = OpenAI(api_key=api_key)


#MULTI TURN CONVERSATIONS
#storing responses allow for conversation history, which can be fed into the model to have back and forth convos:
#before calling the model, we can also pass users questions, a list:
conversation= [{"role": "system",
                  "content":"You are a employee of a trip planning agencies tasked with answering the clients questions about an upcoming trip" } ]
questions=[
    "How far away is the Louvre from the Eiffel Tower (in miles) if you are driving?",
"Where is the Arc de Triomphe?",
"What are the must-see artworks at the Louvre Museum?"
]
for q in questions: #loop through each question to get separate answers
        user_dict= {"role": "user",
                           "content": q}
        conversation.append(user_dict) #add the user dictionary to the message passed to the model
                
        response= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation,
            temperature=0.0,
            max_tokens= 100
        )
                
        assistant_dict= {
            "role": "assistant",
            "content": response.choices[0].message.content } #the API response is stored in the assistant dictionary which is then appended to the message list (already in the correct form) for the next iteration
        conversation.append(assistant_dict)
        print("User", q, " \n","Assistant: ", response.choices[0].message.content, " \n") #this makes the output a conversation between two 
                
