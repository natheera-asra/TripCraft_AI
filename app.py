
import streamlit as st
from rag import create_retriever
from graph import agent_app


# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="TripCraft AI",
    page_icon="🌴",
    layout="wide"
)


# ---------------------------
# Custom CSS
# ---------------------------

st.markdown(
"""
<style>

.title {
    font-size: 48px;
    font-weight: bold;
    text-align: center;
    color: #0077b6;
}

.subtitle {
    font-size: 22px;
    text-align: center;
    color: gray;
}

.card {
    padding: 20px;
    border-radius: 15px;
    background-color: #f5f9ff;
}

</style>
""",
unsafe_allow_html=True
)


# ---------------------------
# Header
# ---------------------------

st.markdown(
"""
<div class="title">
🌴 TripCraft AI
</div>

<div class="subtitle">
Your Intelligent Sri Lankan Travel Planner
</div>
""",
unsafe_allow_html=True
)


# ---------------------------
# Tourism Image
# ---------------------------

st.image(
    "assets/places.jpeg",
    caption="Explore Sri Lanka with TripCraft AI",
    use_container_width=True
)


st.divider()


# ---------------------------
# User Input
# ---------------------------

st.subheader("✈️ Plan Your Trip")


query = st.text_area(
    "Enter your travel request",
    placeholder="Example: Plan a 3 day budget trip to Kandy with food and transport"
)


# ---------------------------
# Generate Button
# ---------------------------

if st.button("🚀 Generate Travel Plan"):

    if query:

        with st.spinner("AI agents are planning your journey..."):


            # Create Retriever

            retriever = create_retriever()


            # Run LangGraph

            result = agent_app.invoke({

                "query": query,

                "category": "",

                "retrieved_context": [],

                "travel_plan": "",

                "final_answer": "",

                "retriever": retriever

            })


        st.success("Travel plan generated successfully!")


        st.divider()


        st.subheader("🧳 Your Travel Plan")


        st.write(
            result["final_answer"]
        )


        # Sources

        if "sources" in result:

            st.subheader("📚 Knowledge Sources")

            for source in set(result["sources"]):
                st.write("📄", source)


    else:

        st.warning(
            "Please enter a travel request"
        )


st.divider()

st.caption(
"Powered by LangGraph + LangChain + Groq + Chroma RAG"
)
