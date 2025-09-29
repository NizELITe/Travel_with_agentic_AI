from flight_agent import flight_agent

queries = [
    "Find me flights from Karachi to Dubai on 2025-09-15",
    "Flights from Lahore to Istanbul"
]

for q in queries:
    print(f"\nQuery: {q}")
    response = flight_agent(q)
    print("Flight agent response:", response)
