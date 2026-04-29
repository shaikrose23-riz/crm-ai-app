# AI-First CRM HCP Module

## Overview
This project is an AI-powered CRM module designed for logging interactions with Healthcare Professionals (HCPs).  
Instead of manually filling forms, users can interact with an AI assistant that extracts and updates data automatically.

---

## Features

- AI-based interaction logging
- Chat-driven form filling
- Edit existing interactions
- Generate summary
- Suggest next actions
- View interaction history

---

## Tech Stack

Frontend:
- React
- Redux

Backend:
- FastAPI (Python)

AI:
- Groq LLM (llama-3.3-70b-versatile)

Database:
- SQLite (crm.db)

---

## Project Structure

backend/
- main.py
- agent.py
- tools.py
- db.py

frontend/
- src/
- public/

---

## How to Run

### Backend

1. Go to backend folder:
cd backend

2. Install dependencies:
pip install fastapi uvicorn groq

3. Run server:
python -m uvicorn main:app --reload

---

### Frontend

1. Go to frontend folder:
cd frontend

2. Install dependencies:
npm install

3. Run app:
npm start

---


## How It Works

- User sends message in chat
- Backend sends it to AI model
- AI extracts structured data
- Agent decides which tool to call
- Tool updates data
- Frontend form updates automatically

---

## LangGraph Concept

The system follows an agent-based flow similar to LangGraph, where:
- User input is analyzed
- A decision is made
- A specific tool is executed

---

## Example

Input:
"Met Dr. Rao yesterday, he was happy"

Output:
- HCP Name: Dr. Rao
- Sentiment: Positive
- Notes: Extracted automatically

---

## Conclusion

This project demonstrates how AI can simplify CRM workflows by replacing manual data entry with intelligent automation.
