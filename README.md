# RicozTrigger MVP

A starter implementation of an enterprise-style event-driven automation platform.

## Architecture

Event Source
    ↓
Event Ingestion API
    ↓
Trigger Engine
    ↓
Condition Evaluation
    ↓
Workflow
    ↓
Action
    ↓
Execution Log

## Tech Stack

- Python
- FastAPI
- SQLite
- HTML/CSS/JavaScript
- REST APIs

## VS Code Setup

Open this folder in VS Code.

Create a virtual environment:

Windows:
    python -m venv .venv
    .venv\Scripts\activate

Install dependencies:

    pip install -r requirements.txt

Start the application:

    uvicorn app.main:app --reload

Open:

    http://127.0.0.1:8000

Swagger API documentation:

    http://127.0.0.1:8000/docs

## Create Demo Workflow and Trigger

Install requests:

    pip install requests

Run:

    python seed_demo.py

Then open the dashboard and click "Send Order Event".

The sample event has amount = 75000.
The trigger checks amount > 50000.
The workflow executes a notification action.
The execution is stored in SQLite.

## Suggested next development modules

1. User authentication and authorization
2. PostgreSQL database
3. Multiple event source connectors
4. Async event queue
5. Advanced condition builder
6. Multi-step workflows
7. Retry and failure handling
8. Webhook execution
9. Monitoring dashboard
10. Audit logs
11. Role-based access control
12. Unit and integration testing
