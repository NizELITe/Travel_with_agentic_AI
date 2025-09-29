
#working perfect from here

# router.py
from typing import Dict, Any
from langgraph.graph import StateGraph, END
from hotel_agent import hotel_agent
from flight_agent import flight_agent

# --- State definition ---
class AgentState(Dict[str, Any]):
    query: str
    hotel_result: Any
    flight_result: Any


# --- Simple classifier ---
def classify_query(query: str) -> str:
    query_lower = query.lower()
    if any(word in query_lower for word in ["hotel", "stay", "room", "accommodation"]):
        return "hotel"
    elif any(word in query_lower for word in ["flight", "ticket", "plane", "airline"]):
        return "flight"
    else:
        return "unknown"


# --- Router logic ---
def router_node(state: AgentState) -> str:
    query = state["query"]
    classification = classify_query(query)

    if classification == "hotel":
        return "hotel_agent"
    elif classification == "flight":
        return "flight_agent"
    else:
        return END


# --- Nodes ---
def hotel_node(state: AgentState) -> AgentState:
    result = hotel_agent(state["query"])   # ✅ call function directly
    return {**state, "hotel_result": result, "flight_result": None}


def flight_node(state: AgentState) -> AgentState:
    result = flight_agent(state["query"])  # ✅ call function directly
    return {**state, "flight_result": result, "hotel_result": None}


# --- Graph definition ---
workflow = StateGraph(AgentState)

workflow.add_node("hotel_agent", hotel_node)
workflow.add_node("flight_agent", flight_node)
workflow.add_node("router", lambda s: s)  # pass-through router node

workflow.add_conditional_edges(
    "router",
    router_node,
    {
        "hotel_agent": "hotel_agent",
        "flight_agent": "flight_agent",
        END: END
    }
)

workflow.set_entry_point("router")

# Expose app for main.py
app = workflow.compile()
