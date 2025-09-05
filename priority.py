import os
import google.generativeai as genai

# 🔑 Set your Gemini API key here
os.environ["GOOGLE_API_KEY"] = "API KEY HERE"  # Replace with your actual API key

# Configure Gemini
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Simulated call transcripts (already converted from speech-to-text)
patients = {
    "Patient A": "Hello, please send an ambulance quickly! My teacher just collapsed. He was clutching his chest, complaining of severe chest pain, and now he’s unconscious. His blood pressure is very low.",
    "Patient B": "Hi, I need help for my friend. He fell from his bike and broke his leg. There’s a lot of pain but he is fully awake, talking, and his vitals seem okay.",
    "Patient C": "Please hurry, my daughter is struggling to breathe. She has a history of asthma, she can barely talk right now and is gasping for air.",
    "Patient D": "Yes, my neighbor cut himself while cooking. He has a few minor cuts on his arm, but he’s fully conscious and the bleeding isn’t serious."
}

# Build the triage prompt
prompt = """You are a medical triage AI for ambulance dispatch.
Input is call transcripts (converted from speech-to-text).
For each patient:
1. Detect the most likely CONDITION or DISEASE from the call.
2. Rank patients by PRIORITY (1 = most critical, 4 = least critical).

Output in this format:
Priority Ranking:
1. Patient X → Condition: <condition> → Priority level
2. Patient Y → Condition: <condition> → Priority level
"""

for patient, call_text in patients.items():
    prompt += f"\n{patient} (Call Transcript): {call_text}"

# Call Gemini
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content(prompt)

# Show results
print("🚑 Patient Priority Ranking:\n")
print(response.text)
