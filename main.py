# from router import app

# # Example queries
# state = {"query": "Find me flights from Karachi to Dubai on 2025-09-15"}
# print(app.invoke(state)["result"])

# state = {"query": "Show me hotels in Dubai under $150 with 4 star rating"}
# print(app.invoke(state)["result"])
# from router import app

# queries = [
#     "Find me flights from Karachi to Dubai on 2025-09-15",
#     "Show me hotels in Dubai under $150 with 4 star rating"
# ]

# for q in queries:
#     state = {"query": q}
#     response = app.invoke(state)
#     print(f"Query: {q}\nFinal Response: {response.get('result')}\n{'-'*50}")




# main.py
# from router import app

# if __name__ == "__main__":
#     queries = [
#         "Show me hotels in Dubai under $150 with 4 star rating",
#         "Find me luxury hotels in Paris",
#         "Find me flights from Karachi to Dubai on 2025-09-15",
#         "I need both hotels and flights for New York"
#     ]

#     for q in queries:
#         print("\n🚀 Running query:", q)
#         state = {"query": q}  # initial state
#         response = app.invoke(state)

#         # make it readable
#         final_state = dict(response)

#         print("📌 Full State:", final_state)
#         print("🏨 Hotel Result:", final_state.get("hotel_result"))
#         print("✈️ Flight Result:", final_state.get("flight_result"))
#         print("-" * 60)




# main.py
from router import app

if __name__ == "__main__":
    queries = [
        "Show me hotels in Dubai under $150 with 4 star rating",
        "Find me flights from Karachi to Dubai on 2025-09-15",
        "I need a cheap stay in Paris",
          # should END with no result
    ]

    for q in queries:
        print(f"\n🚀 Running query: {q}")
        state = {"query": q, "hotel_result": None, "flight_result": None}
        response = app.invoke(state)

        print("📌 Full State:", response)
        print("🏨 Hotel Result:", response.get("hotel_result"))
        print("✈️ Flight Result:", response.get("flight_result"))
        print("-" * 60)
