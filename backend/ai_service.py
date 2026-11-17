import os
from dotenv import load_dotenv, find_dotenv
import anthropic

# Load ANTHROPIC_API_KEY from GlucoCircle/.env (same setup as test_ai.py)
load_dotenv(find_dotenv(usecwd=True))
client = anthropic.Anthropic()

SYSTEM_PROMPT = (
    "You are the assistant inside GlucoCircle, a glucose tracking app. "
    "Give clear, general information. You are not a doctor: do not diagnose "
    "or change medication doses, and tell users to contact their care team "
    "for medical decisions or readings that seem dangerous."
)

def ask_claude(user_message):
    message = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    return message.content[0].text