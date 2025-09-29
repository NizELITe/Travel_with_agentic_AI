# 🌍 Travel Planner AI

This project is an **Agentic AI-powered travel assistant** that helps users search for **flights and hotels** using natural language queries.  
It uses **LangGraph**, **LangChain**, and a **Supabase database** to reason about user requests and route them to the right agent.  

---

## 📖 Overview

- Users can type queries like:  
  - *“Find me flights from Karachi to Dubai on 15th September”*  
  - *“Show me hotels in Dubai under $150 with 4-star ratings”*  

- The system automatically:  
  1. Interprets the query using **LangChain + Ollama**  
  2. Uses a **LangGraph router** to decide whether it’s a **flight** or **hotel** request  
  3. Calls the respective **Agent** (Flight Agent / Hotel Agent)  
  4. Queries **Supabase** for structured travel data  
  5. Returns a clean result to the user via a **Flask web app**  

---

## 🧠 Agentic AI Workflow (LangGraph + LangChain)

This project demonstrates how **Agentic AI** works with multiple specialized agents:  

- **Router (LangGraph)**: Acts as the **decision-maker**, routing queries to the correct agent  
- **Flight Agent**: Handles flight-related queries and fetches from Supabase  
- **Hotel Agent**: Handles hotel-related queries and fetches from Supabase  
- **Supabase Client**: Connects agents to a structured travel database  
- **LangChain Integration**: Provides LLM reasoning, query parsing, and response formatting  

This **modular, agentic design** makes the system scalable — new agents (e.g., Car Rentals, Tours) can be added easily.  

---

## 🎯 Use Cases

- 🧳 **Personal Travel Planning** – Quickly find flights & hotels  
- 🏨 **Hotel Comparison** – Filter hotels by budget, rating, location  
- ✈️ **Flight Search Chatbot** – Ask in plain English instead of using forms  
- 🌐 **Travel Agency Integration** – Add conversational AI to travel websites  

---

## 📂 Project Components

- `flight_agent.py` → Handles flight-related queries  
- `hotel_agent.py` → Handles hotel-related queries  
- `router.py` → LangGraph router that decides query type  
- `supabase_client.py` → Connects to travel database  
- `main.py` → Flask web app entry point  
- `templates/` → Jinja2 templates (index, results, base layout)  
- `static/` → CSS & JS frontend files  

---

## 🚀 Tech Stack

- **LangGraph** → Multi-agent orchestration  
- **LangChain** → LLM reasoning and query parsing  
- **Ollama** → Local LLM integration  
- **Supabase** → Travel database backend  
- **Flask** → Web framework for frontend + backend integration  

---

This project demonstrates how **Agentic AI (LangGraph + LangChain)** can be applied in **real-world travel planning**, combining reasoning, routing, and database querying in a clean workflow.  
