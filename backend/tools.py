from datetime import datetime

# Dummy in-memory storage (we will connect DB later)
interaction_store = {}

#  LOG INTERACTION
def log_interaction(data):
    interaction_store["current"] = data
    return {"status": "logged", "data": data}


#  EDIT INTERACTION
def edit_interaction(updated_fields):
    if "current" not in interaction_store:
        return {"error": "No interaction found"}

    interaction_store["current"].update(updated_fields)
    return {"status": "updated", "data": interaction_store["current"]}


# GET SUMMARY
def get_summary():
    data = interaction_store.get("current", {})
    return {
        "summary": f"Meeting with {data.get('hcp_name')} was {data.get('sentiment')}"
    }


# SUGGEST NEXT ACTION
def suggest_action():
    data = interaction_store.get("current", {})
    if data.get("sentiment") == "positive":
        return {"action": "Schedule follow-up meeting"}
    return {"action": "Send informational email"}


# FETCH PAST INTERACTIONS
def fetch_interactions():
    return {"history": [interaction_store.get("current", {})]}