import os
from dotenv import load_dotenv, find_dotenv
import anthropic
from werkzeug.testapp import test_app

print("Running from:", os.getcwd())
print("Found .env at:", find_dotenv(usecwd=True))
load_dotenv(find_dotenv(usecwd=True))
print("Key loaded:", bool(os.getenv("ANTHROPIC_API_KEY")))

client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hi in one sentence."}],
)
print(message.content[0].text)