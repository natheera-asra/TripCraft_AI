# ✈️ TripCraft AI - Agentic AI Travel Planner

## Project Overview

TripCraft AI is an AI-based travel planning application developed to help users create travel plans for Sri Lanka destinations.

The system uses AI agents, LangGraph, RAG, and Large Language Models to collect relevant information from a tourism knowledge base and generate travel recommendations.

---

## Problem Statement

Planning a trip requires information about places to visit, hotels, transportation, food, and other travel details.

Usually, users need to search different sources and manually prepare a plan. This project aims to reduce that effort by providing an AI assistant that can generate a travel plan based on user requirements.

---

## Main Objectives

- Create an AI-based travel planning assistant.
- Generate customized travel itineraries.
- Use tourism documents as a knowledge source.
- Apply RAG to retrieve relevant information.
- Use multiple agents for different travel tasks.

---

## AI Agents Used

The system contains several agents:

### Planner Agent
Creates the main travel plan based on user input.

### Budget Agent
Provides suggestions according to budget requirements.

### Attraction Agent
Finds suitable places and activities.

### Weather Agent
Considers weather-related information.

### Reflection Agent
Checks the generated plan and improves the final output.

---

## Agent Workflow

```
User Input
    |
    ↓
LangGraph Workflow
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

---

## Agentic AI Patterns Used

### 1. Planning Pattern

Used in:

```
agents.py - Planner Agent
```

The planner agent divides the user request into smaller travel planning tasks.

### 2. Reflection Pattern

Used in:

```
agents.py - Reflection Agent
```

The reflection agent reviews the generated plan and improves the response.

### 3. Router / Orchestrator Pattern

Used in:

```
graph.py
```

LangGraph controls the flow between different agents.

---

## Model Selection

Two different models are used from Groq.

| Task | Model | Reason |
|---|---|---|
| Agent routing | Llama-3.1-8B-Instant | Faster response and suitable for simple decisions |
| Travel plan generation | Llama-3.3-70B-Versatile | Better reasoning for detailed travel plans |

---

## RAG Implementation

The application uses a tourism dataset containing Sri Lanka travel information.

Dataset includes:

- Destination guides
- Hotels
- Transportation details
- Attractions
- Food information
- Safety tips

### RAG Process

```
PDF Documents
      ↓
Text Splitting
      ↓
HuggingFace Embeddings
      ↓
ChromaDB
      ↓
Relevant Information Retrieval
      ↓
LLM Response
```

### RAG Details

Documents:
```
73 PDF files
```

Text chunks:
```
119 chunks
```

Embedding model:

```
sentence-transformers/all-MiniLM-L6-v2
```

Vector database:

```
ChromaDB
```

Chunking:

```
Chunk size: 500
Overlap: 100
```

---

## Project Files

```
TripCraft_AI/

app.py
    - Streamlit interface

agents.py
    - AI agent logic

graph.py
    - LangGraph workflow

rag.py
    - Document retrieval and RAG pipeline

data/
    - Tourism documents

requirements.txt
    - Required libraries
```

---

## Technologies Used

- Python
- LangChain
- LangGraph
- Groq API
- Llama Models
- HuggingFace Embeddings
- ChromaDB
- Streamlit

---

## Running the Application

Install dependencies:

```
pip install -r requirements.txt
```

Run:

```
streamlit run app.py
```

---

## Limitations

- The system depends on the available tourism documents.
- Real-time hotel booking is not available.
- Live weather API is not integrated.
- Some travel information may require future updates.

---

## Future Improvements

- Add real-time weather information.
- Add hotel and transport APIs.
- Develop a mobile application.
- Add multilingual support.

---

## Developer

Natheera Asra

Project:
TripCraft AI - Agentic AI Travel Planner

# Conclusion

TripCraft AI demonstrates the use of Agentic AI concepts by combining multiple AI agents, RAG-based information retrieval, vector databases, and Large Language Models.

The project shows how AI technologies can be applied to solve real-world travel planning problems by generating useful and personalized travel recommendations.
