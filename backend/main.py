from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_agent
# from db import save_interaction, get_all_interactions, update_interaction
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatRequest):
    try:
        print("Incoming:", req.message)

        result = run_agent(req.message)

        print("Result:", result)

        return result

    except Exception as e:
        print("ERROR:", str(e))
        return {"error": str(e)}


