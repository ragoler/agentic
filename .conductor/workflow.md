# Project Workflow - AI Trip Planner

## Guiding Principles
1. **The Plan is the Source of Truth:** All work must be tracked in `plan.md`.
2. **The Status is Always Current:** `status.md` must be updated at the end of every work session.
3. **The Architecture is Deliberate:** Changes to the system design must be documented in `architecture.md` *before* implementation.
4. **Test-Driven Development:** Write tests for new backend functionality.

## Task Workflow

1.  **Select Task:** Choose the next unchecked task from `plan.md`.
2.  **Implement:** Perform the work required. For backend code, write tests first.
3.  **Verify:** Ensure the implementation works as expected and that all tests pass.
4.  **Document Deviations:** If the implementation differs from the architecture, update `architecture.md` and add a note explaining the change.
5.  **Mark Done:** Edit `plan.md` and change the task from `[ ]` to `[x]`.
6.  **Update Status:** Modify `status.md` to reflect the completion of the task.
7.  **Commit and Push:** Follow the Git Workflow to commit and push all changes.

## Development Commands

### Backend
```bash
# Navigate to the backend directory
cd backend

# Install dependencies
pip install -r requirements.txt

# Run development server
uvicorn app.main:app --reload
```

### Frontend
- Open `frontend/index.html` directly in a web browser.

### Testing
```bash
# Navigate to the backend directory
cd backend

# Run all tests
pytest
```

## Git Workflow
After completing a task and updating the plan and status files:

```bash
# Stage all changes
git add .

# Commit the changes (example message)
git commit -m "feat: Complete Task X.X - Description of task"

# Push to the remote repository
git push origin main
```

## Commit Guidelines
- Use descriptive, present-tense commit messages (e.g., `feat: Add flight search endpoint`).
- Group related changes for a single task into one commit.
