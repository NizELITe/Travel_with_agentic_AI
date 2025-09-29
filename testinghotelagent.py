from hotel_agent import hotel_agent

queries = [
    "Show me hotels in Dubai under $150 with 4 star rating",
    "Find hotels in Istanbul"
]

for q in queries:
    print(f"\nQuery: {q}")
    response = hotel_agent(q)
    print("Hotel agent response:", response)
