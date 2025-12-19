import google.generativeai as genai

API_KEY = "AIzaSyA06u9SwGv_diVuBkhNfXx8BcnlnvlnJy8"
genai.configure(api_key=API_KEY)
model=genai.GenerativeModel("gemini-2.5-flash")
chat = model.start_chat()
print("Welcome to the Gemini-2.5-Flash chat!")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the chat. Goodbye!")
        break

    response = chat.send_message(user_input)
    print("Gemini-2.5-Flash: " + response.text)