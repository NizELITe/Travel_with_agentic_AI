

from langchain_ollama import ChatOllama
from supabase_client import supabase
import json, re

llm = ChatOllama(model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF", temperature=0)

def flight_agent(query: str):
    prompt = f"""
Extract origin, destination, and departure_date (YYYY-MM-DD) from query.
Return JSON: {{"origin": "...", "destination": "...", "departure_date": "..."}}
Query: "{query}"
"""
    try:
        result = llm.invoke(prompt)
        if isinstance(result, list):
            result = result[0]
        params = json.loads(result)
    except Exception:
        origin = re.search(r'from (\w+)', query)
        dest = re.search(r'to (\w+)', query)
        date = re.search(r'(\d{4}-\d{2}-\d{2})', query)
        params = {
            "origin": origin.group(1) if origin else None,
            "destination": dest.group(1) if dest else None,
            "departure_date": date.group(1) if date else None
        }

    q = supabase.table("flights").select("*").eq("origin", params["origin"]).eq("destination", params["destination"])
    if params.get("departure_date"):
        q = q.eq("departure_date", params["departure_date"])
    data = q.execute().data
    print("Flight agent response:", data)
    return data
