# AI Trip Planner - Task Breakdown

## General Development Guidance
- **Build Incrementally:** Follow the phases and tasks in order.
- **Test Continuously:** Write tests for each new piece of functionality.
- **Document Decisions:** If the architecture changes, update `architecture.md`.

## Phase 1: Project Setup & Core Backend

### Task 1.1: Initialize Project Structure
- [x] Create `backend` and `frontend` directories.
- [x] Set up the directory structure inside `backend` as defined in `architecture.md`.
- [x] Initialize git repository.
- [x] Create `requirements.txt` with `fastapi`, `uvicorn`, and `httpx`.
- [x] Create `.gitignore` for Python.

### Task 1.2: Setup FastAPI Application
- [x] Create the main FastAPI app instance in `backend/app/main.py`.
- [x] Set up a basic configuration in `backend/app/core/config.py`.
- [x] Create a health check endpoint (e.g., `/health`) to verify the server is running.

### Task 1.3: Create Pydantic Models
- [x] Create `TripRequest` model in `backend/app/models/trip.py` to handle incoming user requests.
- [x] Create initial response models for flights, hotels, etc.

### Task 1.4: Implement Core API Endpoint
- [x] Create the main `/plan` API endpoint in `backend/app/api/v1/trip.py`.
- [x] Initially, have it accept a `TripRequest` and return mock data.

### Task 1.5: Setup Testing Framework
- [x] Add `pytest` and `httpx` to `requirements.txt`.
- [x] Configure `pytest`.
- [x] Write a simple test for the `/health` endpoint.
- [x] Write a test for the `/plan` endpoint using mock data.

## Phase 2: Basic Frontend

### Task 2.1: Create HTML Structure
- [x] Create `frontend/index.html`.
- [x] Add a form to collect user input for destination, start date, and end date.
- [x] Add a submit button and a container to display results.

### Task 2.2: Add Basic Styling
- [x] Create `frontend/css/style.css`.
- [x] Add simple, clean styles for the form and results container.

### Task 2.3: Implement Frontend Logic
- [ ] Create `frontend/js/main.js`.
- [ ] Write JavaScript to capture form data on submit.
- [ ] Use the `fetch` API to send the data to the backend's `/plan` endpoint.
- [ ] Write a function to display the results returned from the backend.

## Phase 3: External API Integration

### Task 3.1: Flight Search Service
- [ ] Choose a flight search API (e.g., a free test API).
- [ ] Create `backend/app/services/flight_service.py`.
- [ ] Write a function to call the flight API using `httpx`, passing the user's criteria.
- [ ] Add API key handling via environment variables.

### Task 3.2: Hotel Search Service
- [ ] Choose a hotel search API.
- [ ] Create `backend/app/services/hotel_service.py`.
- [ ] Write a function to call the hotel API.

### Task 3.3: Integrate Services into Main Endpoint
- [ ] In the `/plan` endpoint, replace the mock data logic.
- [ ] Call the `flight_service` and `hotel_service` asynchronously.
- [ ] Combine the results into a single response.

### Task 3.4: Testing with Mocks
- [ ] Write unit tests for the `flight_service` and `hotel_service`, mocking the external API calls.
- [ ] Update the integration test for the `/plan` endpoint to use these mocks.

## Phase 4: Refinement and Finalization

### Task 4.1: Improve Frontend Display
- [ ] Format the JSON results from the API into a human-readable display.
- [ ] Add loading indicators while waiting for the API response.
- [ ] Implement basic error handling and display messages to the user if the API fails.

### Task 4.2: Add Attraction & Transport (Optional)
- [ ] If time permits, integrate a third service for attractions or transportation, following the pattern from Phase 3.

### Task 4.3: Final Review
- [ ] Review all code against the `code_styleguide.md`.
- [ ] Ensure all tests are passing.
- [ ] Write a `README.md` with instructions on how to set up and run the project.
