from langchain.chat_models import init_chat_model
from dotenv import load_dotenv

load_dotenv()

model = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


def ask_ai():
    message_count = 0
    while True:
        if message_count == 5:
            print("We're done chatting.")
            break

        if message_count == 0:
            print("Hello, how can we help you? Please enter your message:")
        user_input = input()

        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        response = model.invoke(user_input)
        print("AI:", response.content)
        message_count += 1


ask_ai()
