
from langgraph.graph import StateGraph
from typing import TypedDict, List

from agents import (
    router_agent,
    rag_agent,
    planner_agent,
    reflection_agent
)


class TravelState(TypedDict):

    query: str

    category: str

    retrieved_context: List[str]

    sources: List[str]

    travel_plan: str

    final_answer: str

    retriever: object



workflow = StateGraph(TravelState)


# Add Agents

workflow.add_node(
    "router",
    router_agent
)


workflow.add_node(
    "rag",
    rag_agent
)


workflow.add_node(
    "planner",
    planner_agent
)


workflow.add_node(
    "reflection",
    reflection_agent
)



# Agent communication flow

workflow.set_entry_point("router")


workflow.add_edge(
    "router",
    "rag"
)


workflow.add_edge(
    "rag",
    "planner"
)


workflow.add_edge(
    "planner",
    "reflection"
)



workflow.set_finish_point(
    "reflection"
)



agent_app = workflow.compile()
