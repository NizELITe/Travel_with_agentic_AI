from flight_agent import flight_agent
from hotel_agent import hotel_agent

def smart_router(query: str):
    query_lower = query.lower()
    if "flight" in query_lower or "fly" in query_lower:
        return flight_agent(query)
    elif "hotel" in query_lower or "stay" in query_lower:
        return hotel_agent(query)
    else:
        return "Cannot determine agent"

# Test queries
queries = [
    "Find me flights from Karachi to Dubai on 2025-09-15",
    "Show me hotels in Dubai under $150 with 4 star rating"
]

for q in queries:
    result = smart_router(q)
    print(f"\nQuery: {q}\nResult: {result}")
