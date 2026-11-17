from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic()

message = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=100,
    messages=[{"role": "user", "content": "Say hi in one sentence."}],
)
print(message.content[0].text)