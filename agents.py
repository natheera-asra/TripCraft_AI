
from langchain_groq import ChatGroq
import os


# -------------------------
# Models
# -------------------------

router_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.environ["GROQ_API_KEY"]
)


planner_llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3,
    api_key=os.environ["GROQ_API_KEY"]
)


reflection_llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.2,
    api_key=os.environ["GROQ_API_KEY"]
)



# -------------------------
# Router Agent
# -------------------------

def router_agent(state):

    query = state["query"]

    response = router_llm.invoke(
        f"""
Classify this travel query.

Query:
{query}

Return:
destination,
transport,
hotel,
food,
itinerary
"""
    )

    state["category"] = response.content

    return state



# -------------------------
# RAG Agent
# -------------------------

def rag_agent(state):

    docs = state["retriever"].invoke(
        state["query"]
    )


    context = []
    sources = []


    for doc in docs:

        context.append(
            doc.page_content
        )

        sources.append(
            doc.metadata.get(
                "source",
                "Unknown"
            )
        )


    state["retrieved_context"] = context

    state["sources"] = sources


    return state



# -------------------------
# Planner Agent
# -------------------------

def planner_agent(state):

    prompt=f"""

You are TripCraft AI,
a Sri Lankan travel planning assistant.

Create a travel plan using ONLY the retrieved knowledge.

User Question:

{state["query"]}


Retrieved Knowledge:

{state["retrieved_context"]}


Rules:

- Do not invent attractions.
- Do not add outside information.
- Use only the provided travel documents.
- Create a realistic day-by-day itinerary.
- Include food and transport details if available.

"""


    response = planner_llm.invoke(prompt)


    state["travel_plan"] = response.content


    return state



# -------------------------
# Reflection Agent
# -------------------------

def reflection_agent(state):

    prompt=f"""

You are a travel quality reviewer.

Review this travel plan:

{state["travel_plan"]}


Improve:

- completeness
- readability
- realistic timing
- organization


Important:

Do not introduce new attractions.
Do not add facts outside the provided plan.


Return the final answer.

"""


    response = reflection_llm.invoke(prompt)


    state["final_answer"] = response.content


    return state
