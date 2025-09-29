# 🌍 Travel Planner AI

This project is an **AI-powered travel assistant** that helps users search for **flights and hotels** using natural language queries.  
It combines **LLM reasoning** with a **Supabase database** to understand user requests and return accurate travel options.  

---

## 📖 Overview

- Users can type queries like:  
  - *“Find me flights from Karachi to Dubai on 15th September”*  
  - *“Show me hotels in Dubai under $150 with 4-star ratings”*  

- The system automatically:  
  1. Understands the query using **LangGraph + LangChain with Ollama**  
  2. Decides whether the query is about **flights** or **hotels**  
  3. Queries the **Supabase database** for matching results  
  4. Returns a clean and structured response  

---

## 🎯 Use Case

The project is designed to **simplify travel planning** by allowing users to search in plain language instead of filling multiple forms.  
Potential applications:  

- 🧳 Personal travel planning  
- 🏨 Hotel comparison tool  
- ✈️ Flight search chatbot  
- 🌐 Integration into travel agencies’ websites  

---

## 📂 Project Components

- **Flight Agent** → Handles flight-related queries  
- **Hotel Agent** → Handles hotel-related queries  
- **Router** → Decides which agent to use  
- **Supabase Client** → Connects to travel database  
- **Flask Web App + Frontend** → Provides a simple UI for users  

---

This project demonstrates how **AI + databases + web apps** can work together to make real-world tasks (like booking travel) easier and smarter.  
