from langchain_ollama import ChatOllama
from supabase_client import supabase
import re

llm = ChatOllama(
    model="hf.co/bartowski/Llama-3.2-1B-Instruct-GGUF",
    temperature=0
)

def hotel_agent(query: str):
    # Better prompt
    prompt = f"""
Extract the following from the user query:
- city
- max_price (if mentioned)
- min_rating (if mentioned)

Return ONLY in this JSON format:
{{"city": "CITY_NAME", "max_price": 150, "min_rating": 4}}
If a field is missing, set it to null.
Query: "{query}"
"""
    result = llm.predict(prompt)

    # Safely parse JSON
    import json
    try:
        params = json.loads(result)
    except:
        # fallback using regex
        city_match = re.search(r'in (\w+)', query)
        city = city_match.group(1) if city_match else None
        max_price_match = re.search(r'under \$?(\d+)', query)
        max_price = float(max_price_match.group(1)) if max_price_match else None
        min_rating_match = re.search(r'(\d) star', query)
        min_rating = float(min_rating_match.group(1)) if min_rating_match else None
        params = {"city": city, "max_price": max_price, "min_rating": min_rating}

    city = params.get("city")
    max_price = params.get("max_price")
    min_rating = params.get("min_rating")

    if not city:
        return "Cannot find city in query"

    # Call Supabase
    query = supabase.table("hotels").select("*").eq("city", city)
    if max_price:
        query = query.lte("price_per_night", max_price)
    if min_rating:
        query = query.gte("rating", min_rating)

    return query.execute().data

# Test
print(hotel_agent("Show me hotels in Dubai under $150 with 4 star rating"))
