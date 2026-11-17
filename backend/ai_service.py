import os
import json
from dotenv import load_dotenv, find_dotenv
import anthropic

# Load ANTHROPIC_API_KEY from GlucoCircle/.env (same setup as test_ai.py)
load_dotenv(find_dotenv(usecwd=True))
client = anthropic.Anthropic()

#setting the personality and behavior of the AI assistant (Claude) for GlucoCircle
SYSTEM_PROMPT = (
    "You are Mira, the assistant inside GlucoCircle, a glucose tracking app. "
    "Give clear, general information. You are not a doctor: do not diagnose "
    "or change medication doses, and tell users to contact their care team "
    "for medical decisions or readings that seem dangerous. You are friendly, supportive and informative, and you explain things in simple language."
)

# Function to send a request to Claude API and get a response
def ask_claude(user_message):
    message = client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=1500,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    return "".join(block.text for block in message.content if block.type == "text")

#Claude prompt for generating insights from glucose analysis results
def generate_glucose_insights(results):
    analysis_data = json.dumps(results, indent=2)

    prompt = f"""
You are Mira, the assistant inside GlucoCircle, a glucose tracking app. 

Glucose analysis:
{analysis_data}

Explain:
1. The overall trends in the user's glucose readings.
2. Any potential concerns or patterns that the user should be aware of.
3. What the average, minimum, and maximum glucose levels represent.
4. Suggestions for maintaining healthy glucose levels, such as lifestyle tips.

Use clear, simple language suitable for a general audience. 
Avoid medical jargon.
Do not provide medical advice, diagnoses, or medication changes. 
Emphasize that the user should consult their healthcare provider for any concerns.
Do not make assumptions about the user's health or medical history or causes for glucose changes without supporting information.
"""
    return ask_claude(prompt)
