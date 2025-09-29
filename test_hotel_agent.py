from hotel_agent import hotel_agent

# Example natural language queries
queries = [
    "Show me hotels in Dubai under $150 with 4 star rating",
    "Find hotels in Istanbul with rating above 4.5"
]

for q in queries:
    print(f"Query: {q}")
    result = hotel_agent.run(q)   # LLM will parse query and call search_hotels_tool
    print("Result:", result)
    print("-"*50)
