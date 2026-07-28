# ✈️ TripCraft AI - Agentic AI Travel Planner

## Project Overview

TripCraft AI is an Agentic AI-powered travel planning application developed to help users create personalized travel plans for Sri Lanka destinations.

The system uses multiple AI agents, LangGraph workflow orchestration, Retrieval-Augmented Generation (RAG), and Large Language Models (LLMs) to generate accurate and context-aware travel recommendations.

Instead of manually searching multiple sources, users can enter their travel requirements and receive an AI-generated itinerary containing destinations, activities, transportation details, and travel suggestions.

---

# Problem Statement

Planning a trip requires collecting information about destinations, attractions, hotels, transportation, food, and safety details from different sources.

Usually, travelers need to manually search multiple websites and organize information before creating a travel plan. This process is time-consuming and difficult for users who are unfamiliar with the destination.

TripCraft AI addresses this problem by providing an intelligent travel assistant that retrieves information from a Sri Lanka tourism knowledge base and generates customized travel plans using AI agents.

---

# Main Objectives

- Develop an AI-powered travel planning assistant.
- Generate customized day-by-day travel itineraries.
- Use tourism documents as a reliable knowledge source.
- Implement Retrieval-Augmented Generation (RAG).
- Apply multi-agent AI architecture.
- Improve generated plans using reflection-based evaluation.
- Provide an easy-to-use Streamlit interface.

---

# AI Agent Architecture

TripCraft AI uses multiple specialized AI agents that work together through a LangGraph workflow.

## Agents Used

### Router Agent

The Router Agent analyzes the user request and controls the workflow by directing the query to the required agents.

---

### RAG Agent

The RAG Agent retrieves relevant information from the Sri Lanka tourism document collection.

---

### Planner Agent

The Planner Agent generates a structured travel itinerary based on:

- User requirements
- Retrieved tourism information
- Available travel details

---

### Budget Agent

Provides travel suggestions according to user budget requirements.

---

### Attraction Agent

Finds suitable attractions and activities based on the destination.

---

### Weather Agent

Considers available weather-related information during travel planning.

---

### Reflection Agent

Reviews the generated travel plan and improves:

- Completeness
- Organization
- Readability
- Realistic timing

---

# Agent Workflow

```
User Query
     |
     ↓
Router Agent
     |
     ↓
RAG Retrieval Agent
     |
     ↓
Planner Agent
     |
     ↓
Reflection Agent
     |
     ↓
Final Travel Plan
```

LangGraph is used to manage communication and execution flow between different AI agents.

---

# Agentic AI Design Patterns Used

## 1. Planning Pattern

Implemented in:

```
agents.py - Planner Agent
```

The Planner Agent breaks down user requirements and creates a structured travel plan.

---

## 2. Reflection Pattern

Implemented in:

```
agents.py - Reflection Agent
```

The Reflection Agent evaluates the generated output and improves the final response without adding unsupported information.

---

## 3. Router / Orchestrator Pattern

Implemented in:

```
graph.py
```

LangGraph controls the order of agent execution and manages communication between agents.

---

# Model Selection Strategy

TripCraft AI uses different Large Language Models for different tasks instead of using one model for the complete workflow.

This improves efficiency by selecting suitable models based on task complexity.

| Sub-task | Model (Provider) | Reason for Selection |
|---|---|---|
| User request routing | Llama-3.1-8B-Instant (Groq) | Lightweight and fast model suitable for routing decisions. |
| Travel plan generation | Llama-3.3-70B-Versatile (Groq) | Powerful reasoning model for detailed itinerary generation. |
| Travel plan review | Llama-3.1-8B-Instant (Groq) | Efficient model for checking and improving responses. |

This model selection approach balances:

- Response quality
- Processing speed
- Computational efficiency

---

# Retrieval-Augmented Generation (RAG)

TripCraft AI uses a Sri Lanka tourism knowledge base containing travel-related documents.

The knowledge base includes:

- Destination guides
- Hotels
- Transportation information
- Attractions
- Food guides
- Safety information
- Travel recommendations

---

# RAG Pipeline

```
PDF Tourism Documents
          |
          ↓
Document Loading
          |
          ↓
Text Chunking
          |
          ↓
HuggingFace Embeddings
          |
          ↓
ChromaDB Vector Database
          |
          ↓
Similarity Retrieval
          |
          ↓
LLM Response Generation
```

---

# RAG Configuration

## Documents

```
73 PDF documents
```

## Text Processing

```
Chunk size: 800
Chunk overlap: 150
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

# RAG Evaluation

The retrieval system was tested using different travel-related queries.

| User Query | Retrieved Information | Result |
|---|---|---|
| Kandy visiting places | Kandy travel guide documents | Relevant |
| Galle travel plan | Galle itinerary documents | Relevant |
| Colombo city tour | Colombo tourism documents | Relevant |
| Trincomalee attractions | Trincomalee guide documents | Relevant |
| Ella trip planning | Sri Lanka travel documents | Relevant |

The evaluation shows that the RAG pipeline retrieves relevant tourism information for generating travel recommendations.

---

# Streamlit User Interface

TripCraft AI provides an interactive web interface developed using Streamlit.

Users can enter their travel requirements and receive AI-generated travel plans.

## UI Features

- 🌴 TripCraft AI branding
- 🖼️ Travel banner image
- ✈️ Travel request input
- 🤖 AI-generated itinerary generation
- 📋 Organized travel plan display

---

# User Interaction Flow

```
User enters travel request
          |
          ↓
Streamlit Interface
          |
          ↓
Agent Workflow Processing
          |
          ↓
RAG Knowledge Retrieval
          |
          ↓
Final Travel Plan Output
```

---

# Project Structure

```
TripCraft_AI/

│
├── app.py
│     Streamlit application interface
│
├── agents.py
│     AI agent implementations
│
├── graph.py
│     LangGraph workflow management
│
├── rag.py
│     RAG pipeline and document retrieval
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
- Retrieval-Augmented Generation (RAG)

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

## Configure API Key

Set Groq API key:

```bash
export GROQ_API_KEY="your_api_key"
```

## Run Application

```bash
streamlit run app.py
```

---

# Limitations

- The system depends on available tourism documents.
- Real-time hotel booking is not supported.
- Live weather API integration is not included.
- Travel information depends on the knowledge base updates.

---

# Future Improvements

- Add real-time weather APIs.
- Integrate hotel booking services.
- Add transportation APIs.
- Develop a mobile application.
- Add multilingual support.
- Improve personalized recommendations.

---

# Developer

**Natheera Asra**

Project:

**TripCraft AI - Agentic AI Travel Planner**

---

# Conclusion

TripCraft AI demonstrates the practical application of Agentic AI by combining multiple AI agents, LangGraph orchestration, RAG-based information retrieval, vector databases, and Large Language Models.

The project shows how AI technologies can be applied to solve real-world travel planning problems by generating personalized and context-aware travel recommendations.
