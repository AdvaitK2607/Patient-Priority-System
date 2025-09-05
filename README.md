# 🚑 Ambulance Patient Prioritization using Gemini AI

This project is an **AI-powered emergency triage assistant** that takes **emergency call transcripts** (converted from speech-to-text) and automatically:

1. **Detects the most likely medical condition** of each patient.  
2. **Ranks patients by priority** (1 = most critical, 4 = least critical).  

It uses **Google Gemini API** for natural language understanding.

---

## 📌 Features
- Accepts **realistic emergency call transcripts** (not just short symptom lists).  
- Detects likely **medical conditions** (e.g., cardiac arrest, asthma attack, fractures).  
- Outputs a **priority queue for ambulance dispatch**.  
- Lightweight — no local model downloads, only API calls.  

---

## 🖼 Example Run

**Input (Call Transcripts):**

```text
"Patient A": "Hello, please send an ambulance quickly! My teacher just collapsed. 
He was clutching his chest, complaining of severe chest pain, and now he’s unconscious. 
His blood pressure is very low.",

"Patient B": "Hi, I need help for my friend. He fell from his bike and broke his leg. 
There’s a lot of pain but he is fully awake, talking, and his vitals seem okay.",

"Patient C": "Please hurry, my daughter is struggling to breathe. 
She has a history of asthma, she can barely talk right now and is gasping for air.",

"Patient D": "Yes, my neighbor cut himself while cooking. 
He has a few minor cuts on his arm, but he’s fully conscious and the bleeding isn’t serious."
```

**Output (Gemini AI):**

🚑 Patient Priority Ranking:
```text
Patient A → Condition: Cardiac Arrest (Heart Attack) → Priority 1  
Patient C → Condition: Severe Asthma Attack → Priority 2  
Patient B → Condition: Leg Fracture → Priority 3  
Patient D → Condition: Minor Cuts → Priority 4  
```
