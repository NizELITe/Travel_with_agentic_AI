
from langchain_ollama import ChatOllama
from supabase_client import supabase
import json, re

llm = ChatOllama(model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF", temperature=0)

def hotel_agent(query: str):
    prompt = f"""
Extract city, max_price, min_rating from query.
Return JSON: {{"city": "...", "max_price": 0, "min_rating": 0}}
Query: "{query}"
"""
    try:
        result = llm.invoke(prompt)
        if isinstance(result, list):
            result = result[0]
        params = json.loads(result)
    except Exception:
        city = re.search(r'in (\w+)', query)
        price = re.search(r'under \$?(\d+)', query)
        rating = re.search(r'(\d) star', query)
        params = {
            "city": city.group(1) if city else None,
            "max_price": float(price.group(1)) if price else None,
            "min_rating": float(rating.group(1)) if rating else None
        }

    q = supabase.table("hotels").select("*").eq("city", params["city"])
    if params.get("max_price"):
        q = q.lte("price_per_night", params["max_price"])
    if params.get("min_rating"):
        q = q.gte("rating", params["min_rating"])
    data = q.execute().data
    print("Hotel agent response:", data)
    return data


