# ✈️ TripCraft AI - Agentic AI Travel Planner

## Project Description

TripCraft AI is an AI-based travel planning application developed to help users create personalized travel plans for Sri Lankan destinations.

Planning a trip usually requires searching different websites for places to visit, hotels, transport options, food, and safety information. This can take a lot of time.

This project provides an intelligent travel assistant where users can enter their travel requirements and receive a generated travel plan with recommended places, activities, and travel suggestions.

The system uses Agentic AI, LangGraph, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to create useful and context-aware travel recommendations.

---

# Problem Statement

When planning a trip, travelers need to collect information from multiple sources and manually organize their itinerary.

This process can be difficult because information about destinations, attractions, transportation, and other travel details are available in different places.

TripCraft AI solves this problem by providing an AI assistant that retrieves information from a Sri Lanka tourism knowledge base and creates a customized travel plan automatically.

---

# Project Objectives

The main objectives of this project are:

- Develop an AI-powered travel planning assistant.
- Generate personalized travel itineraries.
- Use tourism documents as a reliable information source.
- Implement Retrieval-Augmented Generation (RAG).
- Apply multiple AI agents for different travel tasks.
- Improve responses using reflection-based checking.
- Provide a simple and user-friendly Streamlit interface.

---

# System Architecture

The overall architecture of TripCraft AI is shown below:

```
                    User
                     |
                     ↓
            Streamlit Interface
                     |
                     ↓
              Router Agent
                     |
                     ↓
            LangGraph Workflow
                     |
        --------------------------------
        |              |               |
        ↓              ↓               ↓
    RAG Agent     Planner Agent   Budget Agent
        |
        ↓
Sri Lanka Tourism
 Knowledge Base

                     |
                     ↓
            Attraction Agent
                     |
                     ↓
             Weather Agent
                     |
                     ↓
           Reflection Agent
                     |
                     ↓
             Final Travel Plan
```

LangGraph is used to control the communication and execution flow between different AI agents.

---

# AI Agents

## Router Agent

The Router Agent receives the user request and decides which agents are required to process the query.

---

## RAG Agent

The RAG Agent searches the tourism knowledge base and retrieves relevant information related to the user's request.

---

## Planner Agent

The Planner Agent creates the main travel itinerary using:

- User requirements
- Retrieved information
- Travel details

---

## Budget Agent

The Budget Agent provides suggestions based on the user's travel budget.

---

## Attraction Agent

The Attraction Agent identifies suitable attractions, activities, and places to visit.

---

## Weather Agent

The Weather Agent considers available weather information during travel planning.

---

## Reflection Agent

The Reflection Agent reviews the generated travel plan and improves:

- Organization
- Completeness
- Readability
- Travel suitability

---

# Agent Communication Flow

```
User Request
      |
      ↓
Router Agent
      |
      ↓
RAG Agent
      |
      ↓
Planner Agent
      |
      ↓
Budget Agent + Attraction Agent + Weather Agent
      |
      ↓
Reflection Agent
      |
      ↓
Final Travel Plan
```

Agents communicate through the shared workflow state managed by LangGraph.

---

# Agentic AI Design Patterns Used

## 1. Planning Pattern

The Planner Agent uses the planning pattern to break down the user's travel requirements and create a structured itinerary.

Implemented in:

```
agents.py
```

---

## 2. Reflection Pattern

The Reflection Agent checks the generated travel plan and improves the quality of the final response.

Implemented in:

```
agents.py
```

---

## 3. Router / Orchestrator Pattern

LangGraph works as an orchestrator that controls the order of agent execution and manages communication between agents.

Implemented in:

```
graph.py
```

---

# Model Selection Strategy

Different models are selected for different tasks instead of using one model for everything.

| Task | Model | Reason |
|---|---|---|
| Query Routing | Llama-3.1-8B-Instant (Groq) | Fast and suitable for simple routing decisions |
| Travel Plan Generation | Llama-3.3-70B-Versatile (Groq) | Better reasoning for creating detailed travel plans |
| Plan Review | Llama-3.1-8B-Instant (Groq) | Faster checking and improvement |

This approach improves the balance between:

- Response quality
- Speed
- Efficiency

---

# Retrieval-Augmented Generation (RAG)

TripCraft AI uses a Sri Lanka tourism knowledge base for retrieving travel-related information.

The knowledge base contains:

- Destination guides
- Tourist attractions
- Hotels
- Transportation details
- Food information
- Safety tips

---

# RAG Pipeline

```
Tourism PDF Documents
          |
          ↓
Document Loading
          |
          ↓
Text Splitting
          |
          ↓
Embedding Generation
          |
          ↓
Chroma Vector Database
          |
          ↓
Similarity Search
          |
          ↓
Relevant Context Retrieval
          |
          ↓
LLM Response Generation
```

---

# RAG Configuration

## Document Collection

```
73 PDF documents
```

## Text Chunking

The documents are divided into smaller text sections to improve retrieval.

```
Chunk Size: 800
Chunk Overlap: 150
```

## Embedding Model

```
sentence-transformers/all-MiniLM-L6-v2
```

## Vector Database

```
ChromaDB
```

---

# Retrieval Evaluation

The retrieval system was tested using five sample travel queries.

| Query | Retrieved Information | Result |
|---|---|---|
| Kandy visiting places | Kandy Travel Guide, Temple of the Tooth, Kandy Lake | Relevant |
| Galle attractions | Galle itinerary and attraction information | Relevant |
| Colombo city tour | Colombo city tour information | Relevant |
| Trincomalee beaches | Nilaveli Beach and Trincomalee information | Relevant |
| Ella hiking places | Retrieved unrelated Galle/Mirissa information | Not Relevant |

## Evaluation Result

The system retrieved relevant information for 4 out of 5 test queries.

The incorrect result shows that retrieval performance can be improved by adding more destination-specific documents and increasing the knowledge base.

---

# Streamlit Application

TripCraft AI provides a web interface developed using Streamlit.

Users can:

- Enter their travel requirements.
- Generate AI travel plans.
- View organized travel recommendations.

## Main Features

- 🌴 Travel assistant interface
- ✈️ Travel request input
- 🤖 AI-generated itinerary
- 📋 Structured travel recommendations

---

# Live Demo

Streamlit Community Cloud:

https://tripcraftai-uwvlqvtzqnnttdvebknjjd.streamlit.app/

---

# Project Structure

```
TripCraft_AI/

│
├── app.py
│     Streamlit application interface
│
├── agents.py
│     AI agent implementation
│
├── graph.py
│     LangGraph workflow
│
├── rag.py
│     RAG pipeline and retrieval system
│
├── data/
│     Sri Lanka tourism PDF documents
│
├── assets/
│     Application images
│
└── requirements.txt
      Required Python libraries
```

---

# Technologies Used

- Python
- LangChain
- LangGraph
- Groq API
- Llama Models
- HuggingFace Embeddings
- ChromaDB
- Streamlit
- Retrieval-Augmented Generation

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/natheera-asra/TripCraft_AI.git
```

## Navigate to Project Folder

```bash
cd TripCraft_AI
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Add API Key

Set the Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

## Run Application

```bash
streamlit run app.py
```

---

# Limitations

- The system depends on the available tourism documents.
- Real-time hotel booking is not available.
- Live weather API integration is not included.
- Information quality depends on the knowledge base.

---

# Future Improvements

Future improvements include:

- Adding real-time weather APIs.
- Integrating hotel booking services.
- Adding transport APIs.
- Supporting multiple languages.
- Developing a mobile application.
- Improving personalized recommendations.

---

# Developer

**Natheera Asra**

Project:

**TripCraft AI - Agentic AI Travel Planner**

---

# Conclusion

TripCraft AI demonstrates how Agentic AI can be used for real-world travel planning.

By combining multiple AI agents, RAG-based retrieval, vector databases, and Large Language Models, the system can generate personalized travel recommendations from a tourism knowledge base.

The project shows how AI can reduce the effort required for travel planning and provide useful recommendations for users.
