from groq import Groq
import os
from tools import (
    log_interaction,
    edit_interaction,
    get_summary,
    suggest_action,
    fetch_interactions,
)
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_data(user_message):
    prompt = f"""
    Extract structured data from this message:
    "{user_message}"

    Return ONLY valid JSON like:
    {{
      "hcp_name": "...",
      "date": "...",
      "sentiment": "...",
      "notes": "..."
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.choices[0].message.content
             
    print("RAW AI OUTPUT:", text)


    import json
    
    try:
        
        start = text.find("{")
        end = text.rfind("}") + 1
        json_str = text[start:end]

        return json.loads(json_str)



        #return json.loads(text)

    except Exception as e:
        print("JSON ERROR:", e)

        return {
            "hcp_name": "Unknown",
            "date": "Unknown",
            "sentiment": "neutral",
            "notes": user_message
        }


def run_agent(user_message):
    message = user_message.lower()

    default_data = {
        "hcp_name": "",
        "date": "",
        "sentiment": "",
        "notes": ""
    }

    # TOOL SELECTION (LangGraph-like decision)

    if "change" in message or "edit" in message:
        updated_fields = {"sentiment": "negative"}
        result = edit_interaction(updated_fields)
        return result.get("data", default_data)

    elif "summary" in message:
        summary = get_summary()
        return {**default_data, "notes": summary["summary"]}

    elif "next" in message:
        action = suggest_action()
        return {**default_data, "notes": action["action"]}

    elif "history" in message:
        history = fetch_interactions()
        history_list = history.get("history", [])

        if history_list and history_list[0]:
            h = history_list[0]
            text = f"HCP: {h.get('hcp_name')}, Sentiment: {h.get('sentiment')}"
        else:
            text = "No interactions logged yet"

        return {**default_data, "notes": text}

    else:
        # 🔥 AI EXTRACTION
        data = extract_data(user_message)

        result = log_interaction(data)
        return result.get("data", default_data)
