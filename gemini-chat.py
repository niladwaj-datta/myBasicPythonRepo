import google.generativeai as genai

API_KEY = "AIzaSyC4KKXT29wutK5pLQcsKmE-C-PXoWUF1ZI"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()
print("Welcome to the Gemini-2.0-Flash chat!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Gemini-2.0-Flash: " + response.text)