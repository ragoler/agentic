# AI Trip Planner - Technical Architecture

## Project Overview
An AI-powered agentic system, based on the Agent Development Kit (ADK) standard, to help users plan trips.

## Technology Stack

### Backend
- **Framework**: Python with FastAPI
- **Agent Framework**: ADK Principles (Orchestrator and Specialized Agents)
- **API Gateway**: Managed Connectivity Platform (MCP) for all external API access
- **Data Validation**: Pydantic
- **External API Client**: HTTPX for asynchronous calls via MCP

### Frontend
- **Framework**: None (Vanilla JS)
- **Styling**: Basic HTML and CSS
- **API Client**: Fetch API

### Deployment
- **Application Server**: Uvicorn
- **Containerization**: Docker
- **Deployment Target**: Local execution initially, with a goal for Google Cloud Run

## Agentic Architecture (ADK)
The system is composed of a central orchestrator agent that manages a team of specialized agents.

- **Orchestrator Agent**: The "brain" of the operation. It receives user requests from the API layer, delegates tasks to the appropriate specialized agents, and synthesizes their findings into a coherent trip plan.
- **Specialized Agents**: Each agent is an expert in a specific domain:
    - **Flight Agent**: Searches for flight options.
    - **Hotel Agent**: Finds accommodation.
    - **Attraction Agent**: Discovers local points of interest.
    - **Transportation Agent**: Identifies local transport options.

## Managed Connectivity Platform (MCP)
All communication with external, third-party APIs (e.g., Skyscanner, Booking.com) is routed through a centralized MCP Gateway.
- **Purpose**: The MCP acts as a single, secure entry point for all external data. It manages API keys, handles request/response formatting, and provides a consistent interface for the specialized agents.
- **Benefit**: This decouples the agents from the specific implementations of external APIs, making the system more modular and easier to maintain.

## Directory Structure
```
trip_planner/
├── .conductor/           # Project management files
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py        # FastAPI app instance
│   │   ├── api/           # API endpoint definitions (interacts with Orchestrator)
│   │   │   └── v1/
│   │   │       └── trip.py
│   │   ├── agents/        # Core agent logic
│   │   │   ├── orchestrator.py
│   │   │   ├── flight_agent.py
│   │   │   └── hotel_agent.py
│   │   ├── mcp_gateway/   # Managed Connectivity Platform
│   │   │   ├── __init__.py
│   │   │   └── external_apis.py
│   │   ├── core/          # Configuration
│   │   └── models/        # Pydantic models
│   └── tests/
│       ├── test_agents.py
│       └── test_mcp_gateway.py
├── frontend/
│   # ... (frontend files)
└── # ... (project root files)
```

## Core Features & Data Flow
1.  A user submits trip details via the **Frontend**.
2.  The FastAPI **API** receives the request and passes it to the **Orchestrator Agent**.
3.  The **Orchestrator Agent** delegates tasks (e.g., "find flights") to specialized agents like the **Flight Agent**.
4.  The **Flight Agent** requests flight data by making a call to the **MCP Gateway**.
5.  The **MCP Gateway** connects to the external flight API, retrieves the data, and returns it in a standardized format to the Flight Agent.
6.  The **Orchestrator Agent** collects the results from all specialized agents and assembles the final trip plan.
7.  The plan is returned through the API to the **Frontend**.

## Security Considerations
- **MCP Gateway**: Manages all external API keys and credentials securely.
- **Input Validation**: Pydantic models for all data entering the agent system.
- **CORS**: Standard FastAPI configuration.

## Testing Strategy
- **Unit Tests**: For individual agents and MCP data transformations.
- **Integration Tests**: For the Orchestrator's ability to coordinate agents, mocking the MCP Gateway.
- **Coverage Goals**: Aim for >80% overall coverage.
